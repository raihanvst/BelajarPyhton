from tkinter import*

master = Tk()
Label(master, text='Nama:').grid(row=0)
Label(master, text='Alamat:').grid(row=1)
box1 = Entry(master)
box2 = Entry(master)
box1.grid(row=0, column=1)
box2.grid(row=1, column=1)
mainloop()