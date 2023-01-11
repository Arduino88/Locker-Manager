from tkinter import *
from tkinter import ttk
import os
import sv_ttk

memoryList = []
trimmedMemoryList = []

desktop = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
masterListLocation = desktop + "\LockerManager\masterlist.txt"

#BUTTON FUNCTIONS
def readMasterList():
    with open(masterListLocation) as masterFile:
        for line in masterFile:
            memoryList.append(line)
    for sub in memoryList:
        trimmedMemoryList.append(sub.replace("\n", ""))

def saveList():
    with open(masterListLocation, "w") as masterFile:
        masterFile.write("\n".join(trimmedMemoryList))

def updateLockerList(*args):
    lockerNumber0.set(sectionThousands.get() + sectionHundreds.get() + sectionTens.get())
    if lockerNumber0.get() == 0:
        lockerNumber0.set(1)
    lockerNumber1.set(lockerNumber0.get() + 1)
    lockerNumber2.set(lockerNumber0.get() + 2)
    lockerNumber3.set(lockerNumber0.get() + 3)
    lockerNumber4.set(lockerNumber0.get() + 4)
    lockerNumber5.set(lockerNumber0.get() + 5)
    lockerNumber6.set(lockerNumber0.get() + 6)
    lockerNumber7.set(lockerNumber0.get() + 7)
    lockerNumber8.set(lockerNumber0.get() + 8)
    lockerNumber9.set(lockerNumber0.get() + 9)
    lockerText0.set(trimmedMemoryList[lockerNumber0.get()])
    lockerText1.set(trimmedMemoryList[lockerNumber1.get()])
    lockerText2.set(trimmedMemoryList[lockerNumber2.get()])
    lockerText3.set(trimmedMemoryList[lockerNumber3.get()])
    lockerText4.set(trimmedMemoryList[lockerNumber4.get()])
    lockerText5.set(trimmedMemoryList[lockerNumber5.get()])
    lockerText6.set(trimmedMemoryList[lockerNumber6.get()])
    lockerText7.set(trimmedMemoryList[lockerNumber7.get()])
    lockerText8.set(trimmedMemoryList[lockerNumber8.get()])
    lockerText9.set(trimmedMemoryList[lockerNumber9.get()])
    root.after(100, updateLockerList)

def addStudent(*args):
    try:
        trimmedMemoryList[int(entryLocker.get())] = studentName.get()
        saveList()
    except ValueError:
        pass

def removeStudent(*args):
    try:
        trimmedMemoryList[int(entryClearLocker.get())] = "empty"
        saveList()
    except ValueError:
        pass

#ROOT
root = Tk()
root.title("Locker Manager v1.2")

#VARIABLE INITIALIZATION
studentName = StringVar()
lockerNumber = StringVar()
removeLockerNumber = StringVar()
lockerText0 = StringVar()
lockerText1 = StringVar()
lockerText2 = StringVar()
lockerText3 = StringVar()
lockerText4 = StringVar()
lockerText5 = StringVar()
lockerText6 = StringVar()
lockerText7 = StringVar()
lockerText8 = StringVar()
lockerText9 = StringVar()
lockerNumber0 = IntVar()
lockerNumber1 = IntVar()
lockerNumber2 = IntVar()
lockerNumber3 = IntVar()
lockerNumber4 = IntVar()
lockerNumber5 = IntVar()
lockerNumber6 = IntVar()
lockerNumber7 = IntVar()
lockerNumber8 = IntVar()
lockerNumber9 = IntVar()
sectionThousands = IntVar()
sectionHundreds = IntVar()
sectionTens = IntVar()

#MAINFRAME
mainframe = ttk.Frame(root, padding=(3,3,12,12))

#MAINFRAME LABELFRAMES
assignLockerLabelFrame = ttk.LabelFrame(mainframe, text="Assign Locker")
browseLockerLabelFrame = ttk.LabelFrame(mainframe, text="Browse Lockers")
clearLockerLabelFrame = ttk.LabelFrame(mainframe, text="Clear Locker")

#ASSIGN LOCKER LABELFRAME
lblStudentName = ttk.Label(assignLockerLabelFrame, text="Student Name:")
lblLockerNumber = ttk.Label(assignLockerLabelFrame, text="Locker Number:")
entryName = ttk.Entry(assignLockerLabelFrame, textvariable=studentName)
entryLocker = ttk.Entry(assignLockerLabelFrame, textvariable=lockerNumber)
btnAdd = ttk.Button(assignLockerLabelFrame, text="ADD", command=addStudent)

