# python functions

# def followed by name + () + :
def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# python_food()

# all python functions return a result, if none is given, it will return None
# print(python_food())

# basic idea of a function is to write a block of code once, and then call it whenever you need to
# in your program

def center_text(*args, sep=" ", end='\n', file=None, flush=False):  # parameter can be called anything, parameter- variables defined in the function definition
    # argument- the actual values used when the function is called
    # sometimes they're used interchangably, but there are differences
    # 'text' is the parameter of this function
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin, text
    # a function's signature refers to the parameters in a function definition.  if two functions
    # take the same parameters, then they have the same signature


# with open("centered", mode='w') as centered_file:
center_text("This is my text.")  # 'this is my text' is the argument passed to the function
center_text("Spam and Eggs")
center_text("spam, spam and eggs")
center_text("spam spam spam spam spam")
center_text(12)
center_text('12')
center_text("first", "second", 3, 4, "spam", sep=':')



