import sys
import serial
from serial.tools import list_ports
from parse import compile
from parse import *
import threading
from threading import Lock

class ArduinoInterface():
    def __init__(self):
        self.serialName = ''
        self.baudRate = 115200
        self.timeout = 1000
        self.write_timeout = 2000;
        self.ser = serial.Serial()
        self.lineFormat = compile('')
        self.lock = Lock()
        self.reading = False;

    def start(self):
        if(self.ser.isOpen()):
            return
        self.ser.baudrate = self.baudRate
        self.ser.port = self.serialName
        self.ser.timeout = self.timeout
        self.ser.write_timeout = self.write_timeout;
        if not self.ser.isOpen():
            self.ser.open()
        threading.Timer(.5,self.flushInputBuffer).start()

    def readLine(self):
        self.reading = True;
        self.lock.acquire()
        try:
            toRet = self.ser.readline().decode()
        except:
            self.lock.release()
            return ""
        while(len(toRet)!=0 and (toRet[-1]=='\n' or toRet[-1]=='\r')):
            toRet = toRet[0:-1]
        self.lock.release()
        return toRet
    def readLineFloats(self,numFloats):
        datas = []
        toRet = []
        while(len(datas)!=numFloats):
            try:
                datas = self.readLine().split("\t")
                if len(datas)==2:
                    for i in range(len(datas)):
                        toRet.append(float(datas[i]))
            except:
                datas = []
        return toRet
    def readLineFormat(self,strFormat=None):
        try:
            if strFormat==None:
                strFormat = self.lineFormat
            ret = strFormat.parse(self.readLine()+" ")
            if ret == None:
                return None
        except:
            return ""
        return ret.fixed[:-1]

    def flushInputBuffer(self):
        try:
            if(self.reading):
                self.reading = False;
                self.lock.acquire()
                self.ser.reset_input_buffer()
                self.lock.release()
                print ("**************flushed buffer**************")
                threading.Timer(.5,self.flushInputBuffer).start()
        except:
            self.lock.release()

    def sendLine(self,textToSend=''):
        print("textToSend:"+textToSend)
        self.lock.acquire()
        try:
            toRet = self.ser.write(textToSend.encode())
        except:
            print("send failed...")
            toRet = 0
        self.lock.release()
        return toRet
        
    def close(self):
        if not self.ser.isOpen():
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
    ard = ArduinoInterface()
    ard.serialName = serial.tools.list_ports.comports()[3].device
    ard.start()
    dat = ard.readLine()
    print(ard.readLineFloats(2))
    print(ard.readLineFloats(2))
    print(ard.readLineFloats(2))
    print(ard.readLineFloats(2))
    ard.close()
