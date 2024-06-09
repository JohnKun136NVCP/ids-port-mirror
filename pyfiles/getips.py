import serial
import serialpports as serport
import time
import os.path
def getIPs(): #Get ip from esp32 by SERIAL
    ips = []
    try:
        nameport = serport.ports() #Show ports
        esp = serial.Serial(nameport,115200)#Port selected
        print("REBOOT/RESET (EN button) your ESP32 to get IPS")#Make sure a reboot to work
        while (len(ips)<1):#Only send ip from esp32
            line = esp.readline().decode('utf-8').rstrip()
            ips.append(line)#IP
        esp.close()
        return ips #Return ip into a list
    except:
        return [] #If not connected or port is not available return []

def generateTxtFile(ipSta): #Generate ip and make directory if it is necessary
    path = os.path.abspath(os.getcwd())+"/.ip/ip.txt"
    if(os.path.isfile(path)!=True):
        os.mkdir(".ip");os.chdir(".ip/")
        with open("ip.txt","a") as file:
            file.write(ipSta)
    else:
        os.chdir(".ip/")
        option = input("Do you want to overwrite it? [Y/N]: ")
        if(option=="Y" or option=="yes" or option == "YES" or option=="y"):
            with open("ip.txt","w") as file:
                file.write(ipSta)
        else:
            print("Nothing to do here")


while (True):
    iplist = getIPs()
    if(iplist==[]):
        time.sleep(0.5)
        print("Fist, connect your esp32 to port serial,please")
    elif(iplist!=[]):
        ipsta = iplist[0]
        print("Your IP STA is: ",ipsta)
        print("Now you can unplugged your ESP32")
        break
generateTxtFile(ipsta)
