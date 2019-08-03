from PyQt4.QtGui import *
from MainWindowFrontEnd import *

import pyqtgraph as pg
import random

def _map(value, fromLow, fromHigh, toLow, toHigh):

    fromDif = (fromHigh - fromLow)
    toDof = (toHigh - toLow)

    toValue = (value * toDof) / fromDif
    
    return toValue

print(_map(10, 0, 5, 0, 360))


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
        
        # Set Up and create The Tool Bar
        self.setupToolBar()
    

        # Main Window Widgets connections     self.MainUi.
        self.MainUi.Channel1Check.toggled.connect(self.Channel1Checking)
        self.MainUi.Channel2Check.toggled.connect(self.Channel2Checking)
        self.MainUi.Channel3Check.toggled.connect(self.Channel3Checking)
        self.MainUi.Channel4Check.toggled.connect(self.Channel4Checking)
        self.MainUi.ConfSerPowerButton.clicked.connect(self.powerButtonFunc)
        self.MainUi.Channel1VoltsSlider.valueChanged.connect(self.Channel1VoltsSliderCMD)
        self.MainUi.Channel1MsSlider.valueChanged.connect(self.Channel1MsSliderCMD)
        
        
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

        self.MainUi.Channel1VLabel.setText("{} V/Div".format(val))
        print(val, _map(val, 0, 100, 0.01, 20))

    def Channel1MsSliderCMD(self):
        val = self.MainUi.Channel1MsSlider.value()

        self.MainUi.Channel1MsLabel.setText("{} ms/Div".format(val))
        print(val)












































