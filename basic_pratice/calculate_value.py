'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''

n = int(input("Enter the number = "))

# The placeholders %s are used to format the strings.

n1 = int("%s"%n)
n2 =int("%s%s"%(n,n))
n3 = int("%s%s%s"%(n,n,n))

print('the value of n+nn+nnn is = ',n1+n2+n3)



'''The said code prompts the user to input an integer, which is then stored in the variable "a".

There after the first variable n1 is created by converting the input integer "a" to a string and then back to an integer.

The second variable n2 is created by concatenating two copies of the input integer "a" as a string and then converting that string to an integer.

'''


