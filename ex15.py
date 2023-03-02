# imports the argv object from the sys module
from sys import argv

# unpacks the script name and first argument from argv
script, filename = argv

# opens the file by name and saves it to txt
txt = open(filename)

# prints the filename
print(f"Here's your file {filename}:")
# prints the contents of the txt file
print(txt.read())
# close the file
txt.close()

# asks for the user's input to get the filename again
print("Type the filename again:")
# saves the user's input as file_again
file_again = input("> ")

# opens the file based on the user's input
txt_again = open(file_again)

# prints the contents of the file again
print(txt_again.read())

# close the file
txt_again.close()
