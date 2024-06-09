import sys
import os
import esp32Tools as esp32t
def openIP(ippath):
    with open(ippath,'r') as ipfile:
        return ipfile.readline()


if len(sys.argv)== 3:
    print("Checking CSV path and IP file...")
    if (os.path.isfile(sys.argv[1])==True and os.path.isfile(sys.argv[2])):
        print("Starting IDS listener")
        esp32IDS = esp32t.esp32Data(openIP(sys.argv[2]),sys.argv[1])
        print("If you have not started the IDS, please REBOOT/RESET (EN button) your ESP32...")
        esp32IDS.systemAlarm()
    else:
        print("May your CSV doesn't exist or your ip file doesn't exist. Please, check your directories.")

else:
    print("Script needs esp32listner.py ipfilepath ipfilepath")
