from tkinter import *
win = Tk()
win.title("Styless Notepad")

btn = Button(win,text="File",bg="lightblue",height="2",width="6",bd=3).place(x=0,y=0)
btn = Button(win,text="Edit",bg="lightblue",height="2",width="6",bd=3).place(x=50,y=0)
btn = Button(win,text="Format",bg="lightblue",height="2",width="6",bd=3).place(x=100,y=0)
btn = Button(win,text="Help",bg="lightblue",height="2",width="6",bd=3).place(x=150,y=0)

win.mainloop()