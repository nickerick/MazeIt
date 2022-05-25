from tkinter import *

from matplotlib.pyplot import text

ws = Tk()
# ws.geometry('400x300')
# ws.attributes('-zoomed', True)
ws.state("zoomed")
ws.title('Maze Solver')
ws['bg']='#5a5f69'

f = ("Times bold", 14)
f2 = ("Times bold", 34)

def prevPage():
    homeScreen["text"] = "new text"
    
homeScreen = Label(
    ws,
    text="Solv-a-Maze",
    bg=ws["bg"],
    font=f2,
    pady=50
)
homeScreen.pack(expand=False, fill=BOTH)

b = Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=lambda: [b.pack_forget(), homeScreen.pack_forget()],
    )
b.pack(side=TOP)

ws.mainloop()