
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout, QGroupBox, QLabel, QPushButton, QFormLayout ,QMessageBox
from PyQt5 import QtGui
from time import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import serial
from serial.serialutil import SerialBase, SerialException, to_bytes, \
    PortNotOpenError, SerialTimeoutException, Timeout

import sys
import os
from datetime import date, datetime
sys.path.append("../")
from packages.serialCom import SerialCom
from PyQt5.QtCore import QThread, Qt, pyqtSignal
import pandas

sys.path.append("../design/")
from design import *


class Thread(QThread):
    changeLabelText = pyqtSignal(str)
    port = None
    stopped = False
    started= False
    
    def stop(self):
        self.stopped = True
    
        

    def run(self):
        print("running")
        ser = SerialCom()
        print("hello")
        ser.startCom(self.port) 
        data= {}        
        while True:
            print("hii")
            if self.port :
                serialData = ser.readLine()
                print(serialData)
                sensor , value = serialData.split(":")
                
                self.changeLabelText.emit(serialData)
                if sensor in data.keys():
                    values = data[sensor]["values"]
                    values.append(value)
                    times = data[sensor]["time"]
                    times.append(datetime.now())
                    data[sensor]["values"] = values
                    data[sensor]["time"] = times
                    
                                
                
                else :
                    data[sensor] = {
                    "values" : [value],
                    "time" : [datetime.now()]
                }
            if self.stopped :
                print("stopped")   
                print("saving data")
                for sensor in data :
                    pd =pandas.DataFrame(data[sensor])
                    print(pd.head())
                    pd.to_csv(sensor + ".csv", index=False)
                break
   
    



class main(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        

    def addDisplayLables(self):
        horizontalLayout_values = QtWidgets.QHBoxLayout()
        horizontalLayout_values.setObjectName("horizontalLayout_values")
        ValueLabel = QtWidgets.QLabel(self.display)
        ValueLabel.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";")
        ValueLabel.setObjectName("ValueLabel")
        horizontalLayout_values.addWidget(ValueLabel)
        ValueLabel_2 = QtWidgets.QLabel(self.display)
        ValueLabel_2.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";")
        ValueLabel_2.setObjectName("ValueLabel_2")
        horizontalLayout_values.addWidget(ValueLabel_2)
        ValueLabel_3 = QtWidgets.QLabel(self.display)
        ValueLabel_3.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";")
        ValueLabel_3.setObjectName("ValueLabel_3")
        horizontalLayout_values.addWidget(ValueLabel_3)
        self.verticalLayout_2.addLayout(horizontalLayout_values)
        return [ValueLabel, ValueLabel_2, ValueLabel_3]
    
    





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())