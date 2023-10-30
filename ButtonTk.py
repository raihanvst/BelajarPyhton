import tkinter as tk

r = tk.Tk()
r.title('Membuat button close')
button = tk.Button(r, text='stop', width=25, command=r.destroy)
button.pack()
r.mainloop()