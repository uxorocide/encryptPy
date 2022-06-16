from tkinter import * 
import tkinter.ttk as ttk
from tkinter.ttk import *
import main

def menu():
    root = Tk()

    root.geometry("800x430")


    #large text box for input
    textHere = Text (root) 
    textHere.place(x = 10, y = 10, width = 480, height = 380)

    #console text box
    console = Text (root)
    console.place( x  = 510, y = 60, width = 280, height = 330)

    #import button
    importButton = ttk.Button
    importButton(text="import").place(y=10, x=510, width = 100, height = 25)

    #export button
    exportButton = ttk.Button
    importButton(text="export").place(y=400, x=10, width = 100, height = 25)

    #start button
    startButton = ttk.Button
    importButton(text="start").place(y=400, x=580 , width = 100, height = 25)

    #stop button
    stopButton = ttk.Button
    importButton(text="stop").place(y=400, x=690, width = 100, height = 25)

    root.mainloop()

menu()