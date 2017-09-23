# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import os
import tkinter

# title our gui app window
calcWindow = tkinter.Tk()
calcWindow.title("Calculator")

# sizing the tk window
calcWindow.geometry('220x300+50+100')
calcWindow['padx'] = 12

# config the columns, i think it's 5, but we'll see
for i in range(0, 6):
    calcWindow.columnconfigure(i)


# config the rows, i think it's 7, but we'll see
for i in range(0, 7):
    calcWindow.rowconfigure(i)

# output window
outputWindow = tkinter.Entry(calcWindow)
outputWindow.grid(row=0, column=0, columnspan=5, sticky='nw')

#  let's make a button frame
buttonFrame = tkinter.Frame(calcWindow)
buttonFrame.grid(row=1, column=0, sticky='nw')

# make some buttons
buttons = []  # going to store the buttons in a list
button_Text = ['C', 'CE', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '=', '/']
for item in button_Text:
    item = tkinter.Button(buttonFrame, text=item)
    buttons.append(item)


# add row 1 in to the button frame
x = button_Text.index('C')
for i in range(0, 2):
    buttons[x].grid(row=1, column=i, sticky='new')
    x += 1

# add row two to button frame
x = button_Text.index('7')
for i in range(0, 4):
    buttons[x].grid(row=2, column=i, sticky='new')
    x += 1

# add row three to button frame
x = button_Text.index('4')
for i in range(0, 4):
    buttons[x].grid(row=3, column=i, sticky='new')
    x += 1

# add row four to button frame
x = button_Text.index('1')
for i in range(0, 4):
    buttons[x].grid(row=4, column=i, sticky='new')
    x += 1

# add row five to button frame
x = button_Text.index('0')
for i in range(0, 3):
    if buttons[x] == buttons[15]:
        x += 1
        continue
    else:
        buttons[x].grid(row=5, column=i, sticky='new')
        x += 1
buttons[15].grid(row=5, column=1, columnspan=2, sticky='new')



calcWindow.mainloop()