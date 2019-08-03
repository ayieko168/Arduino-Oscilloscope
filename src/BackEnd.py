from PyQt4.QtGui import *
from MainWindowFrontEnd import *
from test import *

class Application(QMainWindow):

    def __init__(self):

        super().__init__()
        self.MainUi = Ui_MainWindow()
        self.MainUi.setupUi(self)
        self.MainUi.toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

        # Create The Graph Windows
        for i in range(1,5):
            self.createGraphs(i)
        
        # Set Up and create The Tool Bar
        self.setupToolBar()
    

        # Main Window Widgets connections
        
    def createGraphs(self, GraphNumber):

        global sub

        window = GraphWindow()

        sub = QMdiSubWindow()
        sub.setWidget(window)
        sub.setWindowTitle("Channel"+str(GraphNumber))
        self.MainUi.MDIWindows.addSubWindow(sub)
        sub.show()

        print(sub)
    
    def setupToolBar(self):

        tileWindows = QAction(QIcon("Assets\\TileWindows.png"), "tileWindows", self)
        self.MainUi.toolBar.addAction(tileWindows)
        cascadeWindows = QAction(QIcon("Assets\\cascadeWindows.png"), "cascadeWindows", self)
        self.MainUi.toolBar.addAction(cascadeWindows)
    
    def toolbtnpressed(self, retn):
        retn = retn.text()

        if retn == "tileWindows":
            self.MainUi.MDIWindows.tileSubWindows()
            print(sub.children()[2].title())
        elif retn == "cascadeWindows":
            self.MainUi.MDIWindows.cascadeSubWindows()
            print(sub.children())
            