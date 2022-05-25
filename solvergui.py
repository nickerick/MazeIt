# Import the required libraries
from tkinter import *
from tkinter import ttk

from matplotlib.pyplot import fill

# Create an instance of Tkinter Frame
win = Tk()
# win.state("zoomed")
win.title('Maze Solver')
win['bg']='#5a5f69'
win.geometry("1920x1000")


win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=4)
win.columnconfigure(2, weight=2)
win.columnconfigure(3, weight=4)
win.columnconfigure(4, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(1, weight=10)
win.rowconfigure(2, weight=1)
win.rowconfigure(3, weight=2)
win.rowconfigure(4, weight=1)
win.rowconfigure(5, weight=2)
win.rowconfigure(6, weight=1)
win.rowconfigure(7, weight=2)
win.rowconfigure(8, weight=1)


# Define a function to change the state of the Widget
def change_color():
   canvas.itemconfig(rectangle, fill='green')

# Define a Canvas Widget
mazeCanvas = Canvas(win, width=600, height=600)
mazeCanvas.grid(column=3, row=1)
# mazeCanvas1 = Canvas(win, width=100, height=100)
# mazeCanvas1.grid(column=3, row=2)
# mazeCanvas1 = Canvas(win, width=100, height=100)
# mazeCanvas1.grid(column=4, row=1)

mazeCanvas['bg'] = '#000000'
mazeCanvas['highlightthickness'] = 0

# ROW 1
mazeBlock0 = mazeCanvas.create_rectangle(0, 0, 60, 60, fill='white')
mazeBlock1 = mazeCanvas.create_rectangle(61, 0, 120, 60, fill='white')
mazeBlock2 = mazeCanvas.create_rectangle(121, 0, 180, 60, fill='white')
mazeBlock3 = mazeCanvas.create_rectangle(181, 0, 240, 60, fill='white')
mazeBlock4 = mazeCanvas.create_rectangle(241, 0, 300, 60, fill='white')
mazeBlock5 = mazeCanvas.create_rectangle(301, 0, 360, 60, fill='white')
mazeBlock6 = mazeCanvas.create_rectangle(361, 0, 420, 60, fill='white')
mazeBlock7 = mazeCanvas.create_rectangle(421, 0, 480, 60, fill='white')
mazeBlock8 = mazeCanvas.create_rectangle(481, 0, 540, 60, fill='white')
mazeBlock9 = mazeCanvas.create_rectangle(541, 0, 600, 60, fill='white')
# ROW 2
mazeBlock10 = mazeCanvas.create_rectangle(0, 61, 60, 120, fill='white')
mazeBlock11 = mazeCanvas.create_rectangle(61, 61, 120, 120, fill='white')
mazeBlock12 = mazeCanvas.create_rectangle(121, 61, 180, 120, fill='white')
mazeBlock13 = mazeCanvas.create_rectangle(181, 61, 240, 120, fill='white')
mazeBlock14 = mazeCanvas.create_rectangle(241, 61, 300, 120, fill='white')
mazeBlock15 = mazeCanvas.create_rectangle(301, 61, 360, 120, fill='white')
mazeBlock16 = mazeCanvas.create_rectangle(361, 61, 420, 120, fill='white')
mazeBlock17 = mazeCanvas.create_rectangle(421, 61, 480, 120, fill='white')
mazeBlock18 = mazeCanvas.create_rectangle(481, 61, 540, 120, fill='white')
mazeBlock19 = mazeCanvas.create_rectangle(541, 61, 600, 120, fill='white')
# ROW 3
mazeBlock20 = mazeCanvas.create_rectangle(0, 121, 60, 180, fill='white')
mazeBlock21 = mazeCanvas.create_rectangle(61, 121, 120, 180, fill='white')
mazeBlock22 = mazeCanvas.create_rectangle(121, 121, 180, 180, fill='white')
mazeBlock23 = mazeCanvas.create_rectangle(181, 121, 240, 180, fill='white')
mazeBlock24 = mazeCanvas.create_rectangle(241, 121, 300, 180, fill='white')
mazeBlock25 = mazeCanvas.create_rectangle(301, 121, 360, 180, fill='white')
mazeBlock26 = mazeCanvas.create_rectangle(361, 121, 420, 180, fill='white')
mazeBlock27 = mazeCanvas.create_rectangle(421, 121, 480, 180, fill='white')
mazeBlock28 = mazeCanvas.create_rectangle(481, 121, 540, 180, fill='white')
mazeBlock29 = mazeCanvas.create_rectangle(541, 121, 600, 180, fill='white')
# ROW 4
mazeBlock30 = mazeCanvas.create_rectangle(0, 181, 60, 240, fill='white')
mazeBlock31 = mazeCanvas.create_rectangle(61, 181, 120, 240, fill='white')
mazeBlock32 = mazeCanvas.create_rectangle(121, 181, 180, 240, fill='white')
mazeBlock33 = mazeCanvas.create_rectangle(181, 181, 240, 240, fill='white')
mazeBlock34 = mazeCanvas.create_rectangle(241, 181, 300, 240, fill='white')
mazeBlock35 = mazeCanvas.create_rectangle(301, 181, 360, 240, fill='white')
mazeBlock36 = mazeCanvas.create_rectangle(361, 181, 420, 240, fill='white')
mazeBlock37 = mazeCanvas.create_rectangle(421, 181, 480, 240, fill='white')
mazeBlock38 = mazeCanvas.create_rectangle(481, 181, 540, 240, fill='white')
mazeBlock39 = mazeCanvas.create_rectangle(541, 181, 600, 240, fill='white')
# ROW 5
mazeBlock40 = mazeCanvas.create_rectangle(0, 241, 60, 300, fill='white')
mazeBlock41 = mazeCanvas.create_rectangle(61, 241, 120, 300, fill='white')
mazeBlock42 = mazeCanvas.create_rectangle(121, 241, 180, 300, fill='white')
mazeBlock43 = mazeCanvas.create_rectangle(181, 241, 240, 300, fill='white')
mazeBlock44 = mazeCanvas.create_rectangle(241, 241, 300, 300, fill='white')
mazeBlock45 = mazeCanvas.create_rectangle(301, 241, 360, 300, fill='white')
mazeBlock46 = mazeCanvas.create_rectangle(361, 241, 420, 300, fill='white')
mazeBlock47 = mazeCanvas.create_rectangle(421, 241, 480, 300, fill='white')
mazeBlock48 = mazeCanvas.create_rectangle(481, 241, 540, 300, fill='white')
mazeBlock49 = mazeCanvas.create_rectangle(541, 241, 600, 300, fill='white')
# ROW 6
mazeBlock50 = mazeCanvas.create_rectangle(0, 301, 60, 360, fill='white')
mazeBlock51 = mazeCanvas.create_rectangle(61, 301, 120, 360, fill='white')
mazeBlock52 = mazeCanvas.create_rectangle(121, 301, 180, 360, fill='white')
mazeBlock53 = mazeCanvas.create_rectangle(181, 301, 240, 360, fill='white')
mazeBlock54 = mazeCanvas.create_rectangle(241, 301, 300, 360, fill='white')
mazeBlock55 = mazeCanvas.create_rectangle(301, 301, 360, 360, fill='white')
mazeBlock56 = mazeCanvas.create_rectangle(361, 301, 420, 360, fill='white')
mazeBlock57 = mazeCanvas.create_rectangle(421, 301, 480, 360, fill='white')
mazeBlock58 = mazeCanvas.create_rectangle(481, 301, 540, 360, fill='white')
mazeBlock59 = mazeCanvas.create_rectangle(541, 301, 600, 360, fill='white')
# ROW 7
mazeBlock60 = mazeCanvas.create_rectangle(0, 361, 60, 420, fill='white')
mazeBlock61 = mazeCanvas.create_rectangle(61, 361, 120, 420, fill='white')
mazeBlock62 = mazeCanvas.create_rectangle(121, 361, 180, 420, fill='white')
mazeBlock63 = mazeCanvas.create_rectangle(181, 361, 240, 420, fill='white')
mazeBlock64 = mazeCanvas.create_rectangle(241, 361, 300, 420, fill='white')
mazeBlock65 = mazeCanvas.create_rectangle(301, 361, 360, 420, fill='white')
mazeBlock66 = mazeCanvas.create_rectangle(361, 361, 420, 420, fill='white')
mazeBlock67 = mazeCanvas.create_rectangle(421, 361, 480, 420, fill='white')
mazeBlock68 = mazeCanvas.create_rectangle(481, 361, 540, 420, fill='white')
mazeBlock69 = mazeCanvas.create_rectangle(541, 361, 600, 420, fill='white')
# ROW 8
mazeBlock70 = mazeCanvas.create_rectangle(0, 421, 60, 480, fill='white')
mazeBlock71 = mazeCanvas.create_rectangle(61, 421, 120, 480, fill='white')
mazeBlock72 = mazeCanvas.create_rectangle(121, 421, 180, 480, fill='white')
mazeBlock73 = mazeCanvas.create_rectangle(181, 421, 240, 480, fill='white')
mazeBlock74 = mazeCanvas.create_rectangle(241, 421, 300, 480, fill='white')
mazeBlock75 = mazeCanvas.create_rectangle(301, 421, 360, 480, fill='white')
mazeBlock76 = mazeCanvas.create_rectangle(361, 421, 420, 480, fill='white')
mazeBlock77 = mazeCanvas.create_rectangle(421, 421, 480, 480, fill='white')
mazeBlock78 = mazeCanvas.create_rectangle(481, 421, 540, 480, fill='white')
mazeBlock79 = mazeCanvas.create_rectangle(541, 421, 600, 480, fill='white')
# ROW 9
mazeBlock80 = mazeCanvas.create_rectangle(0, 481, 60, 540, fill='white')
mazeBlock81 = mazeCanvas.create_rectangle(61, 481, 120, 540, fill='white')
mazeBlock82 = mazeCanvas.create_rectangle(121, 481, 180, 540, fill='white')
mazeBlock83 = mazeCanvas.create_rectangle(181, 481, 240, 540, fill='white')
mazeBlock84 = mazeCanvas.create_rectangle(241, 481, 300, 540, fill='white')
mazeBlock85 = mazeCanvas.create_rectangle(301, 481, 360, 540, fill='white')
mazeBlock86 = mazeCanvas.create_rectangle(361, 481, 420, 540, fill='white')
mazeBlock87 = mazeCanvas.create_rectangle(421, 481, 480, 540, fill='white')
mazeBlock88 = mazeCanvas.create_rectangle(481, 481, 540, 540, fill='white')
mazeBlock89 = mazeCanvas.create_rectangle(541, 481, 600, 540, fill='white')
# ROW 10
mazeBlock90 = mazeCanvas.create_rectangle(0, 541, 60, 600, fill='white')
mazeBlock91 = mazeCanvas.create_rectangle(61, 541, 120, 600, fill='white')
mazeBlock92 = mazeCanvas.create_rectangle(121, 541, 180, 600, fill='white')
mazeBlock93 = mazeCanvas.create_rectangle(181, 541, 240, 600, fill='white')
mazeBlock94 = mazeCanvas.create_rectangle(241, 541, 300, 600, fill='white')
mazeBlock95 = mazeCanvas.create_rectangle(301, 541, 360, 600, fill='white')
mazeBlock96 = mazeCanvas.create_rectangle(361, 541, 420, 600, fill='white')
mazeBlock97 = mazeCanvas.create_rectangle(421, 541, 480, 600, fill='white')
mazeBlock98 = mazeCanvas.create_rectangle(481, 541, 540, 600, fill='white')
mazeBlock99 = mazeCanvas.create_rectangle(541, 541, 600, 600, fill='white')

mazeCanvas.itemconfig(mazeBlock34, fill='black')

currBlockIndex = 0
for i in range(10):
    for j in range(10):
        blockId = "mazeBlock" + str(currBlockIndex)
        print(blockId)
        mazeCanvas.itemconfig(mazeBlock, fill='black')
        currBlockIndex += 1


# Create a Button to Disable the Combobox Widget
# ttk.Button(win, text="Change Color", command=change_color).pack()
win.mainloop()