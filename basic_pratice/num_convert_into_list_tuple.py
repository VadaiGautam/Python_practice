'''Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.'''


user_input = input("Enter the number and separated by commas")

print(user_input)

lisst = user_input.split(",")

tuplee = tuple(lisst)

print(f"list : {lisst}")

