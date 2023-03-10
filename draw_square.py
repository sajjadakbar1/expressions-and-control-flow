# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# The square should have as many lines as the number was

m, n = 10, 10
for i in range(m):
    for j in range(n):
        print('*' if i in [0, n-1] or j in [0, m-1] else ' ', end='')
    print()