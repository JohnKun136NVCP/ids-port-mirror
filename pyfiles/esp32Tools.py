import pandas as pd #Import pandas for csv files
import socket #Socket will communicate with ESP32 and it sends information
import time #Sleep time to send information
from email.message import EmailMessage #Send a email notification
import Credentials #Passwords and tokens
import ssl #Email Certificates
import smtplib #Email protol (SMTP)
#Class esp32Tools get most important
class esp32Tools:
    def __init__(self,ip):
        self.ipget = ip #IP from ESP32
        self.ipsrc = "" #IP source
        self.ipdst = "" #IP Destination
        self.lengthsize = 0 #Size
        self.protocol = "" #Protocol
        self.greenRange = 100 #Green Led will turn on
        self.yellowRange = 150#Yellow Led will turn on
        self.redRange = 200#Red Led will turn on
        self.esp32Port = 80 #Port for webconnexion

class emailSender(esp32Tools):
    def __init__(self, ip):
        super().__init__(ip)
        self.emailSender = Credentials.AUTHOR_EMAIL
        self.emailPassword = Credentials.AUTHOR_PASS
        self.emailReceiver = Credentials.RECIPIENT_EMAIL
        self.smtpServer = Credentials.SMTPSERVER
        self.subject = ""
        self.body   = ""
        self.smtpProtocol = 587
    def subjectGet(self,subject):
        self.subject = subject
        return self.subject
    def bodyGet(self,body):
        self.body = body
        return self.body
    def sendEmail(self):
        email = EmailMessage()
        email['From'],email["To"],email["subject"] = self.emailSender,self.emailReceiver,self.subject
        email.set_content(self.body)
        with smtplib.SMTP(self.smtpServer,self.smtpProtocol) as smtpService:
            smtpService.starttls()
            smtpService.login(self.emailSender,self.emailPassword)
            smtpService.sendmail(self.emailSender,self.emailReceiver,email.as_string())

class csvFiles(emailSender):
    def __init__(self, ip,name):
        super().__init__(ip)
        self.nameFile = name #File name csv
        self.source= "" #Path from csv
        self.columns = "" #Number of columns
        self.rows = "" #Number of rows
        self.data = pd.read_csv(self.nameFile) #Read csv using Pandas

    def isFileCSV(self): #Method: Check if it is a csv file
        self.nameFile = str(self.nameFile) #Get the path
        if self.nameFile.lower().endswith('.csv'): #Compare .csv file
            print("File attached")
            return 1
        else:
            print("Path is incorrect or your file is broken")
            return -1
    def removeAdditionalID(self): #If column "No." exist, then this method will remove it
        self.columns = self.data.shape[1] #Get columns (Number)
        self.rows = self.data.shape[0] #Get rows (Number)
        if self.columns==7:
            try: #If it fails
                print("Delete ID column")
                self.data.drop("No.",inplace=True,axis=1) #Delete column "No."
                return self.data #Return data
            except:
                print("Column not found")
                return self.data #If  it doesn't fail, then return data
        return self.data  #If column is not on CSV then it'll return data


class esp32Data(csvFiles): #Subclass esp32Data sends
    def __init__(self, ip,name):
        super().__init__(ip,name)
        self.messageSign = "" #Values for leds to ESP32
        self.messagePort = ""#Local message
        self.counterMessage = 0
        self.counterTotal = len(self.data)
    def openSocket(self,typeMessage): #Open a socket
        self.messageSign = typeMessage
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.ipget, self.esp32Port))
            client_socket.sendall(self.messageSign.encode()) #Sends (0 or 1 or -1)
            client_socket.close()
        except:
            print("Check your ESP32 IP")
    def systemAlarm(self):
        try:
            self.data = self.removeAdditionalID()
        except:pass
        for self.ipsrc ,self.ipdst,self.protocol,self.lengthsize in zip(self.data["Source"],self.data['Destination'],self.data["Protocol"],self.data["Length"]): #loop for values from csv file
            self.counterMessage +=1
            time.sleep(4)
            if(self.lengthsize<=self.greenRange):
                self.messageSign = "0" #Sends a 0
                self.openSocket(self.messageSign)
                self.messagePort = "Everything's Fine"
                print("({}/{}) {}".format(self.counterMessage,self.counterTotal,self.messagePort))
                time.sleep(6)
            elif(self.lengthsize>self.greenRange and self.lengthsize<=self.yellowRange):
                self.messageSign = "1"#Sends a 1. Sends message "size of packet"
                self.messagePort = "Warning! Length packet: "+str(self.lengthsize)
                self.openSocket(self.messageSign)
                print("({}/{}) {}".format(self.counterMessage,self.counterTotal,self.messagePort))
                time.sleep(6)
            elif(self.lengthsize>=self.redRange or self.lengthsize>self.yellowRange):
                self.messageSign = "-1"#Sends a -1. Sends message "ipsrc and ipdst"
                subjectMessage = "SECURITY ALERT LOG!"
                bodyMessageComplete = "Hi,{}.\nThere was a problem with you network. It's been registered high traffic from the IPs {} to {}. Protocol: {}.\nPlease login into local session to check your traffic of server ESP32.".format(Credentials.RECIPIENT_EMAIL.split("@")[0],self.ipsrc,self.ipdst,self.protocol)
                self.messagePort = "High log!"
                esp32Data.subjectGet(self,subjectMessage)
                esp32Data.bodyGet(self,bodyMessageComplete)
                esp32Data.sendEmail(self)
                self.openSocket(self.messageSign)
                print("({}/{}) {}".format(self.counterMessage,self.counterTotal,self.messagePort))
                time.sleep(6)

