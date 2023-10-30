from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'python')
Lb.insert(2, 'c++')
Lb.insert(3, 'JavaScript')
Lb.insert(4, 'php')
Lb.insert(5, 'Ruby')
Lb.insert(6, 'Perl')
Lb.pack()
top.mainloop()