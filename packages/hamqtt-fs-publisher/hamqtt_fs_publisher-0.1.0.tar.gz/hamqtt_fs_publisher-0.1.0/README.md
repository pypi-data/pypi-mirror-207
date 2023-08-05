# HomeAssistant MQTT filesystem publisher

Publish file content as an MQTT topic compatible with HomeAssistant.

It can be useful, e.g., to publish system metrics from `/sys`.

## Quick start

1. Install the Python package: `pip install hamqtt-fs-publisher`.
2. Create a configuration (example in `config.example.yaml`). It can be either
   YAML or JSON. There is a pre-generated JSON schema in
   `hamqtt_fs_publisher/configuration.schema.json`, which can be used, e.g.,
   with VS Code (the current repository is pre-configured for `config.json` and
   `config.yaml`). Remember to set proper authorization details for the MQTT
   broker. If you are using the standard Mosquitto broker add-on in Home
   Assistant, please refer to the [official
   documentation](https://github.com/home-assistant/addons/blob/master/mosquitto/DOCS.md).
3. Run `hamqtt_fs_publisher --config <config_file_name>`.

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
