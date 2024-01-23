# hargassner_gateway
Python code to log data from a Hargassner Nano-PK pellet heating.

## Logging destination possibilities
* volkszähler (mysql database), see https://volkszaehler.org/
* InfluxDB 2.x
* MQTT broker


## Tested with
* Hargassner Nano-PK 20–32 kW (https://www.hargassner.com/de-de/heizungen/pelletheizung/nano-pk-20-32-kw/)

## Instructions
* Connect the heating system via ethernet at touch-panel front. Maybe internal ethernet connection can also be used, this is not tested.
* Get parameter description from sd-card logging
  * Insert SD-Card into sd-card slot at touch-panel front.
  * Enable SD-Card logging for some moments via touch-panel (```Einstellungen``` --> ```Setup``` --> ```Datenaufzeichnung (SD)``` --> ```SD Logging starten```)
  * Stop the logging after a short time and copy file from sd-card to the python script location, e.g. to ```.\test\xml\Full.DAQ```
* Modify desired startscript to match database server, credentials, path to sd-card logging file, etc. and run it with python
  * ```parse_and_log_mysql.py```
  * ```parse_and_log_influx.py```
  * ```parse_and_log_mqtt.py```
