import hargassner
import sys, traceback, mysql

# Open database connection
db = mysql.connector.connect(host='localhost', database='volkszaehler', user='volkszaehler', password='meinPasswort', use_pure=True) # use pure Python implementation

channel_infos = hargassner.parse_header_information("test\\xml\\Full.DAQ")
general_config = hargassner.import_config_file("config.json")
channel_config = hargassner.import_config_file("channel_config.json")

hargassner.create_vz_channels(general_config=general_config, 
                              channel_config=channel_config,
                              sql_connection=db)