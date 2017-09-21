import tkinter

# title our gui app window
calcWindow = tkinter.Tk()
calcWindow.title("Calculator")

# sizing the tk window
calcWindow.geometry('250x350+50+100')
calcWindow['padx'] = 12 # putting a little space on the left

# config the columns, i think it's 5, but we'll see
for i in range(0, 6):
    calcWindow.columnconfigure(i, weight=1000)

# config the rows, i think it's 7, but we'll see, adding weights here so that when resizing it doesn't look too goofy
for i in range(0, 7):
    calcWindow.rowconfigure(i, weight=50)

# output window
outputWindow = tkinter.Entry(calcWindow)
outputWindow.grid(row=0, column=0, columnspan=5, sticky='nsew')

# make some buttons
buttons = []  # going to store the buttons in a list
button_Text = {1: ['C', 'CE'],
               2: ['7', '8', '9', '+'],
               3: ['4', '5', '6', '-'],
               4: ['1', '2', '3', '*'],
               5: ['0', '=', '/']}

for key in button_Text:
    col = 0
    for click in button_Text[key]:
        if click == '=':
            tkinter.Button(calcWindow, text=click).grid(row=key, column=col, columnspan=2, sticky='nsew')
            col +=2
            continue
        tkinter.Button(calcWindow, text=click).grid(row=key, column=col, sticky='nsew')
        col += 1


calcWindow.minsize(250, 350)
calcWindow.maxsize(350, 450)
calcWindow.update_idletasks()
calcWindow.mainloop()