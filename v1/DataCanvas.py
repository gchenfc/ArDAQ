from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
import numpy as np

import time

class DataCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
        self.dataX = []
        self.dataY = [];
        self.plot()
        
    def plot(self):
        plt.ion()
        self.line1, = self.axes.plot(self.dataX,self.dataY, 'r-')
        self.axes.set_title('Data')
        self.axes.set_xlabel('time (s)')
        self.axes.set_ylabel('reading')
        FigureCanvas.updateGeometry(self)
        self.draw()
        self.lastPlotTime = time.time()
        
    def addPoint(self,x,y):
        self.dataX.append(x)
        self.dataY.append(y)
        if ((max(self.dataX)-min(self.dataX))>10):
            ind = (np.abs(np.array(self.dataX)-(self.dataX[-1]-10))).argmin()
            self.line1.set_xdata(self.dataX[ind:])
            self.line1.set_ydata(self.dataY[ind:])
            self.axes.set_xlim(left=self.line1.get_xdata()[-1]-10,right=self.line1.get_xdata()[-1])
        else:
            self.line1.set_xdata(self.dataX)
            self.line1.set_ydata(self.dataY)
            self.axes.set_xlim(left=min(self.line1.get_xdata()),right=self.line1.get_xdata()[-1])
        self.axes.set_ylim(bottom=0,#np.amin(self.line1.get_ydata()),
                            top=1.2*np.amax(self.line1.get_ydata()))
        if time.time()-self.lastPlotTime>.05:
            self.draw()
            self.lastPlotTime = time.time()
            print("plotted")
    def clearData(self):
        self.dataX = []
        self.dataY = []
        self.line1.set_xdata(self.dataX)
        self.line1.set_ydata(self.dataY)
        self.draw()
