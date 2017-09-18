# open, read, close
# open the file, and in what mode
# windows: C:\\path\\to\\the\\file\\sample.txt

# jabber = open("/home/dlopez/Desktop/sample.txt", 'r')  #open in read only with 'r'
# jabber = open("sample.txt", 'r')  # in the root folder of the project
# for line in jabber:  # python treats teh lines of the file like a list
#     if "jabberwock" in line.lower():  # compares lowercase to lowercase
#         print(line, end='')
#
# jabber.close()  # keeps from file corruption

# with takes care of closing the file for us
# it also takes care of error handling
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:  # as long as it's not an empty line, the while loop will run.
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", 'r') as jabber:
#     lines = jabber.readlines()  # converts to a list, useful for debuging
# print(lines)
#
# for line in lines:
#     print(line, end='')  # end='' gets rid of the newline character

with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()  # converts to a list of strings, useful for debuging
print(lines)

for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)

for line in lines[::-1]:
    print(line, end='')

# readline reads a single line from a file and returns a string
# readlines reads the entire file and returns a list of strings
# read- reads the entire file and returns a string containing the contents if a text file