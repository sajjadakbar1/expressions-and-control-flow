# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

row = int(input("Enter number of rows: "))
b = 0
for s in range(1, row + 1):
    for space in range(1, (row - s)+1):
        print(end = "  ")
 
    while b!= (2*s - 1):
        print("* ", end="")
        b += 1   
    b = 0
    print()