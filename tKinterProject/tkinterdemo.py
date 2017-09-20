# allows for gui apps
# part of the standard library, so no extra installs needed
# documentation kind of sucks

try:
    import tkinter
# for python 2, the tkinter module is 'Tkinter' not 'tkinter'.  so,
# this tries for the version 3 module, and the exception covers if
# that fails and imports the python 2 module with the name tkinter
except ImportError:
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# tkinter._test()

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")  # title text for the entire window
mainWindow.geometry('640x480+8+400')  # size of window being opened, note that geometry takes a string not an int

label = tkinter.Label(mainWindow, text="Hello World!")  # text inside the window
label.pack(side='top')  # tells it to put the label text on the top portion

# this is creating a raised rectangle in the main window and orienting it to the left
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)  # passing mainWindow
# canvas.pack(side='top')  # adds it to the canvas on the left hand side of the window
# canvas.pack(side='left', fill=tkinter.Y)  # tkinter.Y expands the canvas vertically to have all available space
# canvas.pack(side='left', fill=tkinter.X, expand=True)  # tkinter.X, expand=True expands the canvas horizontally
# #  to have all available space. expand=True is needed in different scenarios- if side=x, fill=tkinter.X,
# # then you wouldn't need the expand section but you would need it for tkinter.Y
# canvas.pack(side='top', fill=tkinter.BOTH, expand=True)


# new frame to test
leftFrame = tkinter.Frame(mainWindow)  # creates a new frame in the mainWindows
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)  # passing leftFrame
canvas.pack(side='left', anchor='n')

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)

#create some buttons
# button1 = tkinter.Button(mainWindow, text="button1") # create a button, button1, in the mainWindow, with button1 as the text
# button2 = tkinter.Button(mainWindow, text="button2")
# button3 = tkinter.Button(mainWindow, text="button3")

button1 = tkinter.Button(rightFrame, text="button1") # create a button, button1, in the mainWindow, with button1 as the text
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")


# put the button in the window, oriented left
# note that when widgets share the same side, they're placed adjacent to each other in the order they were packed
# button1.pack(side='left')
# button2.pack(side='left')
# button3.pack(side='left')

# you can 'anchor' the buttons using n, s, e, w to further orient them
# this is dependent on which side you pack them as to how they actually get situated.  if you pack on the left,
# you'll get a different result than if you pack on top. if you pack top or bottom, only the horizontal position will
# be changed by anchor. if you pack left/right, only the vertical position will be affected by anchor
# pack is only suitable for very simple layouts as a result
# button1.pack(side='top', anchor='n')
# button2.pack(side='top', anchor='s')
# button3.pack(side='top', anchor='e')

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')


mainWindow.mainloop()  # pass control to tkinter so it can take over and make the window
