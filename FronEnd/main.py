from tkinter import *
# from createPlot import Graph
# from tkinter import ttk
from math import *

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation

from createPlot import GraphCanvas

import random

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


SIZE = "1000x800+50+50"  # size string: WxH+X+Y
MENUFONT = ('Comic Sans MS', '9', 'normal', 'roman')

f0 = Figure(figsize=(5,1.35), dpi=100)
a0 = f0.add_subplot(111)
f0.subplots_adjust(left=0, right=1, top=1, bottom=0)
a0.axis('off')

f1 = Figure(figsize=(5,1.35), dpi=100)
f1.subplots_adjust(left=0, right=1, top=1, bottom=0)
a1 = f1.add_subplot(111)
a1.axis('off')

f2 = Figure(figsize=(5,1.35), dpi=100)
f2.subplots_adjust(left=0, right=1, top=1, bottom=0)
a2 = f2.add_subplot(111)
a2.axis('off')

f3 = Figure(figsize=(5,1.35), dpi=100)
f3.subplots_adjust(left=0, right=1, top=1, bottom=0)
a3 = f3.add_subplot(111)
a3.axis('off')

def animateGraph0(i):
    # global line, xVal
    # print("animate")
    # a0.clear()
    # line.set_ydata(np.sin(xVal + i / 10))  # update the data.
    # return line,

    # graph_data = open('example.txt','r').read()
    # lines = graph_data.split('\n')
    # xs = []
    # ys = []
    # for line in lines:
    #     if len(line) > 1:
    #         x, y = line.split(',')
    #         xs.append(float(x))
    #         ys.append(float(y))
    # a0.clear()
    # a0.plot(xs, ys)

    xar = []
    yar = []

    a0.set_ylim(0, 100)
    line, = a0.plot(xar, yar, 'r', marker='o')
    
    #ser.reset_input_buffer()
    #data = ser.readline().decode("utf-8")
    #data_array = data.split(',')
    #yvalue = float(data_array[1])
    yar.append(99-i)
    xar.append(i)
    line.set_data(xar, yar)
    a0.set_xlim(0, i+1)

    return

def animateGraph1(i):
    # global line, xVal
    # print("animate")
    # a0.clear()
    # line.set_ydata(np.sin(xVal + i / 10))  # update the data.
    # return line,

    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    a1.clear()
    a1.plot(xs, ys)

    return

def animateGraph2(i):
    # global line, xVal
    # print("animate")
    # a0.clear()
    # line.set_ydata(np.sin(xVal + i / 10))  # update the data.
    # return line,

    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    a2.clear()
    a2.plot(xs, ys)

    return

def animateGraph3(i):
    # global line, xVal
    # print("animate")
    # a0.clear()
    # line.set_ydata(np.sin(xVal + i / 10))  # update the data.
    # return line,

    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    a3.clear()
    a3.plot(xs, ys)

    return


def createGraph0(parent):

    # global line, xVal, a0

    print("create 0")

    fm0 = Frame(parent, bg="red")
    fm0.grid_rowconfigure(0, weight=1)
    fm0.grid_columnconfigure(0, weight=1)

    canvas = FigureCanvasTkAgg(f0, fm0)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    # toolbar = NavigationToolbar2Tk(canvas, fm0)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    return fm0

