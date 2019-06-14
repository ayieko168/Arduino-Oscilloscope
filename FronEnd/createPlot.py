import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter import *
from tkinter import ttk

import random

class Graph:
    
    def plot(self, parent=None, subplotArgs=111, figureSize=(5,5), DPI=100, xs=[1], ys=[2], toolBar=True, toolParent=None):

        self.parent = parent
        self.subplotArgs = subplotArgs
        self.figureSize = figureSize
        self.dpi = DPI
        self.xs = xs
        self.ys = ys

        f = Figure(figsize=figureSize, dpi=DPI)
        a = f.add_subplot(subplotArgs)
        x = xs
        y = ys

        # for i in range(1, 20+1):
        #     x.append(i)
        #     y.append(random.randint(1, 10))
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        if toolBar:
            toolbar= NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        else:
            pass
        
        return self
        