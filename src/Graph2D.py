import pyqtgraph as pg
import numpy as np
from numpy import arange, sin, cos, pi
from PyQt4 import QtCore

class Plot2D:

    def __init__(self):
        pass
        
    def create(self, parent):

        global my_plot

        my_plot = pg.PlotWidget()
        parent.setWidget(my_plot)
        my_plot.plot([1,3,5,7,9], [7,9,3,1,6])

        parent.show()

        return my_plot