def createGraph1(parent):

    print("create 1")

    fm1 = Frame(parent, bg="green")
    fm1.grid_rowconfigure(0, weight=1)
    fm1.grid_columnconfigure(0, weight=1)

    canvas = FigureCanvasTkAgg(f1, fm1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    # toolbar = NavigationToolbar2Tk(canvas, fm0)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    return fm1

def createGraph2(parent):

    print("create 0")

    fm2 = Frame(parent, bg="blue")
    fm2.grid_rowconfigure(0, weight=1)
    fm2.grid_columnconfigure(0, weight=1)

    canvas = FigureCanvasTkAgg(f2, fm2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    # toolbar = NavigationToolbar2Tk(canvas, fm0)
    # toolbar.update()
    # canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    return fm2

def createGraph3(parent):

    print("create 3")

    fm3 = Frame(parent, bg="yellow")
    fm3.grid_rowconfigure(0, weight=1)
    fm3.grid_columnconfigure(0, weight=1)

    canvas = FigureCanvasTkAgg(f3, fm3)
    canvas.draw()
    canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

    toolbar = NavigationToolbar2Tk(canvas, fm3)
    toolbar.update()
    canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)

    return fm3

def createGraphsHolder(parent):
    """create a holder for the Actual Graphs"""
    # Make graph variables Global
    global paneGraphs, graph1, graph0, graph2, graph3, lineMarker

    graphsFrame = LabelFrame(parent, text="graphs", width=780, height=50, bg="indigo")
    graphsFrame.grid_rowconfigure(0, weight=1)
    graphsFrame.grid_columnconfigure(0, weight=1)

    paneGraphs = PanedWindow(graphsFrame, orient=VERTICAL, sashwidth=5, sashrelief=SOLID, bg='#ddd')

    # graph3 = g.createGraph(paneGraphs, texT="graph3", bG="yellow", figsizE=(5,1.35), lineColor="yellow")
    # Create Graph Instances
    graph0 = createGraph0(paneGraphs)
    graph1 = createGraph1(paneGraphs)
    graph2 = createGraph2(paneGraphs)
    graph3 = createGraph3(paneGraphs)

    paneGraphs.add(graph0, minsize=50)
    paneGraphs.add(graph1, minsize=50)
    paneGraphs.add(graph2, minsize=50)
    paneGraphs.add(graph3, minsize=50)
    
    paneGraphs.grid(row=0, sticky='news')
    graphsFrame.config(height=640, padx=5, pady=5) #important for maintainance of height of the graphs frame container
    return graphsFrame

def createChanelsHolder(parent):
    """create a holder for the Chanel Controls"""

    global ch0FrameVar, ch0TrigCheckVar, ch0MeasureCheckVar, ch0CurveCheckVar, ch0V_DivSclVar,\
            ch1FrameVar, ch1TrigCheckVar, ch1MeasureCheckVar, ch1CurveCheckVar, ch1V_DivSclVar,\
            ch2FrameVar, ch2TrigCheckVar, ch2MeasureCheckVar, ch2CurveCheckVar, ch2V_DivSclVar,\
            ch3FrameVar, ch3TrigCheckVar, ch3MeasureCheckVar, ch3CurveCheckVar, ch3V_DivSclVar

    ###### Chanel Selection CallBacks #####################
    def ch0FrameCmd():
        val = ch0FrameVar.get()
        print("ch0", val)
        if val == 0:
            paneGraphs.forget(graph0)
        else:
            paneGraphs.add(graph0, before=graph1)
    
    def ch1FrameCmd():
        val = ch1FrameVar.get()
        print("ch1", val)
        if val == 0:
            paneGraphs.forget(graph1)
        else:
            paneGraphs.add(graph1, before=graph2)
    
    def ch2FrameCmd():
        val = ch2FrameVar.get()
        print("ch2", val)
        if val == 0:
            paneGraphs.forget(graph2)
        else:
            paneGraphs.add(graph2, before=graph3)
    
    def ch3FrameCmd():
        val = ch3FrameVar.get()
        print("ch3", val)
        if val == 0:
            paneGraphs.forget(graph3)
        else:
            paneGraphs.add(graph3, after=graph2)
    
    #######################################################


    ###### Chanel Controls Call Backs ######################
    def ch0V_DivSclCmd(val):

         print("ch0", val)
         ch0V_DivSclValLabel.config(text="{} V/Div".format(val))

    def ch0Ms_DivSclCmd(val):

        print("ch0", val)
        ch0Ms_DivSclLabel.config(text="{} ms/Div".format(val))
    
    def ch1V_DivSclCmd(val):

         print("ch1", val)
         ch1V_DivSclValLabel.config(text="{} V/Div".format(val))

    def ch1Ms_DivSclCmd(val):

        print("ch1", val)
        ch1Ms_DivSclLabel.config(text="{} ms/Div".format(val))
    
    def ch2V_DivSclCmd(val):

         print("ch2", val)
         ch2V_DivSclValLabel.config(text="{} V/Div".format(val))

    def ch2Ms_DivSclCmd(val):

        print("ch2", val)
        ch2Ms_DivSclLabel.config(text="{} ms/Div".format(val))
    
    def ch3V_DivSclCmd(val):

         print("ch3", val)
         ch3V_DivSclValLabel.config(text="{} V/Div".format(val))

    def ch3Ms_DivSclCmd(val):

        print("ch3", val)
        ch0Ms_DivSclLabel.config(text="{} ms/Div".format(val))
    ####################################################

    chCntrlFrame = LabelFrame(parent, text="chanels")

    # create a holder for Chanel 0 Controls
    ch0Frame = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch0", background='red', font=12,
                                                                variable=ch0FrameVar, command=ch0FrameCmd),
                            width=100, height=150, bg="red")
    
    fm1 = Frame(ch0Frame)
    ch0V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch0V_DivSclCmd, variable=ch0V_DivSclVar)
    ch0V_DivScl.pack(side=LEFT)
    ch0V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch0V_DivSclVar.get()))
    ch0V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(ch0Frame)
    ch0Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch0Ms_DivSclCmd)
    ch0Ms_DivScl.pack(side=LEFT)
    ch0Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch0V_DivSclVar.get()))
    ch0Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch0MeasureCheck = Checkbutton(ch0Frame, text="Measure", indicatoron=0, variable=ch0MeasureCheckVar, command=lambda: print(ch0MeasureCheckVar.get()))
    ch0MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch0CurveCheck = Checkbutton(ch0Frame, text="Curve", indicatoron=0, variable=ch0CurveCheckVar, command=lambda: print(ch0CurveCheckVar.get()))
    ch0CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch0TrigCheck = Checkbutton(ch0Frame, text="Triger", indicatoron=0, variable=ch0TrigCheckVar, command=lambda: print(ch0TrigCheckVar.get()))
    ch0TrigCheck.pack(side=LEFT, padx=2, pady=5)

    ch0Frame.pack(pady=5, padx=5)

    # create a holder for Chanel 1 Controls
    ch1Frame = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch1", font=12, bg="green", variable=ch1FrameVar,
                                                                command=ch1FrameCmd),
                            width=100, height=150, bg="green")

    fm1 = Frame(ch1Frame)
    ch1V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch1V_DivSclCmd, variable=ch1V_DivSclVar)
    ch1V_DivScl.pack(side=LEFT)
    ch1V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch1V_DivSclVar.get()))
    ch1V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(ch1Frame)
    ch1Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch1Ms_DivSclCmd)
    ch1Ms_DivScl.pack(side=LEFT)
    ch1Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch1V_DivSclVar.get()))
    ch1Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch1MeasureCheck = Checkbutton(ch1Frame, text="Measure", indicatoron=0, variable=ch1MeasureCheckVar, command=lambda: print(ch1MeasureCheckVar.get()))
    ch1MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch1CurveCheck = Checkbutton(ch1Frame, text="Curve", indicatoron=0, variable=ch1CurveCheckVar, command=lambda: print(ch1CurveCheckVar.get()))
    ch1CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch1TrigCheck = Checkbutton(ch1Frame, text="Triger", indicatoron=0, variable=ch1TrigCheckVar, command=lambda: print(ch1TrigCheckVar.get()))
    ch1TrigCheck.pack(side=LEFT, padx=2, pady=5)

    ch1Frame.pack(pady=5, padx=5)

    # create a holder for Chanel 2 Controls
    ch2Frame = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch2", font=12, bg="blue", variable=ch2FrameVar,
                                                                command=ch2FrameCmd),
                            width=100, height=150, bg="blue")
    
    fm1 = Frame(ch2Frame)
    ch2V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch2V_DivSclCmd, variable=ch2V_DivSclVar)
    ch2V_DivScl.pack(side=LEFT)
    ch2V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch2V_DivSclVar.get()))
    ch2V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(ch2Frame)
    ch2Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch2Ms_DivSclCmd)
    ch2Ms_DivScl.pack(side=LEFT)
    ch2Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch2V_DivSclVar.get()))
    ch2Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch2MeasureCheck = Checkbutton(ch2Frame, text="Measure", indicatoron=0, variable=ch2MeasureCheckVar, command=lambda: print(ch2MeasureCheckVar.get()))
    ch2MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch2CurveCheck = Checkbutton(ch2Frame, text="Curve", indicatoron=0, variable=ch2CurveCheckVar, command=lambda: print(ch2CurveCheckVar.get()))
    ch2CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch2TrigCheck = Checkbutton(ch2Frame, text="Triger", indicatoron=0, variable=ch2TrigCheckVar, command=lambda: print(ch2TrigCheckVar.get()))
    ch2TrigCheck.pack(side=LEFT, padx=2, pady=5)
    
    ch2Frame.pack(pady=5, padx=5)

    # create a holder for Chanel 3 Controls
    ch3Frame = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch3", font=12, bg="yellow", variable=ch3FrameVar,
                                                                command=ch3FrameCmd),
                            width=100, height=150, bg="yellow")
    
    fm1 = Frame(ch3Frame)
    ch3V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch3V_DivSclCmd, variable=ch3V_DivSclVar)
    ch3V_DivScl.pack(side=LEFT)
    ch3V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch3V_DivSclVar.get()))
    ch3V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(ch3Frame)
    ch3Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch3Ms_DivSclCmd)
    ch3Ms_DivScl.pack(side=LEFT)
    ch3Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch3V_DivSclVar.get()))
    ch3Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch3MeasureCheck = Checkbutton(ch3Frame, text="Measure", indicatoron=0, variable=ch3MeasureCheckVar, command=lambda: print(ch3MeasureCheckVar.get()))
    ch3MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch3CurveCheck = Checkbutton(ch3Frame, text="Curve", indicatoron=0, variable=ch3CurveCheckVar, command=lambda: print(ch3CurveCheckVar.get()))
    ch3CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch3TrigCheck = Checkbutton(ch3Frame, text="Triger", indicatoron=0, variable=ch3TrigCheckVar, command=lambda: print(ch3TrigCheckVar.get()))
    ch3TrigCheck.pack(side=LEFT, padx=2, pady=5)

    ch3Frame.pack(pady=5, padx=5)
    
    chCntrlFrame.config(height=640) #important for maintainance of height
    return chCntrlFrame
       
