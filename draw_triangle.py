# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

a = int(input("Enter number of rows: "))
for b in range(0,a):
    for c in range(0, b+1):
        print('*', end=' ')
    print('\r')