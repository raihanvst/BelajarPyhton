from tkinter import *
layout = Tk()
v = IntVar()

Radiobutton(layout, text='Male',variable = v,value=1).pack(anchor=CENTER)
Radiobutton(layout, text='Female',variable = v,value=2).pack(anchor=CENTER)
mainloop()

