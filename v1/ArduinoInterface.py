import sys
import serial
from serial.tools import list_ports
from parse import compile
from parse import *

class ArduinoInterface():
    def __init__(self):
        self.serialName = ''
        self.baudRate = 115200
        self.timeout = 1000
        self.ser = serial.Serial()
        self.lineFormat = compile('')

    def start(self):
        self.ser.baudrate = self.baudRate
        self.ser.port = self.serialName
        self.ser.timeout = self.timeout
        if not self.ser.isOpen():
            self.ser.open()

    def readLine(self):
        try:
            toRet = self.ser.readline().decode()
        except:
            return ""
        while(len(toRet)!=0 and (toRet[-1]=='\n' or toRet[-1]=='\r')):
            toRet = toRet[0:-1]
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
        if strFormat==None:
            strFormat = self.lineFormat
        ret = strFormat.parse(self.readLine()+" ")
        if ret == None:
            return None
        return ret.fixed[:-1]
        
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
