# File handling is an important part of any web application.

# File Handling

# The key function for working with files in Python is the open() function.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# To open a file for reading it is enough to specify the name of the file:

# f = open('demofile.txt', 'rt')
# g = open('demofile.txt') #"r" for read, and "t" for text are the default values, you do not need to specify them.

# # The open() function returns a file object, which has a read() method for reading the content of the file:

# print(f.read())
# print()

# If the file is located in a different location, you will have to specify the file path
# f = open("D:\\myfiles\welcome.txt", "r")

# Read Only Parts of the File
# # By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# print(g.read(5))
# print()

# # You can return one line by using the readline() method:
# z = open('demofile.txt', 'rt')
# print(z.readline())
# print()

# # By looping through the lines of the file, you can read the whole file, 
# # line by line:

# y = open('demofile.txt', 'r')
# for line in y:
#     print(line)
# print()
# # Close Files
# It is a good practice to always close the file when you are done with it.

# w = open('demofile.txt', 'r')
# print(w.readline())
# w.close()
# print()
# print()

# Note: You should always close your files, in some cases, due to buffering, 
# changes made to a file may not show until you close the file.

# Write to an Existing File

# to write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# w = open('demofile.txt', 'a')
# w.write('\nNow the file has more content')
# w.close()
#open and read the file after the appending:
# w = open('demofile.txt', 'r')
# print(w.read())
# w.close()


f = open('demofile2.txt', 'a')
f.write('\nNow the file has more content')
f.close()
# f.read()

w = open('demofile2.txt', 'r')
print(w.read())
w.close()
# f.close()

# Open the file "demofile3.txt" and overwrite the content:

b = open('demofile3.txt', 'w')  #he "w" method will overwrite the entire file.
b.write('\nwoops!i have deleted the content')
b.close()

a = open('demofile3.txt', 'r')
print(a.read())
a.close()

# Create a New File

# to create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist


# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt":

c = open('myfile.txt', 'x')
# Result: a new empty file is created

# Create a new file if it does not exist:
d = open('myfile.txt', 'w')

# Python Delete File

# Delete a File

# To delete a file, you must import the OS module, and run its os.remove() 
# function:

import os

# os.remove('myfile.txt')

# Check if File exist:

# To avoid getting an error, you might want to check if the file exists 
# before you try to delete it:

# Check if file exists, then delete it:

if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('file does not exist.')

# Delete Folder

# To delete an entire folder, use the os.rmdir() method:

os.rmdir('myfolder')

# Note:You can only remove empty folders
