# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

chickens = int(input("How many chickens you want: "))
cows = int(input("How many cows you want: "))
pigs = int(input("How many pigs you want: "))

print('\n'"All the animals you want have " +str(chickens*2 + cows*4 + pigs*4)+" legs.")