# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

h = int(input("Enter Diamond height: "))

for s in range(h):
    print(" " * (h - s), "*" * (s * 2 + 1))

for s in range(h - 2, -1, -1):
    print(" " * (h - s), "*" * (s * 2 + 1))