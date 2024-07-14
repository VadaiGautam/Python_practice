'''Write a Python program that accepts a filename from the user and prints the extension of the file.'''

filename = input("Enter the filename: ")

c = filename.split('.')

print(c[1])
    
        