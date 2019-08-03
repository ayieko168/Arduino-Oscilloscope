from PyQt4.QtGui import *
from BackEnd import *

if __name__ == "__main__":
    
    w = QApplication([])
    app = Application()
    app.show()
    w.exec_()