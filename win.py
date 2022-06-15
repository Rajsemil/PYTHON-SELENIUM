from tkinter import *
win = Tk()
win.title("Styless Notepad")

MyMenu=Menu(win)
MyMenu.add_cascade(label='File')
win.config(Mene=MyMenu)

win.mainloop()