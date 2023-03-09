# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

a = input("Enter first number: ")
b = input("Enter second number: ")

if a < b: print("The second number should be bigger"'\n'+a+'\n'+b)
else: a > b
c = int(b) + 1
print(str(c))