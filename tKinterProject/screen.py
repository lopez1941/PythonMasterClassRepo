try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")  # title text for the entire window
# mainWindow.geometry('640x480+8+200')  # size of window being opened, note that geometry takes a string not an int
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text='TKinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)  # put 'label' in row 0 column 0, but span it across 3 columns

# making a 5x5 grid inside our 'mainWindow'
# column size is based on the size of the widget.  the weight property really comes into play when a window is resized.
# a weight of 3 will resize 3 times faster than 1
# when placing widgets in the same cell, give the row or column a low weighting
# give titles low weight so that when resizing vertically it doesn't look goofy
mainWindow.columnconfigure(0, weight=100)  # actually creating the columns
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)  # creating and putting meat on the bones of the rows
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for zone in os.listdir('/Windows/System32'):
# for zone in os.listdir('/usr/bin'):  # for windows it would be /Windows/System32 instead of /usr/bin
    # insert commands in /usr/bin into our fileList
    fileList.insert(tkinter.END, zone)  # END places each item at the end of the list
# command
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)  # create a scroll bar
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)  # adding to the grid
fileList['yscrollcommand'] =listScroll.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')  # labelframe adds caption and border around the frame
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()  # create radio button space
rbValue.set(1)  # set- sets the default value
radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)  # 1st button
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)  # button 2, etc
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
# add radio buttons to the grid
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget displaying the result
resultLabel = tkinter.Label(mainWindow, text="Result")  # creates a label for the result field
resultLabel.grid(row=2, column=2, sticky='nw')  # puts the result in row2, column2, oriented nw
result = tkinter.Entry(mainWindow)  # creates a result field
result.grid(row=2, column=2, sticky='sw')

# frame for the spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# time spinners, spinbox is up/down arrows, run it, you'll see
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)  # by using from_ instead of a range, you don't have to remember to add an extra number
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)  # use this 'from_' way instead of a range, i like this better
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)  # add a label and grid it in one line
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)  # add a label and grid it in one line
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36  # padding the widget to move it over a little

#frame for date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# date labels for date frame
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# day spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",\
                                                      "Oct", "Nov", "Dec")) # using 'values' so we can specify the text
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
# adding spinners to the grid
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# ok and cancel buttons
okButton = tkinter.Button(mainWindow, text="Ok")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)  # remember no parenthesis after destroy, do not 'destroy()' just do destroy
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')



mainWindow.mainloop()

print(rbValue.get())  # retrieves the value of the button selected




