cd /D E:\Messdaten\Temperaturen\Hargassner_Gateway\

echo ############################################################### >> errors.txt
date /T >> errors.txt
time /T >> errors.txt

date /T > debug.txt
time /T >> debug.txt

"C:\Program Files\Python37\python.exe" E:\Messdaten\Temperaturen\Hargassner_Gateway\parse_and_log.py >> debug.txt 2>> errors.txt
