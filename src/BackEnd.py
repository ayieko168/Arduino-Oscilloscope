from PyQt4.QtGui import *
from MainWindowFrontEnd import *

import pyqtgraph as pg
import random
import os
import datetime

import csv, json, xml

def _map(value, in_min, in_max, out_min, out_max):

    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Application(QMainWindow):

    def __init__(self):

        global window1, window2, window3, window4

        super().__init__()
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)
        self.MainUi.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)


        # Create The Graph Windows
        window1 = self.createGraphs(1)
        window2 = self.createGraphs(2)
        window3 = self.createGraphs(3)
        window4 = self.createGraphs(4)
        
        # Set Up Initial Label Values
        self.setupLabelValues()

        # Set Up and create The Tool Bar
        self.setupToolBar()
    

        # Main Window Widgets connections 
        ### Check Buttons
        self.MainUi.Channel1Check.toggled.connect(self.Channel1Checking)
        self.MainUi.Channel2Check.toggled.connect(self.Channel2Checking)
        self.MainUi.Channel3Check.toggled.connect(self.Channel3Checking)
        self.MainUi.Channel4Check.toggled.connect(self.Channel4Checking)
        ### Buttons
        self.MainUi.ConfSerPowerButton.clicked.connect(self.powerButtonFunc)
        self.MainUi.SaveDataButton.clicked.connect(self.saveDataToTxtFile)
        ### Sliders
        self.MainUi.Channel1VoltsSlider.valueChanged.connect(self.Channel1VoltsSliderCMD)
        self.MainUi.Channel1MsSlider.valueChanged.connect(self.Channel1MsSliderCMD)
        self.MainUi.Channel2VoltsSlider.valueChanged.connect(self.Channel2VoltsSliderCMD)
        self.MainUi.Channel2MsSlider.valueChanged.connect(self.Channel2MsSliderCMD)
        self.MainUi.Channel3VoltsSlider.valueChanged.connect(self.Channel3VoltsSliderCMD)
        self.MainUi.Channel3MsSlider.valueChanged.connect(self.Channel3MsSliderCMD)
        self.MainUi.Channel4VoltsSlider.valueChanged.connect(self.Channel4VoltsSliderCMD)
        self.MainUi.Channel4MsSlider.valueChanged.connect(self.Channel4MsSliderCMD)
        
        
    def createGraphs(self, GraphNumber):

        sub = QMdiSubWindow()
        # sub.setWidget(self.my_plot)
        sub.setWindowTitle("Channel"+str(GraphNumber))
        self.MainUi.MDIWindows.addSubWindow(sub)
        sub.show()

        return sub
    
    def setupToolBar(self):

        tileWindows = QAction(QIcon("Assets\\TileWindows.png"), "tileWindows", self)
        self.MainUi.toolBar.addAction(tileWindows)
        cascadeWindows = QAction(QIcon("Assets\\cascadeWindows.png"), "cascadeWindows", self)
        self.MainUi.toolBar.addAction(cascadeWindows)

    def setupLabelValues(self):

        self.MainUi.Channel1MsLabel.setText("{:.1f} ms/Div".format(_map(self.MainUi.Channel1MsSlider.value(), 35, 74, 0.001, 999)))

    def toolbtnpressed(self, retn):
        retn = retn.text()

        if retn == "tileWindows":
            self.MainUi.MDIWindows.tileSubWindows()
        elif retn == "cascadeWindows":
            self.MainUi.MDIWindows.cascadeSubWindows()
    
    def Channel1Checking(self):

        if self.MainUi.Channel1Check.isChecked() == True: # Enabled...
            window1.show()
        else:
            window1.hide()
    
    def Channel2Checking(self):

        if self.MainUi.Channel2Check.isChecked() == True: # Enabled...
            window2.show()
        else:
            window2.hide()
    
    def Channel3Checking(self):

        if self.MainUi.Channel3Check.isChecked() == True: # Enabled...
            window3.show()
        else:
            window3.hide()
    
    def Channel4Checking(self):

        if self.MainUi.Channel4Check.isChecked() == True: # Enabled...
            window4.show()
        else:
            window4.hide()
            
    def powerButtonFunc(self):

        if self.MainUi.ConfSerPowerButton.isChecked() == True:
            # Enable Serial Read
            self.MainUi.ConfSerPowerButton.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.MainUi.ConfSerPowerButton.setText("Power ON")
        else:
            #disable serial read
            self.MainUi.ConfSerPowerButton.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.MainUi.ConfSerPowerButton.setText("Power OFF")

    def Channel1VoltsSliderCMD(self):
        val = self.MainUi.Channel1VoltsSlider.value()

        if val >= 50:
            valNew = _map(val, 50, 100, 1, 20)
            self.MainUi.Channel1VLabel.setText("{:.1f} V/Div".format(valNew))
            print(val, valNew)
        elif val <= 49:
            valNew = _map(val, 0, 49, 0.01, 0.9)
            valNew *= 1000
            self.MainUi.Channel1VLabel.setText("{:.1f} mV/Div".format(valNew))

    def Channel1MsSliderCMD(self):
        val = self.MainUi.Channel1MsSlider.value()

        if val >= 75:
            valNew = _map(val, 75, 100, 1, 20)
            self.MainUi.Channel1MsLabel.setText("{:.1f} S/Div".format(valNew))
            print(val, valNew)
        elif (val >= 35) and (val <= 74):
            valNew = _map(val, 35, 74, 0.001, 999)
            self.MainUi.Channel1MsLabel.setText("{:.1f} ms/Div".format(valNew))
            print(val, valNew)
        elif val <= 34:
            valNew = _map(val, 0, 34, 20, 999)
            self.MainUi.Channel1MsLabel.setText("{:.1f} us/Div".format(valNew))
            print(val, valNew)

    def Channel2VoltsSliderCMD(self):
        val = self.MainUi.Channel2VoltsSlider.value()

        if val >= 50:
            valNew = _map(val, 50, 100, 1, 20)
            self.MainUi.Channel2VLabel.setText("{:.1f} V/Div".format(valNew))
            print(val, valNew)
        elif val <= 49:
            valNew = _map(val, 0, 49, 0.01, 0.9)
            valNew *= 1000
            self.MainUi.Channel2VLabel.setText("{:.1f} mV/Div".format(valNew))

    def Channel2MsSliderCMD(self):
        val = self.MainUi.Channel2MsSlider.value()

        if val >= 75:
            valNew = _map(val, 75, 100, 1, 20)
            self.MainUi.Channel2MsLabel.setText("{:.1f} S/Div".format(valNew))
            print(val, valNew)
        elif (val >= 35) and (val <= 74):
            valNew = _map(val, 35, 74, 0.001, 999)
            self.MainUi.Channel2MsLabel.setText("{:.1f} ms/Div".format(valNew))
            print(val, valNew)
        elif val <= 34:
            valNew = _map(val, 0, 34, 20, 999)
            self.MainUi.Channel2MsLabel.setText("{:.1f} us/Div".format(valNew))
            print(val, valNew)

    def Channel3VoltsSliderCMD(self):
        val = self.MainUi.Channel3VoltsSlider.value()

        if val >= 50:
            valNew = _map(val, 50, 100, 1, 20)
            self.MainUi.Channel3VLabel.setText("{:.1f} V/Div".format(valNew))
            print(val, valNew)
        elif val <= 49:
            valNew = _map(val, 0, 49, 0.01, 0.9)
            valNew *= 1000
            self.MainUi.Channel3VLabel.setText("{:.1f} mV/Div".format(valNew))

    def Channel3MsSliderCMD(self):
        val = self.MainUi.Channel3MsSlider.value()

        if val >= 75:
            valNew = _map(val, 75, 100, 1, 20)
            self.MainUi.Channel3MsLabel.setText("{:.1f} S/Div".format(valNew))
            print(val, valNew)
        elif (val >= 35) and (val <= 74):
            valNew = _map(val, 35, 74, 0.001, 999)
            self.MainUi.Channel3MsLabel.setText("{:.1f} ms/Div".format(valNew))
            print(val, valNew)
        elif val <= 34:
            valNew = _map(val, 0, 34, 20, 999)
            self.MainUi.Channel3MsLabel.setText("{:.1f} us/Div".format(valNew))
            print(val, valNew)

    def Channel4VoltsSliderCMD(self):
        val = self.MainUi.Channel4VoltsSlider.value()

        if val >= 50:
            valNew = _map(val, 50, 100, 1, 20)
            self.MainUi.Channel4VLabel.setText("{:.1f} V/Div".format(valNew))
            print(val, valNew)
        elif val <= 49:
            valNew = _map(val, 0, 49, 0.01, 0.9)
            valNew *= 1000
            self.MainUi.Channel4VLabel.setText("{:.1f} mV/Div".format(valNew))

    def Channel4MsSliderCMD(self):
        val = self.MainUi.Channel4MsSlider.value()

        if val >= 75:
            valNew = _map(val, 75, 100, 1, 20)
            self.MainUi.Channel4MsLabel.setText("{:.1f} S/Div".format(valNew))
            print(val, valNew)
        elif (val >= 35) and (val <= 74):
            valNew = _map(val, 35, 74, 0.001, 999)
            self.MainUi.Channel4MsLabel.setText("{:.1f} ms/Div".format(valNew))
            print(val, valNew)
        elif val <= 34:
            valNew = _map(val, 0, 34, 20, 999)
            self.MainUi.Channel4MsLabel.setText("{:.1f} us/Div".format(valNew))
            print(val, valNew)

    def saveDataToTxtFile(self):
        saveDatafileType = self.MainUi.SaveDataFileFormatCombo.currentText()

        data = "No Data"
        dataDestination = "SavedData\\Data--{}.{}".format(str(datetime.datetime.today()).replace(" ","--").replace(".", "-").replace(":", "-"), saveDatafileType)
        
        if saveDatafileType == "txt":
            with open(dataDestination, "w") as foTxt:
                foTxt.write(data)
        elif saveDatafileType == "json":
            print("json")
        elif saveDatafileType == "csv":
            print("csv")
        elif saveDatafileType == "xml":
            print("xml")
        














































