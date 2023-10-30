from tkinter import *

root = Tk()
menu = Menu(root)

root.config(menu=menu)
filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu =Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

viewmenu = Menu(menu)
menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='ToolWindows')
viewmenu.add_command(label='Apprearance')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Type Definition')
viewmenu.add_command(label='Parameter Info')
viewmenu.add_command(label='Type Info')
viewmenu.add_command(label='Contect Info')
viewmenu.add_separator()
viewmenu.add_command(label='Recent Files')
viewmenu.add_command(label='Recently Changed Files')
viewmenu.add_command(label='Recent Location')
viewmenu.add_command(label='Recent Changes')
viewmenu.add_separator()
viewmenu.add_command(label='Compare With...')
viewmenu.add_command(label='Compare With Clipboard')
viewmenu.add_separator()
viewmenu.add_command(label='Quick Switch Scheme...')
viewmenu.add_command(label='Active Editor')
viewmenu.add_separator()
viewmenu.add_command(label='Increase Font Size in All Editors')
viewmenu.add_command(label='Decrease Font Size in All Editors')
viewmenu.add_command(label='Reset Font Size')






mainloop()



