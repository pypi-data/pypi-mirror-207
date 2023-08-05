"""HomeAssistant MQTT filesystem publisher service."""

import time
from pathlib import Path
from threading import Event, Timer
from typing import List, Optional

import click
from ha_mqtt.ha_device import HaDevice  # type: ignore
from ha_mqtt.mqtt_device_base import MqttDeviceBase, MqttDeviceSettings  # type: ignore
from ha_mqtt.mqtt_sensor import MqttSensor  # type: ignore
from loguru import logger
from paho.mqtt.client import Client

from .configuration import Config, ReadMixin


class MqttReader:
    """MQTT file reader publisher."""

    def __init__(
        self, device_name: str, entity_config: ReadMixin, entity: MqttDeviceBase
    ):
        """Initialize a MQTT file reader publisher.

        Arguments:
            device_name -- name of the HA device.
            entity_config -- entity configuration.
            entity -- MQTT entity.
        """
        self._device = device_name
        self._config = entity_config
        self._entity = entity
        self._log_name = f"{device_name}/{entity.name}"
        self._timer: Optional[Timer] = None
        self._stop_event = Event()
        logger.info(
            '{}: Initialized reader for file "{}".',
            self._log_name,
            entity_config.read_path,
        )

    def publish_read(self):
        """Read a value from file and publish it to MQTT broker."""
        state = self._config.read_path.read_text("utf-8")
        if self._config.read_strip:
            state = state.strip()
        logger.debug('{}: Publishing state "{}".', self._log_name, state)
        self._entity.publish_state(state)
        if not self._stop_event.is_set():
            self.start(False)

    def start(self, log: bool = True):
        """Start the periodic reading."""
        if self._stop_event.is_set():
            return
        if log:
            logger.info(
                "{}: Starting periodic read with {}s interval.",
                self._log_name,
                self._config.read_interval,
            )
        if self._timer is not None:
            self._timer.cancel()
        self._timer = Timer(self._config.read_interval, self.publish_read)
        self._timer.start()

    def close(self):
        """Close the reader and clean up the MQTT state."""
        logger.info("{}: Closing reader.", self._log_name)
        self._stop_event.set()
        if self._timer is not None:
            self._timer.cancel()
        self._entity.close()


@click.command()
@click.option(
    "--config",
    "-c",
    default="config.yaml",
    type=click.Path(dir_okay=False, path_type=Path),
    help="Configuration file (either YAML or JSON).",
)
def main(config: Path):
    """Run the HA MQTT filesystem publisher."""
    logger.info("Parsing configuration...")
    config_found = False
    config_default_dir = Path("hamqtt_fs_publisher")
    for prefix in (
        Path(),
        Path("/etc") / config_default_dir,
        Path.home() / ".config" / config_default_dir,
    ):
        tried_path = prefix / config
        if tried_path.exists() and not tried_path.is_dir():
            config_found = True
            config = tried_path
            logger.debug('Found configuration in "{}".', config)
            break

    if not config_found:
        logger.error('Configuration not found at "{}" path.', config)

    config_parsed = Config.parse_file(config)

    logger.info("Connecting to MQTT broker...")
    mqtt_config = config_parsed.mqtt
    client = Client(mqtt_config.client_id)
    if mqtt_config.user is not None:
        client.username_pw_set(mqtt_config.user, mqtt_config.password)
    client.connect(mqtt_config.host, mqtt_config.port)
    client.loop_start()

    logger.info("Reading MQTT device configuration...")
    readers: List[MqttReader] = []
    for device_config in config_parsed.devices:
        device = HaDevice(device_config.name, device_config.unique_id)
        for entity_config in device_config.entities:
            settings = MqttDeviceSettings(
                entity_config.name,
                entity_config.unique_id,
                client,
                device,
                entity_config.entity_type,
            )
            sensor_config = entity_config.sensor
            if sensor_config is not None:
                # For now, there is support only for read-only sensors.
                reader = MqttReader(
                    device_config.name,
                    sensor_config,
                    MqttSensor(
                        settings,
                        sensor_config.unit,
                        sensor_config.device_class,
                        send_only=True,
                    ),
                )
                # Try to publish the initial value and start periodic reader.
                reader.publish_read()
                reader.start()
                readers.append(reader)

    logger.info("Initialization complete.")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        # Close all devices for cleanup. Gets marked as offline/unavailable in
        # HomeAssistant.
        for reader in readers:
            reader.close()
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter
