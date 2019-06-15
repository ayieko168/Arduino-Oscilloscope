from tkinter import *
# from createPlot import Graph
# from tkinter import ttk

SIZE = "1000x800+50+50"  # size string: WxH+X+Y
MENUFONT = ('Comic Sans MS', '9', 'normal', 'roman')

def translate(side="w", percentage=20, parent=None):

    parent.update()
    parent.update_idletasks()
    h = parent.winfo_height() # height of parent in pxls
    w = parent.winfo_width() # width of parent in pxls

    print(h, w)

def createGraphsHolder(parent):
    """create a holder for the Actual Graphs"""

    graphsFrame = LabelFrame(parent, text="graphs", width=780, height=50, bg="indigo")
    graphsFrame.grid_rowconfigure(0, weight=1)
    graphsFrame.grid_columnconfigure(0, weight=1)

    def createGraph(parent, texT=None, heighT=155, bG="white"):
        """create the plot/graph area for the graphs"""
        gFrame = LabelFrame(parent, text=texT,
                                height=heighT, bg=bG)
        return gFrame
    
    paneGraphs = PanedWindow(graphsFrame, orient=VERTICAL, sashwidth=5, sashrelief=SOLID, bg='#ddd')
    paneGraphs.add(createGraph(paneGraphs, texT="graph0", bG="red"), minsize=50)
    paneGraphs.add(createGraph(paneGraphs, texT="graph1", bG="green"), minsize=50)
    paneGraphs.add(createGraph(paneGraphs, texT="graph2", bG="blue"), minsize=50)
    paneGraphs.add(createGraph(paneGraphs, texT="graph3", bG="yellow"), minsize=50)
    paneGraphs.grid(row=0, sticky='news')

    graphsFrame.config(height=640, padx=5, pady=5) #important for maintainance of height of the graphs frame container
    return graphsFrame

