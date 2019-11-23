import hargassner
import sys, traceback, mysql

# Open database connection
db = mysql.connector.connect(host='homeserver', database='volkszaehler', user='volkszaehler', password='meinPasswort', use_pure=True) # use pure Python implementation

channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")
channel_config = hargassner.import_config_file("channel_config.json")
hargassner.connect_and_log_data(ip_address='10.0.0.25', channel_infos=channel_infos, channel_config=channel_config, sql_connection=db)

