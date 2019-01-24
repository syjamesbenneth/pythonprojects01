from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title","This is a message")

response = tkinter.messagebox.askquestion("Question 1", "Do you like coffee?")

if response == 'yes':
    print("Here is some coffee for you")

root.mainloop()