def createMenuBar(parent):

    menubar = Menu(parent, font=MENUFONT)

    fileMenu = Menu(tearoff=0, font=MENUFONT)
    fileMenu.add_command(label="Exit")

    menubar.add_cascade(label="File", menu=fileMenu)

    return menubar

def makeGraphandChanelsFrame(parent):
    """Create a frame holder for the Graphs And The Chanel Controls"""

    mainFrameChanels = LabelFrame(parent, bg="pink", height=640, padx=5, pady=5)
    mainFrameChanels.grid_rowconfigure(0, weight=1)
    mainFrameChanels.grid_columnconfigure(0, weight=1)

    # fcnsObj = Functions()
 
    paneGphCh = PanedWindow(mainFrameChanels, orient=HORIZONTAL, sashwidth=4, sashrelief=SOLID, bg='#60c0ff')
    paneGphCh.add(createGraphsHolder(paneGphCh), minsize=780)
    paneGphCh.add(createChanelsHolder(paneGphCh), minsize=100)
    paneGphCh.grid(row=0, sticky='news')

    return mainFrameChanels

class XYZ_PlotTopLevel():
    """create a top level widget to plot the XYZ graph on"""

    def create(self):

        global xyzTopLevel

        print("XYZ PLOTING TOP LEVEL")

        xyzTopLevel = Toplevel(root)
        xyzTopLevel.geometry("500x500+100+100")
        xyzTopLevel.title("Arduino Oscilloscope - XYZ PLOT")
        # xyzTopLevel.iconbitmap(default="Assets\youtube-dl-gui.bmp", )
        xyzTopLevel.grid_rowconfigure(0, weight=1)
        xyzTopLevel.grid_columnconfigure(0, weight=1)

        x, y = root.winfo_screenheight(), root.winfo_screenwidth()

        kwargs = {
            "texT": "XYZ Frame",
            "figsizE": ((x/100), (y/100)), 
        }

        xyzTopLevel.overrideredirect()
        return xyzTopLevel
    
    def _destroy(self):

        xyzTopLevel.destroy()

