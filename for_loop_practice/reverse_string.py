'''Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.'''


user_name = input("enter the name - ")

print(f"name is - {user_name}")

length = len(user_name)

print(f"length is {length}")

print(f"Reverse the string")

v = 1
for i in user_name:
    

    
    ans = length-v
    v = v+1
    print(user_name[ans],end=" ")
   

