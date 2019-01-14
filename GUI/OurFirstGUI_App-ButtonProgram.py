# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("500x500")

def helloCallBack():
   msg=messagebox.showinfo( "HOME", "Welcome to Python GUI")


B = Button(top, text ="CLICK TO LOGIN", command = helloCallBack)

B.place(x=30,y=30)

top.mainloop()

"""
	1. Import the Tkinter module.

	2. Create the GUI application main window.

	3. Add one or more of the above-mentioned widgets to the GUI application.

	4. Enter the main event loop to take action against each event triggered by the user.
"""
