# Write a program that stores a number and the user has to figure it out
# The user can input guesses
# After each guess the program would tell one of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

import random
n = random.randrange(1,10)
guess = int(input("Guess your number: "))
while n!= guess:
    if guess < n:
        print("The stored number is lower")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("The stored number is higher")
        guess = int(input("Enter number again: "))
    else: break
    print('\n'"You found the number: " +str(n))