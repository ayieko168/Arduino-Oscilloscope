import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import math
from time import sleep

f = 10
t = 0
Samples = 1000


# while True:

#     y2 = np.sin( 2* np.pi * f * t)
#     print(y)
#     t+=0.01
#     sleep(0.25)

def update():
    global f, t, ys, y2

    print(len(y2))
    if len(y2) == Samples:
        y2.pop(y2.index(y2[0]))

    y2.append(np.sin( 2 * np.pi * f * t))
    
    t += 0.0001
    c2.updateData(y2)


# define the data
theTitle = "pyqtgraph plot"
y2 = []

# create plot
plt = pg.plot()
plt.showGrid(x=True,y=True)
dat2 = []
c2 = pg.PlotCurveItem(dat2)
plt.addItem(c2)

timer = pg.QtCore.QTimer ()
timer.timeout.connect(update)
timer.start(0.1)

## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()