def makeControls_Options_FileIOFrame(parent):
    """create a holder for the Meter, Sampling controls, Data save, Signal generator"""

    global ani0
    # Signal Gen Vars
    global sgnlFrameVar, sgnlFreqScaleVar, sgnlPeriodScaleVar, sgnlt_onScaleVar
    # Sampling Vars
    global smplDtScaleVar, smplQScaleVar, sgnlRealLableVar, sgnlTotalLableVar, smplFlowTypeRadioVar
    # Save File Frame Vars
    global saveSeePntsCheckVar, saveDetFrqCheckVar, saveVerCheckVar
    # XYZ Vars
    global xyzFrameVar, xyzV_DivScaleVar, xyzSftCrvCheckVar, xyvViwChnlsCheckVar

    ################Call Back Functions########################
    # Frame Call Back
    def xyzFrameCmd():
        print("xyz", xyzFrameVar.get())
        val = xyzFrameVar.get()

        topl = XYZ_PlotTopLevel()
        
        if val == 1:
            xyzV_DivScale.config(state=NORMAL); xyzSftCrvCheck.config(state=NORMAL); xyvViwChnlsCheck.config(state=NORMAL)
            topl.create()
        else:
            xyzV_DivScale.config(state=DISABLED); xyzSftCrvCheck.config(state=DISABLED); xyvViwChnlsCheck.config(state=DISABLED)
            topl._destroy()

    # Signal Gen Scroll Callback Functions
    def sgnlFreqScaleCmd(val):
         print("sigGen", val)
         sgnlFreqScaleLable.config(text="f {} Hz".format(val))

    def sgnlPeriodScaleCmd(val):
         print("sigGen", val)
         sgnlPeriodScaleLable.config(text="T {} ms".format(val))

    def sgnlt_onScaleCmd(val):
         print("sigGen", val)
         sgnlt_onScaleLable.config(text="T_on {}%".format(val))
    # Sampling CallBack Functions
    def smplDtScaleCmd(val):
         print("samlpling", val)
         smplDtScale.config(label="dt {}ms".format(val))
    
    def smplQScaleCmd(val):
         print("sampling", val)
         smplQScale.config(label="q {}".format(val))

    def smplFlowTypeRadioCmd():
        print(smplFlowTypeRadioVar.get())
    # Save File CallBacks
    def saveDataButtnCmd():
        print("save file")
    
    def saveSeePntsCheckCmd():
        global lineMarker, graph0
        print("see points ", saveSeePntsCheckVar.get())
        lineMarker.set("o")
        print("save check = ", lineMarker.get())

        paneGraphs.forget(graph0)
        # graph0 = createGraph(paneGraphs, texT="graph0", bG="red", figsizE=(5,1.35), lineColor="red")
        paneGraphs.add(graph0, before=graph1)


        

    # XYZ Call Backs
    def xyzV_DivScaleCmd(val):
        print("xyz", val)
        xyzV_DivScaleLable.config(text="{} V/Div".format(val))
        p = ani0._interval
        print(p)
    ###########################################################

    mainFrameOptions = LabelFrame(parent, bg="blue", width=750)
    mainFrameOptions.grid_rowconfigure(0, weight=1)
    mainFrameOptions.grid_columnconfigure(0, weight=1)
    
    # create a holder for the Meter
    mtrFrame = LabelFrame(mainFrameOptions, labelwidget=Checkbutton(text="Meter"), width=100)
    mtrFrame.pack(side=LEFT, anchor="w", fill=Y, pady=5, padx=5)

    # create a holder for the Signal Generator
    sgnlFrame = LabelFrame(mainFrameOptions, labelwidget=Checkbutton(text="Signal Gen", variable=sgnlFrameVar , command=lambda: print("sgnlGen", sgnlFrameVar.get())), width=100)

    fm1 = Frame(sgnlFrame)
    sgnlFreqScale = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=sgnlFreqScaleCmd, variable=sgnlFreqScaleVar)  # Frequency Scale
    sgnlFreqScale.pack(side=LEFT)
    sgnlFreqScaleLable = Label(fm1, text="f {} Hz".format(sgnlFreqScaleVar.get()))
    sgnlFreqScaleLable.pack(side=LEFT)
    fm1.pack()
    fm2 = Frame(sgnlFrame)
    sgnlPeriodScale = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=sgnlPeriodScaleCmd, variable=sgnlPeriodScaleVar)  # Period Scale 
    sgnlPeriodScale.pack(side=LEFT)
    sgnlPeriodScaleLable = Label(fm2, text="T {} ms".format(sgnlPeriodScaleVar.get()))
    sgnlPeriodScaleLable.pack(side=LEFT)
    fm2.pack()
    fm3 = Frame(sgnlFrame)
    sgnlt_onScale = Scale(fm3, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=sgnlt_onScaleCmd, variable=sgnlt_onScaleVar) # Time on scale
    sgnlt_onScale.pack(side=LEFT)
    sgnlt_onScaleLable = Label(fm3, text="T_on {}%".format(sgnlt_onScaleVar.get()))
    sgnlt_onScaleLable.pack(side=LEFT)
    fm3.pack()

    sgnlFrame.pack(side=LEFT, anchor="w", fill=Y, pady=5, padx=5)

    # create a holder for the Sampling Controls
    smplFrame = LabelFrame(mainFrameOptions, text="Sampling Controls", width=200)

    fm1 = Frame(smplFrame)
    smplDtScale = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, label="dt {}ms".format(smplDtScaleVar.get()), sliderlength=10, showvalue=0, command=smplDtScaleCmd, variable=smplDtScaleVar) # Sampling dt Scale
    smplDtScale.pack(side=LEFT)
    smplQScale = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, label="q {}".format(smplQScaleVar.get()), sliderlength=10, showvalue=0, command=smplQScaleCmd, variable=smplQScaleVar) # Sampling q Scale | number of variables
    smplQScale.pack(side=LEFT)
    fm1.pack()
    fm2 = Frame(smplFrame)
    smplFlowTypeRadio = Radiobutton(fm2, text="ONCE", variable=smplFlowTypeRadioVar, value="once", indicatoron=0, command=smplFlowTypeRadioCmd) # receive only one sample
    smplFlowTypeRadio.pack(side=LEFT, padx=5)
    smplFlowTypeRadio = Radiobutton(fm2, text="VARIOUS", variable=smplFlowTypeRadioVar, value="various", indicatoron=0, command=smplFlowTypeRadioCmd)
    smplFlowTypeRadio.pack(side=LEFT)
    smplFlowTypeRadio = Radiobutton(fm2, text="FLOW", variable=smplFlowTypeRadioVar, value="flow", indicatoron=0, command=smplFlowTypeRadioCmd)
    smplFlowTypeRadio.pack(side=LEFT, padx=5)
    fm2.pack()
    fm3 = Frame(smplFrame)
    sgnlRealLable = Label(fm3, text="Real: dt {}fs ".format(sgnlRealLableVar.get())) # dt size (ms)
    sgnlRealLable.pack(side=LEFT)
    sgnlTotalLable = Label(fm3, text="total : {}fs".format(sgnlTotalLableVar.get())) # total sample time
    sgnlTotalLable.pack(side=LEFT)
    fm3.pack()
    smplFrame.pack(side=LEFT, anchor="w", fill=Y, pady=5, padx=5)

    # create a holder for the SeePoints, DetectFreq, SaveData Controls
    saveFrame = LabelFrame(mainFrameOptions, text="", width=200)

    saveSeePntsCheck = Checkbutton(saveFrame, text="See Points", indicatoron=1, variable=saveSeePntsCheckVar, command=saveSeePntsCheckCmd)
    saveSeePntsCheck.pack(anchor="w")
    fm1 = Frame(saveFrame)
    saveDetFrqCheck = Checkbutton(fm1, text="Detect Freq", indicatoron=1, variable=saveDetFrqCheckVar, command=lambda: print(saveDetFrqCheckVar.get()))
    saveDetFrqCheck.pack(side=LEFT)
    saveVerCheck = Checkbutton(fm1, text="ver", indicatoron=1, variable=saveVerCheckVar, command=lambda: print(saveVerCheckVar.get()))
    saveVerCheck.pack(side=LEFT)
    fm1.pack()
    saveDataButtn = Button(saveFrame, text="Save Data", width=15, relief=GROOVE, command=saveDataButtnCmd)
    saveDataButtn.pack(pady=5)
    
    saveFrame.pack(side=LEFT, anchor="w", fill=Y, pady=5, padx=5)
    
    # create a holder for the XYZ Chanel Controls
    xyzFrame = LabelFrame(mainFrameOptions, labelwidget=Checkbutton(text=" XYZ ", variable=xyzFrameVar , command=xyzFrameCmd, width=20))

    fm1 = Frame(xyzFrame)
    xyzV_DivScale = Scale(fm1, state=DISABLED, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=xyzV_DivScaleCmd, variable=xyzV_DivScaleVar) # Time on scale
    xyzV_DivScale.pack(side=LEFT, padx=3)
    xyzV_DivScaleLable = Label(fm1, text="{} V/Div".format(xyzV_DivScaleVar.get()))
    xyzV_DivScaleLable.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(xyzFrame)
    xyzSftCrvCheck = Checkbutton(fm2, state=DISABLED, text="Soft Curves", indicatoron=1, variable=xyzSftCrvCheckVar, command=lambda: print(xyzSftCrvCheckVar.get()))
    xyzSftCrvCheck.pack(side=BOTTOM, anchor="w")
    xyvViwChnlsCheck = Checkbutton(fm2, state=DISABLED, text="View Channels", indicatoron=1, variable=xyvViwChnlsCheckVar, command=lambda: print(xyvViwChnlsCheckVar.get()))
    xyvViwChnlsCheck.pack(side=BOTTOM, anchor="w")
    fm2.pack(pady=5)

    xyzFrame.pack(side=RIGHT, anchor="w", fill=Y, pady=5, padx=5)
    
    return mainFrameOptions

