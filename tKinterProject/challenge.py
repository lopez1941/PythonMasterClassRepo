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

import tkinter

# title our gui app window
calcWindow = tkinter.Tk()
calcWindow.title("Calculator")

# sizing the tk window
calcWindow.geometry('250x350+50+100')
calcWindow['padx'] = 12
#calcWindow['pady'] = 8

# config the columns, i think it's 5, but we'll see
for i in range(0, 6):
    calcWindow.columnconfigure(i, weight=1000)

# config the rows, i think it's 7, but we'll see
for i in range(0, 7):
    calcWindow.rowconfigure(i, weight=50)

# output window
outputWindow = tkinter.Entry(calcWindow)
outputWindow.grid(row=0, column=0, columnspan=5, sticky='nsew')

# make some buttons
buttons = []  # going to store the buttons in a list
button_Text = ['C', 'CE', '7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', '*', '0', '=', '/']
for item in button_Text:
    item = tkinter.Button(calcWindow, text=item)
    buttons.append(item)

# row 1 C and CE
i = button_Text.index('C')
for x in range(0, 2):
    buttons[i].grid(row=1, column=x, sticky='nsew')
    i += 1

# row 2, 7 8 9 +
i = button_Text.index('7')
for x in range(0, 4):
    buttons[i].grid(row=2, column=x, sticky='nsew')
    i += 1

# row 3
i = button_Text.index('4')
for x in range(0, 4):
    buttons[i].grid(row=3, column=x, sticky='nsew')
    i += 1

# row 4
i = button_Text.index('1')
for x in range(0, 4):
    buttons[i].grid(row=4, column=x, sticky='nsew')
    i += 1

# row 5
i = button_Text.index('0')
for x in range(0, 3):
    if i == 15:
        buttons[i].grid(row=5, column=x, columnspan=2, sticky='nsew')
        x += 2
        i += 1
    if i == 16:
        buttons[i].grid(row=5, column=3, sticky='nsew')
    else:
        buttons[i].grid(row=5, column=x, sticky='nsew')
        i += 1

calcWindow.minsize(250,350)

calcWindow.mainloop()