import tkinter as tk # Python 3.x Version
#import Tkinter as tk # Python 2.x Version

root = tk.Tk()

label = tk.Label(root, text="Hello World!") # Create a text label
label.pack(padx=20, pady=20) # Pack it into the window

solveButton = tk.Button(root, text="Solve Maze!")
solveButton.pack(padx=20, pady=20)

root.mainloop()