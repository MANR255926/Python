#variable and print example
#This script demonstrates variable declaration and printing in Python

name = "allyan"
age = 20
height = 5.2
bol = False
NON = None
num = int("10")  # converting string to integer

print("\n")

# Printing variables
print ("Variable values:")
print ("Name:", name)
print ("Age:", age)
print ("Height:", height)
print ("sum:", 23 + 25)
print ("bol:", bol)
print ("NON:", NON)
print (not False)#it will print True
print (not True)#it will print False
print ("sum of age & height by type casting:", age + height)
print ("sum of age & num by type casting:", age + num)

print("\n")

# Type of variables
print ("Variable types:")
print (type(name))
print (type(age))
print (type(height))
print (type(bol))
print (type(NON))

print("\n")

#input from user
print ("update your name ")
name = input("Enter your name: ")
print ("Updated Name: ", name)
#input function always save input as string
#for example if we enter 20 it will save as string not integer
num = input("Enter a number: ")
print ("Updated num:", num)
print ("Type of updated num:", type(num))
# to convert string to any other type we can use type casting
num = int(input(num))
print ("\n", type(num))