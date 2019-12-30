from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from BackEnd import *

if __name__ == "__main__":
    
    w = QApplication([])
    app = Application()
    app.show()
    w.exec_()