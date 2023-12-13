import hargassner
import sys, traceback
import socket

mqtt_cred = { "broker": "nas.stein",
              "port": 1883,
              "username": "Hargassner_Gateway",
              "password": "meinPasswort",
              "cliend_id": socket.gethostname()}


print("Parsing header information from 'test\\xml\\Full.DAQ'", flush=True)
channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")

#print("Importing config file from 'channel_config.json'", flush=True)
#channel_config = hargassner.import_config_file("channel_config.json")

print("Connecting to and logging data from 'HSV1'", flush=True)
#hargassner.connect_and_log_data(ip_address='HSV1', channel_infos=channel_infos, channel_config=channel_config, sql_connection=db)
#hargassner.connect_and_log_data_influx(ip_address='HSV1.stein', channel_infos=channel_infos, channel_config=channel_config, influx_credentials=influx_cred)
hargassner.connect_and_log_data_mqtt(ip_address='HSV1.stein', channel_infos=channel_infos, mqtt_credentials=mqtt_cred)

print("Closing connection", flush=True)