def createChanelsHolder(parent):
    """create a holder for the Chanel Controls"""

    global mtrFrame0Var, ch0TrigCheckVar, ch0MeasureCheckVar, ch0CurveCheckVar, ch0V_DivSclVar,\
            mtrFrame1Var, ch1TrigCheckVar, ch1MeasureCheckVar, ch1CurveCheckVar, ch1V_DivSclVar,\
            mtrFrame2Var, ch2TrigCheckVar, ch2MeasureCheckVar, ch2CurveCheckVar, ch2V_DivSclVar,\
            mtrFrame3Var, ch3TrigCheckVar, ch3MeasureCheckVar, ch3CurveCheckVar, ch3V_DivSclVar

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


    chCntrlFrame = LabelFrame(parent, text="chanels")

    # create a holder for Chanel 0 Controls
    mtrFrame0 = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch0", background='red', font=12,
                                                                variable=mtrFrame0Var, command=lambda: print("ch0", mtrFrame0Var.get())),
                            width=100, height=150, bg="red")
    
    fm1 = Frame(mtrFrame0)
    ch0V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch0V_DivSclCmd, variable=ch0V_DivSclVar)
    ch0V_DivScl.pack(side=LEFT)
    ch0V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch0V_DivSclVar.get()))
    ch0V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(mtrFrame0)
    ch0Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch0Ms_DivSclCmd)
    ch0Ms_DivScl.pack(side=LEFT)
    ch0Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch0V_DivSclVar.get()))
    ch0Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch0MeasureCheck = Checkbutton(mtrFrame0, text="Measure", indicatoron=0, variable=ch0MeasureCheckVar, command=lambda: print(ch0MeasureCheckVar.get()))
    ch0MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch0CurveCheck = Checkbutton(mtrFrame0, text="Curve", indicatoron=0, variable=ch0CurveCheckVar, command=lambda: print(ch0CurveCheckVar.get()))
    ch0CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch0TrigCheck = Checkbutton(mtrFrame0, text="Triger", indicatoron=0, variable=ch0TrigCheckVar, command=lambda: print(ch0TrigCheckVar.get()))
    ch0TrigCheck.pack(side=LEFT, padx=2, pady=5)

    mtrFrame0.pack(pady=5, padx=5)

    # create a holder for Chanel 1 Controls
    mtrFrame1 = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch1", font=12, bg="green", variable=mtrFrame1Var,
                                                                command=lambda: print("ch1", mtrFrame1Var.get())),
                            width=100, height=150, bg="green")

    fm1 = Frame(mtrFrame1)
    ch1V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch1V_DivSclCmd, variable=ch1V_DivSclVar)
    ch1V_DivScl.pack(side=LEFT)
    ch1V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch1V_DivSclVar.get()))
    ch1V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(mtrFrame1)
    ch1Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch1Ms_DivSclCmd)
    ch1Ms_DivScl.pack(side=LEFT)
    ch1Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch1V_DivSclVar.get()))
    ch1Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch1MeasureCheck = Checkbutton(mtrFrame1, text="Measure", indicatoron=0, variable=ch1MeasureCheckVar, command=lambda: print(ch1MeasureCheckVar.get()))
    ch1MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch1CurveCheck = Checkbutton(mtrFrame1, text="Curve", indicatoron=0, variable=ch1CurveCheckVar, command=lambda: print(ch1CurveCheckVar.get()))
    ch1CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch1TrigCheck = Checkbutton(mtrFrame1, text="Triger", indicatoron=0, variable=ch1TrigCheckVar, command=lambda: print(ch1TrigCheckVar.get()))
    ch1TrigCheck.pack(side=LEFT, padx=2, pady=5)

    mtrFrame1.pack(pady=5, padx=5)

    # create a holder for Chanel 2 Controls
    mtrFrame2 = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch2", font=12, bg="blue", variable=mtrFrame2Var,
                                                                command=lambda: print("ch2", mtrFrame2Var.get())),
                            width=100, height=150, bg="blue")
    
    fm1 = Frame(mtrFrame2)
    ch2V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch2V_DivSclCmd, variable=ch2V_DivSclVar)
    ch2V_DivScl.pack(side=LEFT)
    ch2V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch2V_DivSclVar.get()))
    ch2V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(mtrFrame2)
    ch2Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch2Ms_DivSclCmd)
    ch2Ms_DivScl.pack(side=LEFT)
    ch2Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch2V_DivSclVar.get()))
    ch2Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch2MeasureCheck = Checkbutton(mtrFrame2, text="Measure", indicatoron=0, variable=ch2MeasureCheckVar, command=lambda: print(ch2MeasureCheckVar.get()))
    ch2MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch2CurveCheck = Checkbutton(mtrFrame2, text="Curve", indicatoron=0, variable=ch2CurveCheckVar, command=lambda: print(ch2CurveCheckVar.get()))
    ch2CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch2TrigCheck = Checkbutton(mtrFrame2, text="Triger", indicatoron=0, variable=ch2TrigCheckVar, command=lambda: print(ch2TrigCheckVar.get()))
    ch2TrigCheck.pack(side=LEFT, padx=2, pady=5)
    
    mtrFrame2.pack(pady=5, padx=5)

    # create a holder for Chanel 3 Controls
    mtrFrame3 = LabelFrame(chCntrlFrame, labelwidget=Checkbutton(text="ch3", font=12, bg="yellow", variable=mtrFrame3Var,
                                                                command=lambda: print("ch3", mtrFrame3Var.get())),
                            width=100, height=150, bg="yellow")
    
    fm1 = Frame(mtrFrame3)
    ch3V_DivScl = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch3V_DivSclCmd, variable=ch3V_DivSclVar)
    ch3V_DivScl.pack(side=LEFT)
    ch3V_DivSclValLabel = Label(fm1, text="{} V/Div".format(ch3V_DivSclVar.get()))
    ch3V_DivSclValLabel.pack(side=LEFT)
    fm1.pack(pady=5)
    fm2 = Frame(mtrFrame3)
    ch3Ms_DivScl = Scale(fm2, orient=HORIZONTAL, from_=1, to=20, sliderlength=10, showvalue=0, command=ch3Ms_DivSclCmd)
    ch3Ms_DivScl.pack(side=LEFT)
    ch3Ms_DivSclLabel = Label(fm2, text="{} ms/Div".format(ch3V_DivSclVar.get()))
    ch3Ms_DivSclLabel.pack(side=LEFT)
    fm2.pack(pady=5)
    ch3MeasureCheck = Checkbutton(mtrFrame3, text="Measure", indicatoron=0, variable=ch3MeasureCheckVar, command=lambda: print(ch3MeasureCheckVar.get()))
    ch3MeasureCheck.pack(side=LEFT, padx=2, pady=5)
    ch3CurveCheck = Checkbutton(mtrFrame3, text="Curve", indicatoron=0, variable=ch3CurveCheckVar, command=lambda: print(ch3CurveCheckVar.get()))
    ch3CurveCheck.pack(side=LEFT, padx=2, pady=5)
    ch3TrigCheck = Checkbutton(mtrFrame3, text="Triger", indicatoron=0, variable=ch3TrigCheckVar, command=lambda: print(ch3TrigCheckVar.get()))
    ch3TrigCheck.pack(side=LEFT, padx=2, pady=5)

    mtrFrame3.pack(pady=5, padx=5)
    
    chCntrlFrame.config(height=640) #important for maintainance of height
    return chCntrlFrame
       
def createMenuBar(parent):

    menubar = Menu(parent, font=MENUFONT)

    fileMenu = Menu(tearoff=0, font=MENUFONT)
    fileMenu.add_command(label="Exit")

    menubar.add_cascade(label="File", menu=fileMenu)

    return menubar

def makeGraph_ChanelsFrame(parent):
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

    
        return xyzTopLevel
    
    def _destroy(self):

        xyzTopLevel.destroy()

def makeControls_Options_FileIOFrame(parent):
    """create a holder for the Meter, Sampling controls, Data save, Signal generator"""

    # Signal Gen Vars
    global sgnlFrameVar, sgnlFreqScaleVar, sgnlPeriodScaleVar, sgnlt_onScaleVar
    # Sampling Vars
    global smplDtScaleVar, smplQScaleVar, sgnlRealLableVar, sgnlTotalLableVar, smplFlowTypeRadioVar
    # Save File Frame Vars
    global saveSeePntsCheckVar, saveDetFrqCheckVar, saveVerCheckVar
    # XYZ Vars
    global xyzFrameVar, xyzV_DivScaleVar, xyzSftCrvCheckVar, xyvViwChnlsCheckVar

    ################Call Back Functions########################
    # XYZ Frame Call Back
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
    # XYZ Call Backs
    def xyzV_DivScaleCmd(val):
        print("xyz", val)
        xyzV_DivScaleLable.config(text="{} V/Div".format(val))
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
    smplQScale = Scale(fm1, orient=HORIZONTAL, from_=1, to=20, label="q {}".format(smplQScaleVar.get()), sliderlength=10, showvalue=0, command=smplQScaleCmd, variable=smplQScaleVar) # Sampling q Scale
    smplQScale.pack(side=LEFT)
    fm1.pack()
    fm2 = Frame(smplFrame)
    smplFlowTypeRadio = Radiobutton(fm2, text="ONCE", variable=smplFlowTypeRadioVar, value="once", indicatoron=0, command=smplFlowTypeRadioCmd)
    smplFlowTypeRadio.pack(side=LEFT, padx=5)
    smplFlowTypeRadio = Radiobutton(fm2, text="VARIOUS", variable=smplFlowTypeRadioVar, value="various", indicatoron=0, command=smplFlowTypeRadioCmd)
    smplFlowTypeRadio.pack(side=LEFT)
    smplFlowTypeRadio = Radiobutton(fm2, text="FLOW", variable=smplFlowTypeRadioVar, value="flow", indicatoron=0, command=smplFlowTypeRadioCmd)
    smplFlowTypeRadio.pack(side=LEFT, padx=5)
    fm2.pack()
    fm3 = Frame(smplFrame)
    sgnlRealLable = Label(fm3, text="Real: dt {}fs ".format(sgnlRealLableVar.get()))
    sgnlRealLable.pack(side=LEFT)
    sgnlTotalLable = Label(fm3, text="total : {}fs".format(sgnlTotalLableVar.get()))
    sgnlTotalLable.pack(side=LEFT)
    fm3.pack()
    smplFrame.pack(side=LEFT, anchor="w", fill=Y, pady=5, padx=5)

    # create a holder for the SeePoints, DetectFreq, SaveData Controls
    saveFrame = LabelFrame(mainFrameOptions, text="", width=200)

    saveSeePntsCheck = Checkbutton(saveFrame, text="See Points", indicatoron=1, variable=saveSeePntsCheckVar, command=lambda: print(saveSeePntsCheckVar.get()))
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
    global root
    # createChanelsHolder Variables
    global mtrFrame0Var, ch0TrigCheckVar, ch0MeasureCheckVar, ch0CurveCheckVar, ch0V_DivSclVar,\
            mtrFrame1Var, ch1TrigCheckVar, ch1MeasureCheckVar, ch1CurveCheckVar, ch1V_DivSclVar,\
            mtrFrame2Var, ch2TrigCheckVar, ch2MeasureCheckVar, ch2CurveCheckVar, ch2V_DivSclVar,\
            mtrFrame3Var, ch3TrigCheckVar, ch3MeasureCheckVar, ch3CurveCheckVar, ch3V_DivSclVar
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
        # createChanelsHolder Variables
    mtrFrame0Var = IntVar(); ch0TrigCheckVar = IntVar(); ch0MeasureCheckVar = IntVar(); ch0CurveCheckVar = IntVar(); ch0V_DivSclVar = IntVar()
    mtrFrame1Var = IntVar(); ch1TrigCheckVar = IntVar(); ch1MeasureCheckVar = IntVar(); ch1CurveCheckVar = IntVar(); ch1V_DivSclVar = IntVar()
    mtrFrame2Var = IntVar(); ch2TrigCheckVar = IntVar(); ch2MeasureCheckVar = IntVar(); ch2CurveCheckVar = IntVar(); ch2V_DivSclVar = IntVar()
    mtrFrame3Var = IntVar(); ch3TrigCheckVar = IntVar(); ch3MeasureCheckVar = IntVar(); ch3CurveCheckVar = IntVar(); ch3V_DivSclVar = IntVar()
        # Signal Generator makeControls_Options_FileIOFrame Variables
    sgnlFrameVar = IntVar(); sgnlFreqScaleVar = IntVar(); sgnlPeriodScaleVar = IntVar() ; sgnlt_onScaleVar = IntVar()
        # Sampling makeControls_Options_FileIOFrame Variables
    smplDtScaleVar = IntVar(); smplQScaleVar = IntVar(); sgnlRealLableVar = IntVar(); sgnlTotalLableVar = IntVar(); smplFlowTypeRadioVar = StringVar()
        # Save File Frame makeControls_Options_FileIOFrame Vars
    saveSeePntsCheckVar = IntVar(); saveDetFrqCheckVar = IntVar(); saveVerCheckVar = IntVar()
        # XYZ makeControls_Options_FileIOFrame Vars
    xyzFrameVar = IntVar(); xyzV_DivScaleVar = IntVar(); xyzSftCrvCheckVar = IntVar(); xyvViwChnlsCheckVar = IntVar()
    #############################################################

    menubar = createMenuBar(root)

    paneMain = PanedWindow(orient=VERTICAL, sashwidth=5, sashrelief=SOLID, bg='#ddd')
    paneMain.add(makeGraph_ChanelsFrame(paneMain), minsize=620)
    paneMain.add(makeControls_Options_FileIOFrame(paneMain), minsize=120)
    paneMain.grid(row=0, sticky='news')

    root.config(menu=menubar)
    # root.resizable(0,0)
    root.mainloop()

if __name__ == "__main__":
    
    main()
    