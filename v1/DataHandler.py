import numpy as np
import scipy.io as sio
from threading import Lock

# this class is thread safe
class DataHandler():
    def __init__(self,numDatum):
        print(numDatum)
        self.numDatum = numDatum;
        self.data = np.zeros([0,numDatum]);
        self.xInd = 0;
        self.yInd = [0];

        self.lock = Lock()
        
        self.recentDuration=5

    # select ind/dep variables
    def setXInd(self,ind):
        self.xInd = ind
    def setYInd(self,inds):
        assert isinstance(lst, (list, tuple))
        self.yInd = inds
    def addYInd(self,ind):
        self.yInd.append(ind)
    def removeYInd(self,ind):
        self.yInd.remove(ind)

    # set plotting buffer size
    def setRecentDuration(self,newDuration):
        self.recentDuration = newDuration

    # add a line of data
    def addLine(self,dataLine,blocking=False,timeout=-1):
        if self.lock.acquire(blocking=blocking,timeout=timeout):
            self.data = np.append(self.data,[dataLine],axis=0)
            self.lock.release()

    # get data
    def getCurrX(self):
        return self.data[-1,self.xInd]
    def getCurrY(self):
        return self.data[-1,self.yInd]
    def getCurrPoint(self):
        return [self.data[-1,self.xInd],self.data[-1,self.yInd]]
    def getAllXs(self):
        return self.data[:,self.xInd]
    def getAllYs(self):
        return self.data[:,self.yInd]
    def getAllPoints(self):
        return [self.data[:,self.xInd],self.data[:,self.yInd]]
    def getRecentXs(self):
        if self.lock.acquire():
            startInd = (np.abs(self.data[:,self.xInd]-self.recentDuration)).argmin()
            toRet = self.data[startInd:,self.xInd]
            self.lock.release()
            return toRet
        return None
    def getRecentYs(self):
        if self.lock.acquire():
            startInd = (np.abs(self.data[:,self.xInd]-self.recentDuration)).argmin()
            toRet = self.data[startInd:,self.yInd]
            self.lock.release()
            return toRet
        return None
    def getRecentPoints(self): # return format: [x,[y1,y2,y3,...]]
        if self.lock.acquire():
            startInd = (np.abs(self.data[:,self.xInd]-self.recentDuration)).argmin()
            toRet = [self.data[startInd:,self.xInd],self.data[startInd:,self.yInd]]
            self.lock.release()
            return toRet
        return None

    # save data
    def saveDataMatlab(self,filename="data/data.mat"):
        sio.savemat(filename,{'data':self.data})
    def saveDataPickle(self,filename="data/data.npy"):
        np.save(filename,self.data)
    def saveDataTxt(self,filename="data/data.txt"):
        np.savetxt(filename,self.data,delimiter="\t")
    def clearData(self):
        self.lock.acquire()
        self.data = np.zeros([0,self.numDatum]);
        self.lock.release()
    #def collectFromArduino
