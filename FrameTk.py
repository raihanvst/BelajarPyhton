from tkinter import *
root = Tk()

frame = Frame(root)
frame.pack()

buttonFrame= Frame(root)
buttonFrame.pack(side=BOTTOM)
redbutton= Button(frame,text='aku', fg= 'red')
redbutton.pack(side=LEFT)
greenbutton = Button(frame, text= 'haechan', fg='green')
greenbutton.pack(side=RIGHT)
brownbutton= Button(frame, text= 'suka', fg='brown')
brownbutton.pack(side=LEFT)
cyanbutton= Button(frame, text='si', fg='cyan')
cyanbutton.pack(side=RIGHT)
bluebutton = Button(frame, text='sama', fg='blue')
bluebutton.pack(side=LEFT)
mainloop()