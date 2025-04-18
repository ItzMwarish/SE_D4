# File Read & Write Challenge 🖋️: 
# Create a program that reads a file and 
# writes a modified version to a new file.
# Error Handling Lab 🧪: 
# Ask the user for a filename and 
# handle errors if it doesn’t exist or can’t be read.


filename = input("Enter the filename to read: ")
try:
    with open(filename, 'r') as file:
        fileContent = file.read()
        print("File content:")
        print(fileContent)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")  