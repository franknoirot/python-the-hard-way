# import the sys module to operate on files
from sys import argv

# destructure the arguments passed into the script
script, input_file = argv

# a callable function to print the entire contents of a file
def print_all(f):
    print(f.read())

# a callable function to rewind the read head back to the beginning of a file
def rewind(f):
    f.seek(0)

# a callable function to write any one line of a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Opening the file name passed in on the command line
current_file = open(input_file)

print("First let's print the whole file:\n")

# printing the passed-in file's contents
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewinding the read head to the top of the file
rewind(current_file)

print("Let's print three lines:")

# Stepping through and printing each of the first 3 lines
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)