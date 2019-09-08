# Main Imports
from PyQt4.QtGui import *
from PyQt4 import QtCore
from MainWindowFrontEnd import *
from GraphUpdadeFunctions import Functions

# System operation Imports
import os
import datetime

# Graph Imports
import pyqtgraph as pg
import numpy as np
from numpy import arange, sin, cos, pi

# Other Imports
import csv, json, xml
import random

def _map(value, in_min, in_max, out_min, out_max):

    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Application(QMainWindow):

    def __init__(self):

        super().__init__()
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)
        self.MainUi.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

        # Initialize Graphs
        self.InitializeGraphs()

        # Set Up Initial Label Values
        self.setupLabelValues()

        # Set Up and create The Tool Bar
        self.setupToolBar()

        # MenuBar Connections
        #### Demo Connections
        self.MainUi.actionDemo1.toggled.connect(self.actionDemo1CMD)
        self.MainUi.actionDemo2.toggled.connect(self.actionDemo2CMD)
        self.MainUi.actionDemo3.toggled.connect(self.actionDemo3CMD)

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
            self.MainUi.Channel1GraphicsView.setGeometry(0, 0, 407, 295)
            self.MainUi.Channel2GraphicsView.setGeometry(407, 0, 407, 295)
            self.MainUi.Channel3GraphicsView.setGeometry(0, 295, 407, 295)
            self.MainUi.Channel4GraphicsView.setGeometry(407, 295, 407, 295)

        elif retn == "cascadeWindows":
            pass

        elif retn == "horizontalTile":
            self.MainUi.Channel1GraphicsView.setGeometry(0, 0, 814, 147)
            self.MainUi.Channel2GraphicsView.setGeometry(0, 147, 814, 147)
            self.MainUi.Channel3GraphicsView.setGeometry(0, 294, 814, 147)
            self.MainUi.Channel4GraphicsView.setGeometry(0, 441, 814, 147)
    
    def InitializeGraphs(self):

        global c1, c2, c3, c4, data1, data2, data3, data4, Funcs
        
        
        # Set Graph Looks
        ### Graph 1 Looks
        self.MainUi.Channel1GraphicsView.plotItem.showGrid(True, True)
        self.MainUi.Channel1GraphicsView.plotItem.hideAxis("bottom")
        ### Graph 2 Looks
        self.MainUi.Channel2GraphicsView.plotItem.showGrid(True, True)
        self.MainUi.Channel2GraphicsView.plotItem.hideAxis("bottom")
        ### Graph 3 Looks
        self.MainUi.Channel3GraphicsView.plotItem.showGrid(True, True)
        self.MainUi.Channel3GraphicsView.plotItem.hideAxis("bottom")
        ### Graph 4 Looks
        self.MainUi.Channel4GraphicsView.plotItem.showGrid(True, True)
        self.MainUi.Channel4GraphicsView.plotItem.hideAxis("bottom")

        # Initialize Graph Data
        ### Graph 1 Data
        data1 = np.array([1,4,5,3,np.inf,5,7,6,-np.inf,8,10,9,np.nan,-1,-2,0])
        c1 = pg.PlotCurveItem(data1)
        ### Graph 2 Data
        data2 = np.array([1,4,5,3,np.inf,5,7,6,-np.inf,8,10,9,np.nan,-1,-2,0])
        c2 = pg.PlotCurveItem(data2)
        
        ### Graph 3 Data
        data3 = np.array([1,4,5,3,np.inf,5,7,6,-np.inf,8,10,9,np.nan,-1,-2,0])
        c3 = pg.PlotCurveItem()
        c3.setData(data3, symbol="o")
        ### Graph 4 Data
        data4 = []
        c4 = pg.PlotCurveItem(data4)

        # Initial Plot
        ### Add Data To Graph 1
        self.MainUi.Channel1GraphicsView.addItem(c1)
        ### Add Data To Graph 2
        self.MainUi.Channel2GraphicsView.addItem(c2)
        ### Add Data To Graph 3
        self.MainUi.Channel3GraphicsView.addItem(c3)
        ### Add Data To Graph 4
        self.MainUi.Channel4GraphicsView.addItem(c4)

        Funcs = Functions(c1, c2, c3, c4, data1, data2, data3, data4, 10, 0)

        self.timer = pg.QtCore.QTimer ()
        self.timer.timeout.connect(self.GrapgUpdate)
        self.timer.start(2000)

    def GrapgUpdate(self):
        """Callback Function for the Initialize Graphs method"""

        global c1, c2, c3, c4, data2

        print("update")
        # data2.append([x for x in range])
        c2.updateData(data2)
        self.MainUi.Channel2GraphicsView.addItem(c2)

    def actionDemo1CMD(self):
        global c1, c2, c3, c4, data1, data2, data3, data4, fr, t

        fr = 10
        t = 0
        
        """Call Back For Demo1 MenuBar Option"""
        if self.MainUi.actionDemo1.isChecked() == True:  # if Demo 1 is set..
            # frist disable other buttons
            self.MainUi.actionDemo2.setChecked(False)
            self.MainUi.actionDemo3.setChecked(False)
            # Then Other Stuff

            
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.actionDemoGraphUpdateMethod)
            self.timer.start(2)
    
    def actionDemoGraphUpdateMethod(self):

        if len(self.data4) == 1000:
            self.data4.pop(self.data4.index(self.data4[0]))

        self.data4.append(np.sin( 2 * np.pi * fr * t))
        
        t += 0.0001
        self.c4.updateData(self.data4)

        print("udem")

    def actionDemo2CMD(self):
        """Call Back For Demo2 MenuBar Option"""
        if self.MainUi.actionDemo2.isChecked() == True:  # if Demo 2 is set..
            # frist disable other buttons
            self.MainUi.actionDemo1.setChecked(False)
            self.MainUi.actionDemo3.setChecked(False)
            # Then Other Stuff
            #

    def actionDemo3CMD(self):
        """Call Back For Demo3 MenuBar Option"""
        if self.MainUi.actionDemo3.isChecked() == True:  # if Demo 3 is set..
            # frist disable other buttons
            self.MainUi.actionDemo2.setChecked(False)
            self.MainUi.actionDemo1.setChecked(False)
            # Then Other Stuff
            #

    def Channel1Checking(self):

        if self.MainUi.Channel1Check.isChecked() == True: # Enabled...
            self.MainUi.Channel2GraphicsView.plotItem.show()
        else:
            self.MainUi.Channel2GraphicsView.plotItem.hide()
    
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





















