import hargassner
import sys, traceback, mysql

# Open database connection
print("Opening database connection", flush=True)
db = mysql.connector.connect(host='localhost', database='volkszaehler', user='volkszaehler', password='meinPasswort', use_pure=True) # use pure Python implementation

print("Parsing header information from 'test\\xml\\Full.DAQ'", flush=True)
channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")

print("Importing config file from 'channel_config.json'", flush=True)
channel_config = hargassner.import_config_file("channel_config.json")

print("Connecting to and logging data from 'HSV1'", flush=True)
hargassner.connect_and_log_data(ip_address='HSV1', channel_infos=channel_infos, channel_config=channel_config, sql_connection=db)
#hargassner.connect_and_log_data_influx(ip_address='HSV1', channel_infos=channel_infos, channel_config=channel_config, influx_credentials=influx_cred)

print("Closing database connection", flush=True)
db.close();

