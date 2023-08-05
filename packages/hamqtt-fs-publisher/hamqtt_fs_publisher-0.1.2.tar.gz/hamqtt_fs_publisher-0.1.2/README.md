[![build](https://github.com/MarekPikula/homeassistant-mqtt-filesystem-publisher/workflows/build/badge.svg)](https://github.com/MarekPikula/homeassistant-mqtt-filesystem-publisher/actions?query=workflow%3Abuild+branch%3Amain)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hamqtt-fs_publisher.svg)](https://pypi.org/project/hamqtt-fs_publisher)

# HomeAssistant MQTT filesystem publisher

Publish file content as an MQTT topic compatible with HomeAssistant.

It can be useful, e.g., to publish system metrics from `/sys`.

## Quick start

1. Install the Python package: `pip install hamqtt-fs-publisher`. If you want to
   have support for YAML configuration format install with `ruamel` or `pyyaml`
   extras depending on the YAML library of choice (recommended `ruamel`, e.g.,
   `pip install hamqtt-fs-publisher[ruamel]`).
2. Create a configuration (example in `examples/config.example.yaml`). It can be
   in either YAML or JSON format. There is a pre-generated JSON schema in
   `hamqtt_fs_publisher/configuration.schema.json`, which can be used, e.g.,
   with VS Code (the current repository is pre-configured for `config.json` and
   `config.yaml`). Remember to set proper authorization details for the MQTT
   broker. If you are using the standard Mosquitto broker add-on in Home
   Assistant, please refer to the [official
   documentation](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md).
3. Run `hamqtt_fs_publisher --config <config_file_name>`.

> **Note:** The configuration file path could be either a relative/absolute
> path, or a file under `/etc/hamqtt_fs_publisher` or
> `~/.config/hamqtt_fs_publisher`.

## Systemd service

If you want to run this script as a systemd service you could copy the example
service file from `examples/hamqtt_fs_publisher@.service` to either
`/etc/systemd/system/` or `~/.config/systemd/user/` (if you want to run it in
user mode). Then copy the configuration file to one of the standard
configuration directories (i.e., `/etc/hamqtt_fs_publisher` or
`~/.config/hamqtt_fs_publisher`.)

To enable and start the unit in system mode run:

```shell
$ systemd daemon-reload
$ systemd enable --now hamqtt_fs_publisher@<config_file_name>
```

## Supported features

- Auto-discovery in HomeAssistant.
- Configuration with a simple YAML/JSON file.
- Possibility to create read-only sensor device entities with values taken
  from a file and published to the MQTT broker periodically with set intervals.

## TODO

- Add a logger to connect/disconnect events.
- Add an option to read a value on a button push in GUI (not only periodically).
- Add a switch endpoint (i.e., a file writer).
- Add a generic writer endpoint.
