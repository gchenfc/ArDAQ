import sys
import serial
from serial.tools import list_ports
from parse import compile
from parse import *
import threading
import time

class AlicatInterface():
    def __init__(self):
        self.serialName = '/dev/tty.usbserial'
        self.baudRate = 57600
        self.timeout = 1000
        self.ser = serial.Serial()
        self.ser.write_timeout=1;
        self.ser.timeout=0;
        datVec = "A +0.0 +0.0 +0.0 +0.0 Air".split(' ');
        self.mostRecentData = datVec;
        self.collecting = False;

    def start(self):
        try:
            self.ser.baudrate = self.baudRate
            self.ser.port = self.serialName
            self.ser.timeout = self.timeout
            if not self.ser.isOpen():
                self.ser.open()
            self.collecting = True;
            self.collectThread = threading.Thread(target=self.collectData)
            self.collectThread.start();
        except:
            print("Alicat not connected!!! not collecting h2 consumption...")
    def collectData(self):
        while self.collecting:
            self.poll()
            tmp = self.readLineData();
            self.mostRecentData = tmp
    def stop(self):
        self.collecting = False
    def getMostRecentData(self):
        print(self.mostRecentData)
        return self.mostRecentData
    def poll(self):
        try:
            self.ser.write(b'A\r')
        except:
            print('Alicat Poll Error')
    def readLine(self):
        try:
            startTime = time.time()
            toRet = ""
            thisChar = ""
            while (thisChar != chr(13)) and (time.time()-startTime<.1):
                thisChar = self.ser.read().decode()
                toRet = toRet+thisChar
        except:
            print("error")
            return ""
        while(len(toRet)!=0 and (toRet[-1]=='\n' or toRet[-1]=='\r')):
            toRet = toRet[0:-1]
        return toRet
    def readLineData(self):
        dat = self.readLine();
        datVec = dat.split(' ');
        return datVec;
        
    def close(self):
        if self.ser.isOpen():
            self.ser.close()

    def setSerialName(self,name):
        self.serialName = name
    def setBaud(self,baud):
        self.baudRate = baud
    def setTimeout(self,time):
        self.timeout = time
    def setLineFormat(self,strFormat):
        self.lineFormat = compile(strFormat+"{:s}")

if __name__ == '__main__':
    ali = AlicatInterface()
    ali.start()
    print("started")
    ali.poll()
    print("polled")
    #dat = ali.ser.read(10).decode()
    print(ali.readLine())
    print("readline")
    ali.close()
