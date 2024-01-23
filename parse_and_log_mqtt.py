import hargassner
import sys, traceback
import socket

# MQTT credentials
mqtt_cred = { "broker": "nas.stein",
              "port": 1883,
              "username": "Hargassner_Gateway",
              "password": "meinPasswort",
              "cliend_id": socket.gethostname()}


print("Parsing header information from 'test\\xml\\Full.DAQ'", flush=True)
channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")

print("Connecting to and logging data from 'HSV1'", flush=True)
hargassner.connect_and_log_data_mqtt(ip_address='HSV1.stein', channel_infos=channel_infos, mqtt_credentials=mqtt_cred)

print("Closing connection", flush=True)


