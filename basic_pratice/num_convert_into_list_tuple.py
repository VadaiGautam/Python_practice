'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.'''


# user_input = input("Enter the number and separated by commas")

# print(user_input)

# lisst = user_input.split(" , ")

# tuplee = tuple(lisst)

# print(f"In the list format = {lisst} \nIn the tuple format = {tuplee}")

# Prompt the user to input a sequence of comma-separated numbers and store it in the 'values' variable
values = input("Input some comma-separated numbers: ")

# Split the 'values' string into a list using commas as separators and store it in the 'list' variable
list = values.split(",")

# Convert the 'list' into a tuple and store it in the 'tuple' variable
tuple = tuple(list)

# Print the list
print('List : ', list)

# Print the tuple
print('Tuple : ', tuple)