#CLEAR LOCKER LABELFRAME
lblClearLockerNumber = ttk.Label(clearLockerLabelFrame, text="Locker Number:")
entryClearLocker = ttk.Entry(clearLockerLabelFrame, textvariable=removeLockerNumber)
btnClearLocker = ttk.Button(clearLockerLabelFrame, text="CLEAR", command=removeStudent)

#BROWSE LOCKER FRAMES
browseLockerListFrame = ttk.Frame(browseLockerLabelFrame, borderwidth=0.5, relief="sunken")
lblLockerListHeader = ttk.Label(browseLockerListFrame, text="Lockers", font=("Heading", 16))
lblLocker0 = ttk.Label(browseLockerListFrame, textvariable=lockerText0)
lblLocker1 = ttk.Label(browseLockerListFrame, textvariable=lockerText1)
lblLocker2 = ttk.Label(browseLockerListFrame, textvariable=lockerText2)
lblLocker3 = ttk.Label(browseLockerListFrame, textvariable=lockerText3)
lblLocker4 = ttk.Label(browseLockerListFrame, textvariable=lockerText4)
lblLocker5 = ttk.Label(browseLockerListFrame, textvariable=lockerText5)
lblLocker6 = ttk.Label(browseLockerListFrame, textvariable=lockerText6)
lblLocker7 = ttk.Label(browseLockerListFrame, textvariable=lockerText7)
lblLocker8 = ttk.Label(browseLockerListFrame, textvariable=lockerText8)
lblLocker9 = ttk.Label(browseLockerListFrame, textvariable=lockerText9)
lblLockerNumber0 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber0)
lblLockerNumber1 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber1)
lblLockerNumber2 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber2)
lblLockerNumber3 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber3)
lblLockerNumber4 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber4)
lblLockerNumber5 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber5)
lblLockerNumber6 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber6)
lblLockerNumber7 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber7)
lblLockerNumber8 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber8)
lblLockerNumber9 = ttk.Label(browseLockerListFrame, textvariable=lockerNumber9)

lblSectionNumber = ttk.Label(browseLockerLabelFrame, text="Section Number", font=("Heading", 25))
rBtnZeros = ttk.Radiobutton(browseLockerLabelFrame, text="0s", variable=sectionThousands, value=0)
rBtnThousands = ttk.Radiobutton(browseLockerLabelFrame, text="1000s", variable=sectionThousands, value=1000)
rBtnTwoThousands = ttk.Radiobutton(browseLockerLabelFrame, text="2000s", variable=sectionThousands, value=2000)
rBtnThreeThousands = ttk.Radiobutton(browseLockerLabelFrame, text="3000s", variable=sectionThousands, value=3000)
cbxHundreds = ttk.Combobox(browseLockerLabelFrame, textvariable=sectionHundreds)
cbxHundreds["values"] = (0, 100, 200, 300, 400, 500, 600, 700, 800, 900)
spxTens = ttk.Spinbox(browseLockerLabelFrame, from_=0, to=90, increment=10, textvariable=sectionTens)

#MAINFRAME LABELFRAMES GRID FORMATTING
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), ipadx=5, ipady=5)
assignLockerLabelFrame.grid(column=0, row=0, sticky=(N, W, E, S), ipadx=5, ipady=5)
clearLockerLabelFrame.grid(column=1, row=0, sticky=(N, W, E, S), ipadx=5, ipady=5)
browseLockerLabelFrame.grid(column=0, row=1, columnspan=2, sticky=(N, W, E, S), ipadx=5, ipady=5)

#ASSIGN LOCKER LABELFRAME GRID FORMATTING
lblStudentName.grid(column=0, row=0)
lblLockerNumber.grid(column=0, row=1)
entryName.grid(column=1, row=0, sticky=(N, W, E, S))
entryLocker.grid(column=1, row=1, sticky=(N, W, E, S))
btnAdd.grid(column=1, row=2, sticky=(N, W, E, S))

#CLEAR LOCKER LABELFRAME GRID FORMATTING
lblClearLockerNumber.grid(column=0, row=0)
entryClearLocker.grid(column=0, row=1, sticky=(N, E, S, W))
btnClearLocker.grid(column=0, row=2, sticky=(N, E, S, W))

