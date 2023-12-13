import hargassner
import sys, traceback, mysql

# You can generate an API token from the "API Tokens Tab" in the UI
influx_cred = { "url": "http://homeserver:8086",
                "token": "meinToken",
                "org": "Home",
                "bucket": "Hargassner" }


print("Parsing header information from 'test\\xml\\Full.DAQ'", flush=True)
channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")

print("Importing config file from 'channel_config.json'", flush=True)
channel_config = hargassner.import_config_file("channel_config.json")

print("Connecting to and logging data from 'HSV1'", flush=True)
#hargassner.connect_and_log_data(ip_address='HSV1', channel_infos=channel_infos, channel_config=channel_config, sql_connection=db)
hargassner.connect_and_log_data_influx(ip_address='HSV1.stein', channel_infos=channel_infos, channel_config=channel_config, influx_credentials=influx_cred)

print("Closing database connection", flush=True)
db.close();
