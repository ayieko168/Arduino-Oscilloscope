from PyQt4.QtGui import *
from PyQt4 import QtCore
from MainWindowFrontEnd import *
from Graph2D import Plot2D

import numpy as np
from numpy import arange, sin, cos, pi

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

        def update():

            y = np.random.randint(1,10,(1,20))[0]
            x = [x for x in range(20)]
            k.plot(x,y)

            y1 = np.random.randint(1,10,(1,20))[0]
            x1 = [x for x in range(20)]
            kk.plot(x1,y1)

            y2 = np.random.randint(1,10,(1,20))[0]
            x2 = [x for x in range(20)]
            kkk.plot(x2,y2)

            y3 = np.random.randint(1,10,(1,20))[0]
            x3 = [x for x in range(20)]
            kkkk.plot(x3,y3)

        a = Plot2D()
        k = a.create(window1)
        a1 = Plot2D()
        kk = a1.create(window2)
        a2 = Plot2D()
        kkk = a2.create(window3)
        a3 = Plot2D()
        kkkk = a3.create(window4)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(update)
        self.timer.start(10)
        

        
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
        self.MainUi.SamplingControlOnceButton.clicked.connect(self.SamplingControlOnceButtonCMD)
        self.MainUi.SamplingControlFlowButton.clicked.connect(self.SamplingControlFlowButtonCMD)
        self.MainUi.SamplingControlVariousButton.clicked.connect(self.SamplingControlVariousButtonCMD)
        ### Sliders
        self.MainUi.Channel1VoltsSlider.valueChanged.connect(self.Channel1VoltsSliderCMD)
        self.MainUi.Channel1MsSlider.valueChanged.connect(self.Channel1MsSliderCMD)
        self.MainUi.Channel2VoltsSlider.valueChanged.connect(self.Channel2VoltsSliderCMD)
        self.MainUi.Channel2MsSlider.valueChanged.connect(self.Channel2MsSliderCMD)
        self.MainUi.Channel3VoltsSlider.valueChanged.connect(self.Channel3VoltsSliderCMD)
        self.MainUi.Channel3MsSlider.valueChanged.connect(self.Channel3MsSliderCMD)
        self.MainUi.Channel4VoltsSlider.valueChanged.connect(self.Channel4VoltsSliderCMD)
        self.MainUi.Channel4MsSlider.valueChanged.connect(self.Channel4MsSliderCMD)
        self.MainUi.SigGenFreqSlider.valueChanged.connect(self.SigGenFreqSliderCMD)
        self.MainUi.SigGenPeriodSlider.valueChanged.connect(self.SigGenPeriodSliderCMD)
        self.MainUi.SigGenDutyslider.valueChanged.connect(self.SigGenDutysliderCMD)
        
    def createGraphs(self, GraphNumber):

        sub = QMdiSubWindow()
        # sub.setWidget(self.my_plot)
        sub.setWindowTitle("Channel"+str(GraphNumber))
        self.MainUi.MDIWindows.addSubWindow(sub)

        return sub
    
    def setupToolBar(self):

        tileWindows = QAction(QIcon("Assets\\TileWindows.png"), "tileWindows", self)
        self.MainUi.toolBar.addAction(tileWindows)
        cascadeWindows = QAction(QIcon("Assets\\cascadeWindows.png"), "cascadeWindows", self)
        self.MainUi.toolBar.addAction(cascadeWindows)
        horizontalTile = QAction(QIcon("Assets\\horizontalTile.jpg"), "horizontalTile", self)
        self.MainUi.toolBar.addAction(horizontalTile)
        self.MainUi.toolBar.addSeparator()
        
    def setupLabelValues(self):

        self.MainUi.Channel1MsLabel.setText("{:.1f} ms/Div".format(_map(self.MainUi.Channel1MsSlider.value(), 35, 74, 0.001, 999)))

    def toolbtnpressed(self, retn):
        retn = retn.text()

        if retn == "tileWindows":
            self.MainUi.MDIWindows.tileSubWindows()

        elif retn == "cascadeWindows":
            self.MainUi.MDIWindows.cascadeSubWindows()

        elif retn == "horizontalTile":
            self.MainUi.MDIWindows.tileSubWindows()

            window1.setGeometry(0, 0, 806, 142)
            window2.setGeometry(0, 142, 806, 142)
            window3.setGeometry(0, 284, 806, 142)
            window4.setGeometry(0, 426, 806, 142)
    
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
            # change Power Button Look to On
            self.MainUi.ConfSerPowerButton.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.MainUi.ConfSerPowerButton.setText("Power ON")
            
            # Set default values system Wide
            self.MainUi.SamplingControlOnceButton.setChecked(False)
            self.MainUi.SamplingControlFlowButton.setChecked(False)
            self.MainUi.SamplingControlVariousButton.setChecked(True) #Set Various To default

        else:
            # change Power Button Look To Off
            self.MainUi.ConfSerPowerButton.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.MainUi.ConfSerPowerButton.setText("Power OFF")
            
            # Swith Off every Default Set Buttons
            self.MainUi.SamplingControlOnceButton.setChecked(False)
            self.MainUi.SamplingControlFlowButton.setChecked(False)
            self.MainUi.SamplingControlVariousButton.setChecked(False)
            
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
            ### Convert data to numbered data before writing

            with open(dataDestination, "w") as foTxt:
                foTxt.write(data)
        elif saveDatafileType == "json":
            ### Convert data to dictionary before writing

            with open(dataDestination, "w") as foJson:
                json.dump(data, foJson, indent=2)
            print("json")
        elif saveDatafileType == "csv":
            ### Convert data to comma separated values before writing

            with open(dataDestination, "w") as foCsv:
                foCsv.write(data)
            print("csv")
        elif saveDatafileType == "xml":
            ### Convert data to xml firmat before writing

            with open(dataDestination, "w") as foXml:
                foXml.write(data)
            print("xml")
        
    def SamplingControlOnceButtonCMD(self):
        print("once")

        if self.MainUi.SamplingControlOnceButton.isChecked() == True:  # if once button is set..
            # frist disable other buttons
            self.MainUi.SamplingControlFlowButton.setChecked(False)
            self.MainUi.SamplingControlVariousButton.setChecked(False)
        
        if (self.MainUi.SamplingControlOnceButton.isChecked() == False) and\
            (self.MainUi.SamplingControlFlowButton.isChecked() == False) and\
            (self.MainUi.SamplingControlVariousButton.isChecked() == False) and\
            (self.MainUi.ConfSerPowerButton.isChecked() == True):
            ### If all buttons are off and power is on, set default mode to various

            self.MainUi.SamplingControlVariousButton.setChecked(True)
            print("complex")
 
    def SamplingControlFlowButtonCMD(self):
        print("flow")

        if self.MainUi.SamplingControlFlowButton.isChecked() == True:  # if flow button is set..
            # frist disable other buttons
            self.MainUi.SamplingControlOnceButton.setChecked(False)
            self.MainUi.SamplingControlVariousButton.setChecked(False)
        
        if (self.MainUi.SamplingControlOnceButton.isChecked() == False) and\
            (self.MainUi.SamplingControlFlowButton.isChecked() == False) and\
            (self.MainUi.SamplingControlVariousButton.isChecked() == False) and\
            (self.MainUi.ConfSerPowerButton.isChecked() == True):
            ### If all buttons are off and power is on, set default mode to various

            self.MainUi.SamplingControlVariousButton.setChecked(True)
            print("complex")
    
    def SamplingControlVariousButtonCMD(self):
        print("various")

        if self.MainUi.SamplingControlVariousButton.isChecked() == True:  # if flow button is set..
            # frist disable other buttons
            self.MainUi.SamplingControlOnceButton.setChecked(False)
            self.MainUi.SamplingControlFlowButton.setChecked(False)
        
        if (self.MainUi.SamplingControlOnceButton.isChecked() == False) and\
            (self.MainUi.SamplingControlFlowButton.isChecked() == False) and\
            (self.MainUi.SamplingControlVariousButton.isChecked() == False) and\
            (self.MainUi.ConfSerPowerButton.isChecked() == True):
            ### If all buttons are off and power is on, set default mode to various

            self.MainUi.SamplingControlVariousButton.setChecked(True)
            print("complex")

    def SigGenFreqSliderCMD(self):
        val = self.MainUi.SigGenFreqSlider.value()
        # Resultant value in miliHearts
        
        per = 1 / val
        self.MainUi.SigGenPeriodSlider.setValue(per)
        print(val)
        
    def SigGenPeriodSliderCMD(self):
        val = self.MainUi.SigGenPeriodSlider.value()
        # Resultant value in miliHearts
        if val > 1e6:
            val = val / 1e6
            print("{:.1f} S".format(val))

        elif (val <= 1e6) and (val >= 1e3):
            val = val / 1e3
            print("{:.1f} mS".format(val))

        elif val < 1e3:
            print("{:.1f} uS".format(val))
        
    def SigGenDutysliderCMD(self):
        val = self.MainUi.SigGenDutyslider.value()

        self.MainUi.SigGenDutyLabel.setText("Duty {:.1f}%".format(val))
        print(val)
        
















if __name__ == "__main__":
    
    w = QApplication([])
    app = Application()
    app.show()
    w.exec_()





















