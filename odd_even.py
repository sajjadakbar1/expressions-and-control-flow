# Write a program that reads a number from the standard input,
# then prints "Odd" if the number is odd, or "Even" if it is even.

a = int(input("Please enter your number: "))
if (a % 2) == 0:
   print("{0} is Even.".format(a))
else:
   print("{0} is Odd.".format(a))