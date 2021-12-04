cd /D E:\Messdaten\Temperaturen\Hargassner_Gateway\

echo ############################################################### >> errors_influx.txt
date /T >> errors_influx.txt
time /T >> errors_influx.txt

date /T > debug_influx.txt
time /T >> debug_influx.txt

"C:\Program Files\Python37\python.exe" E:\Messdaten\Temperaturen\Hargassner_Gateway\parse_and_log_influx.py >> debug_influx.txt 2>> errors_influx.txt
