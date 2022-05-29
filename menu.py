from tkinter import * 
from tkinter.ttk import *

def menu():
    root = Tk()

    root.geometry("800x500")


    #large text box for input
    textHere = Text (root) 
    textHere.place(x = 10, y = 10, width = 480, height = 380)

    #import button
    importButton = Button (root)
    importButton(text="import").place(y=10, x=510, width = 150, height = 40)


    #consol text box
    console = Text (root)
    console.place( x  = 510, y = 60, width = 280, height = 330)


    root.mainloop()