def main():

    ############# global variables ###########################
    # global widgets
    global root, lineMarker, ani0
    # createChanelsHolder Variables
    global ch0FrameVar, ch0TrigCheckVar, ch0MeasureCheckVar, ch0CurveCheckVar, ch0V_DivSclVar,\
            ch1FrameVar, ch1TrigCheckVar, ch1MeasureCheckVar, ch1CurveCheckVar, ch1V_DivSclVar,\
            ch2FrameVar, ch2TrigCheckVar, ch2MeasureCheckVar, ch2CurveCheckVar, ch2V_DivSclVar,\
            ch3FrameVar, ch3TrigCheckVar, ch3MeasureCheckVar, ch3CurveCheckVar, ch3V_DivSclVar
    # Signal Generator Vars
    global sgnlFrameVar, sgnlFreqScaleVar, sgnlPeriodScaleVar, sgnlt_onScaleVar
    # Sampling Vars
    global smplDtScaleVar, smplQScaleVar, sgnlRealLableVar, sgnlTotalLableVar, smplFlowTypeRadioVar
    # Save File Frame Vars
    global saveSeePntsCheckVar, saveDetFrqCheckVar, saveVerCheckVar
    # XYZ Vars
    global xyzFrameVar, xyzV_DivScaleVar, xyzSftCrvCheckVar, xyvViwChnlsCheckVar

    #########################################################

    root = Tk()
    root.geometry(SIZE)
    root.title("Arduino Oscilloscope")
    # root.iconbitmap(default="Assets\youtube-dl-gui.bmp", )
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    ################# tkinter variables ###########################
        # global widget vars
    lineMarker = StringVar()
        # createChanelsHolder Variables
    ch0FrameVar = IntVar(); ch0TrigCheckVar = IntVar(); ch0MeasureCheckVar = IntVar(); ch0CurveCheckVar = IntVar(); ch0V_DivSclVar = IntVar()
    ch1FrameVar = IntVar(); ch1TrigCheckVar = IntVar(); ch1MeasureCheckVar = IntVar(); ch1CurveCheckVar = IntVar(); ch1V_DivSclVar = IntVar()
    ch2FrameVar = IntVar(); ch2TrigCheckVar = IntVar(); ch2MeasureCheckVar = IntVar(); ch2CurveCheckVar = IntVar(); ch2V_DivSclVar = IntVar()
    ch3FrameVar = IntVar(); ch3TrigCheckVar = IntVar(); ch3MeasureCheckVar = IntVar(); ch3CurveCheckVar = IntVar(); ch3V_DivSclVar = IntVar()
        # Signal Generator makeControls_Options_FileIOFrame Variables
    sgnlFrameVar = IntVar(); sgnlFreqScaleVar = IntVar(); sgnlPeriodScaleVar = IntVar() ; sgnlt_onScaleVar = IntVar()
        # Sampling makeControls_Options_FileIOFrame Variables
    smplDtScaleVar = IntVar(); smplQScaleVar = IntVar(); sgnlRealLableVar = IntVar(); sgnlTotalLableVar = IntVar(); smplFlowTypeRadioVar = StringVar()
        # Save File Frame makeControls_Options_FileIOFrame Vars
    saveSeePntsCheckVar = IntVar(); saveDetFrqCheckVar = IntVar(); saveVerCheckVar = IntVar()
        # XYZ makeControls_Options_FileIOFrame Vars
    xyzFrameVar = IntVar(); xyzV_DivScaleVar = IntVar(); xyzSftCrvCheckVar = IntVar(); xyvViwChnlsCheckVar = IntVar()
    #############################################################
    ch0FrameVar.set(1)
    ch1FrameVar.set(1)
    ch2FrameVar.set(1)
    ch3FrameVar.set(1)
    lineMarker.set("v")

    menubar = createMenuBar(root)

    paneMain = PanedWindow(orient=VERTICAL, sashwidth=5, sashrelief=SOLID, bg='#ddd')
    paneMain.add(makeGraphandChanelsFrame(paneMain), minsize=620)
    paneMain.add(makeControls_Options_FileIOFrame(paneMain), minsize=120)
    paneMain.grid(row=0, sticky='news')

    ### Call init function

    root.config(menu=menubar)
    ani0 = animation.FuncAnimation(f0, animateGraph0, interval=100)
    ani1 = animation.FuncAnimation(f1, animateGraph1, interval=1000)
    ani2 = animation.FuncAnimation(f2, animateGraph2, interval=1000)
    ani3 = animation.FuncAnimation(f3, animateGraph3, interval=1000)
    # ani33 = animation.FuncAnimation(f0, animate, init_func=init, interval=2, blit=True, save_count=50)
    # root.resizable(0,0)
    root.mainloop()



def __init__():
    print("init funcion")
    global lineMarker

    # ch0FrameVar.set(1)
    # ch1FrameVar.set(1)
    # ch2FrameVar.set(1)
    # ch3FrameVar.set(1)
    # lineMarker.set("v")


if __name__ == "__main__":

    main()
    