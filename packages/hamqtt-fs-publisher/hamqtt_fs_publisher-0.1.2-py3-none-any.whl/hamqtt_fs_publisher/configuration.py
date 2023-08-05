"""HomeAssistant MQTT fs publisher configuration."""

import json
from pathlib import Path
from typing import List, Optional

from ha_mqtt.util import EntityCategory, HaDeviceClass  # type: ignore
from pydantic import BaseModel, Field

try:
    from pydantic_yaml import YamlModel
except ImportError:
    # Fall back to JSON-only model.
    from pydantic import (  # type: ignore # pylint: disable=W0404,C0412 # isort: skip
        BaseModel as YamlModel,
    )


class Mqtt(BaseModel):  # pylint: disable=R0903
    """MQTT configuration."""

    client_id: str = Field(description="MQTT client ID.")
    host: str = Field("localhost", description="MQTT broker host.")
    port: int = Field(1883, description="MQTT broker port number.")
    user: Optional[str] = Field(None, description="Optional MQTT username.")
    password: Optional[str] = Field(None, description="Optional MQTT password.")


class ReadMixin(BaseModel):  # pylint: disable=R0903
    """Filesystem read-only mixin."""

    read_path: Path = Field(description="Path to read the value from.")
    read_interval: float = Field(10.0, description="Read interval in seconds.")
    read_strip: bool = Field(
        True, description="Perform a strip operation on the read value."
    )


class WriteMixin(BaseModel):  # pylint: disable=R0903
    """Filesystem write-only mixin."""

    write_path: Path = Field(description="Path to write the value to.")


class Sensor(ReadMixin):  # pylint: disable=R0903
    """Sensor configuration."""

    unit: str = Field("", description='Unit of measurement, example: "°C",')
    device_class: HaDeviceClass = Field(
        description=(
            "An entry of the device class enum containing the device class as in "
            "https://www.home-assistant.io/integrations/sensor/#device-class"
        )
    )


class Entity(BaseModel):  # pylint: disable=R0903
    """MQTT device configuration."""

    name: str = Field(
        description="Friendly name of the device to be shown in HomeAssistant."
    )
    unique_id: str = Field(
        description="Unique id to identify this device against HomeAssistant."
    )
    entity_type: EntityCategory = Field(
        EntityCategory.PRIMARY,
        description=(
            "Choose CONFIG for entities that configure a device and DIAGNOSTIC for "
            "entities that reveal additional read-only information about a device"
        ),
    )
    sensor: Optional[Sensor] = Field(None, description="Sensor specification.")


class HaDevice(BaseModel):  # pylint: disable=R0903
    """HomeAssistant device grouping multiple entities."""

    name: str = Field(description="Friendly name of the device.")
    unique_id: str = Field(
        description=(
            "One unique identifier that is used by HA "
            "to assign entities to this device."
        )
    )

    entities: List[Entity] = Field(
        default_factory=list, description="List of MQTT entities."
    )


class Config(YamlModel):  # pylint: disable=R0903
    """Base configuration."""

    mqtt: Mqtt = Field(description="MQTT configuration.")
    devices: List[HaDevice] = Field(
        default_factory=list, description="Device configuration."
    )


if __name__ == "__main__":
    CONFIG_SCHEMA = Path(__file__).parent / "configuration.schema.json"
    with open(CONFIG_SCHEMA, "w", encoding="utf-8") as schema_file:
        print(f"Writing configuration schema to {CONFIG_SCHEMA}.")
        schema_file.write(json.dumps(Config.schema(), indent=4))
