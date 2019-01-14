# !/usr/bin/python3
from tkinter import *

root = Tk()

root.geometry("500x500")

var = StringVar()

label = Message(root, textvariable=var, relief=RAISED)

var.set("Hey!? How are you doing?")

label.pack()

root.mainloop()