#LOCKER LABEL FRAME GRID FORMATTING
browseLockerListFrame.grid(column=0, row=0, rowspan=5, ipadx=5, sticky=(N, E, S, W))
lblLockerListHeader.grid(column=0, row=0, columnspan=2)
lblLocker0.grid(column=1, row=1)
lblLocker1.grid(column=1, row=2)
lblLocker2.grid(column=1, row=3)
lblLocker3.grid(column=1, row=4)
lblLocker4.grid(column=1, row=5)
lblLocker5.grid(column=1, row=6)
lblLocker6.grid(column=1, row=7)
lblLocker7.grid(column=1, row=8)
lblLocker8.grid(column=1, row=9)
lblLocker9.grid(column=1, row=10)
lblLockerNumber0.grid(column=0, row=1)
lblLockerNumber1.grid(column=0, row=2)
lblLockerNumber2.grid(column=0, row=3)
lblLockerNumber3.grid(column=0, row=4)
lblLockerNumber4.grid(column=0, row=5)
lblLockerNumber5.grid(column=0, row=6)
lblLockerNumber6.grid(column=0, row=7)
lblLockerNumber7.grid(column=0, row=8)
lblLockerNumber8.grid(column=0, row=9)
lblLockerNumber9.grid(column=0, row=10)
lblSectionNumber.grid(column=1, row=0, columnspan=2)
rBtnZeros.grid(column=1, row=1)
rBtnThousands.grid(column=1, row=2)
rBtnTwoThousands.grid(column=1, row=3)
rBtnThreeThousands.grid(column=1, row=4)
cbxHundreds.grid(column=2, row=1, rowspan=2, sticky=(E, W))
cbxHundreds.bind("<<CombobocSelected>>", updateLockerList)
spxTens.grid(column=2, row=3, rowspan=2, sticky=(E, W))
spxTens.bind()

#COLUMN WEIGHTS
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=2)

assignLockerLabelFrame.columnconfigure(0, weight=1)
assignLockerLabelFrame.columnconfigure(1, weight=200)
assignLockerLabelFrame.rowconfigure(0, weight=1)
assignLockerLabelFrame.rowconfigure(1, weight=1)
assignLockerLabelFrame.rowconfigure(2, weight=1)

clearLockerLabelFrame.columnconfigure(0, weight=1)
clearLockerLabelFrame.rowconfigure(0, weight=1)
clearLockerLabelFrame.rowconfigure(1, weight=1)
clearLockerLabelFrame.rowconfigure(2, weight=1)

browseLockerLabelFrame.columnconfigure(0, weight=1)
browseLockerLabelFrame.columnconfigure(1, weight=1)
browseLockerLabelFrame.columnconfigure(2, weight=2)
browseLockerLabelFrame.rowconfigure(0, weight=1)
browseLockerLabelFrame.rowconfigure(1, weight=1)
browseLockerLabelFrame.rowconfigure(2, weight=1)
browseLockerLabelFrame.rowconfigure(3, weight=1)
browseLockerLabelFrame.rowconfigure(4, weight=1)

browseLockerListFrame.columnconfigure(0, weight=1)
browseLockerListFrame.columnconfigure(1, weight=2)
browseLockerListFrame.rowconfigure(0, weight=1)
browseLockerListFrame.rowconfigure(1, weight=1)
browseLockerListFrame.rowconfigure(2, weight=1)
browseLockerListFrame.rowconfigure(3, weight=1)
browseLockerListFrame.rowconfigure(4, weight=1)
browseLockerListFrame.rowconfigure(5, weight=1)
browseLockerListFrame.rowconfigure(6, weight=1)
browseLockerListFrame.rowconfigure(7, weight=1)
browseLockerListFrame.rowconfigure(8, weight=1)
browseLockerListFrame.rowconfigure(9, weight=1)

#PADDING LOOPS
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in assignLockerLabelFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in clearLockerLabelFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in browseLockerLabelFrame.winfo_children():
    child.grid_configure(padx=15, pady=15)

for child in browseLockerListFrame.winfo_children():
    child.grid_configure(padx=15, pady=5)

readMasterList()

#THEME
sv_ttk.set_theme("dark")

#GRAPHICS LOOP
root.after(100, updateLockerList)
root.mainloop()