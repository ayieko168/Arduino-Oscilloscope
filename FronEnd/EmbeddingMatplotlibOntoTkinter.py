import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter import *
from tkinter import ttk

from createPlot import Graph
import random

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        # Tk.iconbitmap(self, default=)
        Tk.wm_title(self, "Sea of BTC client")

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree):

            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        label = Label(text="Start page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="VisitPage 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = ttk.Button(self, text="VisitPage 2",
                            command= lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="VisitPage 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "PageOne!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()

class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "PageTwo!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        button1 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageThree(Frame):

    

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text = "Graph Page!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="Back Home",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        x = []
        y = []

        for i in range(1, 20+1):
            x.append(i)
            y.append(random.randint(1, 10))
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

        toolbar= NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

app = SeaofBTCapp()
app.mainloop()
