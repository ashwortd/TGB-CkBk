from tkinter import *
win=Tk()
win.geometry("400x400")
b=Button(win,text="Submit")
b.pack()
label1=Label(win,text="hi, welcome to the jungle")
label1.pack()
c=Checkbutton(win,text = "We got what it takes")
c.pack()
c1=Checkbutton(win,text="Your mam don't dance")
c1.pack()
c2=Checkbutton(win,text="Forget about it")
c2.pack()
win.mainloop()
