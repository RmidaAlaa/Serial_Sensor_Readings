# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import  QScrollArea, QVBoxLayout, QGroupBox, QFormLayout

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 900))
        MainWindow.setStyleSheet("\n"
"background-color: rgb(252, 252, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 10, 1100, 135))
        self.header.setMinimumSize(QtCore.QSize(1000, 0))
        self.header.setStyleSheet("background-color: \n"
"#FFFFFF; ")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.kumuluslogo = QtWidgets.QLabel(self.header)
        self.kumuluslogo.setGeometry(QtCore.QRect(10, 0, 261, 161))
        self.kumuluslogo.setText("")
        self.kumuluslogo.setPixmap(QtGui.QPixmap("../../../Downloads/index.png"))
        self.kumuluslogo.setObjectName("kumuluslogo")
        self.APPTitle = QtWidgets.QLabel(self.header)
        self.APPTitle.setGeometry(QtCore.QRect(390, 30, 411, 61))
        self.APPTitle.setStyleSheet("font: 75 11pt \"Ubuntu Condensed\";\n"
"color: #2E279D;\n"
"font: 90 20pt \"Waree\";")
        self.APPTitle.setObjectName("APPTitle")
        self.body = QtWidgets.QFrame(self.centralwidget)
        self.body.setGeometry(QtCore.QRect(0, 150, 1100, 900))
        self.body.setMinimumSize(QtCore.QSize(1100, 900))
        self.body.setMaximumSize(QtCore.QSize(1100, 900))
        self.body.setStyleSheet("background-color: #FFFFFF;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.frame = QtWidgets.QFrame(self.body)
        self.frame.setGeometry(QtCore.QRect(10, 10, 171, 271))
        self.frame.setStyleSheet("background-color: #ACE5FF;\n"
"border-radius: 12px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.COM = QtWidgets.QComboBox(self.frame)
        self.COM.setMinimumSize(QtCore.QSize(5, 50))
        self.COM.setMaximumSize(QtCore.QSize(150, 50))
        self.COM.setStyleSheet("background-color: rgb(252, 252, 252);")
        self.COM.setObjectName("COM")
        self.verticalLayout.addWidget(self.COM)
        self.startButton = QtWidgets.QPushButton(self.frame)
        self.startButton.setMinimumSize(QtCore.QSize(150, 80))
        self.startButton.setStyleSheet(" display:inline-block;\n"
"font: 75 11pt \"Ubuntu Condensed\";\n"
"font: 63 15pt \"URW Bookman\";\n"
"background-color: #2b9348;\n"
" padding:0.3em 1.2em;\n"
" margin:0 0.1em 0.1em 0;\n"
" border:0.16em ;\n"
" border-radius:2em;\n"
"color: rgb(252, 252, 252);\n"
"")
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QToolButton(self.frame)
        self.stopButton.setMinimumSize(QtCore.QSize(150, 80))
        self.stopButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stopButton.setStyleSheet("font: 63 15pt \"URW Bookman\";\n"
"color: rgb(252, 252, 252);\n"
"background-color: rgb(204, 0, 0);\n"
"border-radius: 12px;")
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.display = QtWidgets.QFrame(self.body)
        self.display.setGeometry(QtCore.QRect(190, 10, 791, 291))
        self.display.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.display.setFrameShadow(QtWidgets.QFrame.Raised)
        self.display.setObjectName("display")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.display)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SensoHeader = QtWidgets.QLabel(self.display)
        self.SensoHeader.setMinimumSize(QtCore.QSize(40, 30))
        self.SensoHeader.setMaximumSize(QtCore.QSize(170, 70))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.SensoHeader.setFont(font)
        self.SensoHeader.setStyleSheet("color: rgb(46, 39, 157);\n"
"font: 80 20pt \"URW Bookman\";\n"
"background-color: #FFFFFF;")
        self.SensoHeader.setObjectName("SensoHeader")
        self.horizontalLayout.addWidget(self.SensoHeader)
        self.VoltageHeader = QtWidgets.QLabel(self.display)
        self.VoltageHeader.setMaximumSize(QtCore.QSize(170, 70))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.VoltageHeader.setFont(font)
        self.VoltageHeader.setStyleSheet("color: rgb(46, 39, 157);\n"
"\n"
"font: 80 20pt \"URW Bookman\";\n"
"background-color: #FFFFFF;")
        self.VoltageHeader.setObjectName("VoltageHeader")
        self.horizontalLayout.addWidget(self.VoltageHeader)
        self.ValueHeader = QtWidgets.QLabel(self.display)
        self.ValueHeader.setMaximumSize(QtCore.QSize(170, 70))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.ValueHeader.setFont(font)
        self.ValueHeader.setStyleSheet("color: rgb(46, 39, 157);\n"
"font: 80 20pt \"URW Bookman\";\n"
"background-color: #FFFFFF;\n"
"")
        self.ValueHeader.setObjectName("ValueHeader")
        self.horizontalLayout.addWidget(self.ValueHeader)
        self.DateHeader = QtWidgets.QLabel(self.display)
        self.DateHeader.setMaximumSize(QtCore.QSize(170, 70))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.DateHeader.setFont(font)
        self.DateHeader.setStyleSheet("color: rgb(46, 39, 157);\n"
"font: 80 20pt \"URW Bookman\";\n"
"background-color: #FFFFFF;")
        self.DateHeader.setObjectName("DateHeader")
        self.horizontalLayout.addWidget(self.DateHeader)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.display)
        self.groupBox.setMinimumSize(QtCore.QSize(500, 500))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 761, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_values = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_values.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_values.setObjectName("horizontalLayout_values")
        self.SensorLabel = QtWidgets.QLabel(self.layoutWidget)
        self.SensorLabel.setMinimumSize(QtCore.QSize(150, 50))
        self.SensorLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.SensorLabel.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.SensorLabel.setObjectName("SensorLabel")
        self.horizontalLayout_values.addWidget(self.SensorLabel)
        self.Tensionlabel = QtWidgets.QLabel(self.layoutWidget)
        self.Tensionlabel.setMinimumSize(QtCore.QSize(150, 50))
        self.Tensionlabel.setMaximumSize(QtCore.QSize(100, 100))
        self.Tensionlabel.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.Tensionlabel.setObjectName("Tensionlabel")
        self.horizontalLayout_values.addWidget(self.Tensionlabel)
        self.Valueelabel = QtWidgets.QLabel(self.layoutWidget)
        self.Valueelabel.setMinimumSize(QtCore.QSize(150, 50))
        self.Valueelabel.setMaximumSize(QtCore.QSize(200, 50))
        self.Valueelabel.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Valueelabel.setObjectName("Valueelabel")
        self.horizontalLayout_values.addWidget(self.Valueelabel)
        self.Datelabel = QtWidgets.QLabel(self.layoutWidget)
        self.Datelabel.setMinimumSize(QtCore.QSize(150, 50))
        self.Datelabel.setMaximumSize(QtCore.QSize(200, 50))
        self.Datelabel.setStyleSheet("font: 12pt \"Nirmala UI Semilight\";\n"
"background-color: rgb(255, 255, 255);")
        self.Datelabel.setObjectName("Datelabel")
        self.horizontalLayout_values.addWidget(self.Datelabel)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.Copyright = QtWidgets.QLabel(self.body)
        self.Copyright.setGeometry(QtCore.QRect(956, 676, 131, 31))
        self.Copyright.setStyleSheet("image: url(:/newPrefix/droits-dauteur.png);")
        self.Copyright.setText("")
        self.Copyright.setObjectName("Copyright")
        self.Curve = QtWidgets.QGraphicsView(self.body)
        self.Curve.setGeometry(QtCore.QRect(190, 310, 791, 361))
        self.Curve.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.Curve.setObjectName("Curve")
        self.VisualiseButton = QtWidgets.QPushButton(self.body)
        self.VisualiseButton.setGeometry(QtCore.QRect(30, 300, 131, 61))
        self.VisualiseButton.setStyleSheet("border-radius: 12px;\n"
"background-color: #46B3E6;\n"
" padding:0.3em 1.2em;\n"
" margin:0 0.1em 0.1em 0;\n"
" border:5px ;\n"
" border-radius:5 px;\n"
" box-sizing: border-box;")
        self.VisualiseButton.setObjectName("VisualiseButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 22))
        self.menubar.setObjectName("menubar")
        self.menuInterface = QtWidgets.QMenu(self.menubar)
        self.menuInterface.setObjectName("menuInterface")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuInterface.menuAction())
        scroll_bar = QtWidgets.QScrollBar(self.display)
  
        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet("background : lightgreen;")
  
        # setting vertical scroll bar to it
        #self.display.setVerticalScrollBar(scroll_bar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MainWindow = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.APPTitle.setText(_translate("MainWindow", "Kumulus  Sensor Calibrating "))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop | Save"))
        self.SensoHeader.setText(_translate("MainWindow", "Sensor"))
        self.VoltageHeader.setText(_translate("MainWindow", "Tension"))
        self.ValueHeader.setText(_translate("MainWindow", "Value"))
        self.DateHeader.setText(_translate("MainWindow", "Date"))
        self.SensorLabel.setText(_translate("MainWindow", "TT"))
        self.Tensionlabel.setText(_translate("MainWindow", "TT"))
        self.Valueelabel.setText(_translate("MainWindow", "TT"))
        self.Datelabel.setText(_translate("MainWindow", "TT"))
        self.VisualiseButton.setText(_translate("MainWindow", "Visualisation"))
        self.menuInterface.setTitle(_translate("MainWindow", "Interface"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
