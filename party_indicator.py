# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second represents the number of boys
#
# If the the number of girls and boys are equal and 20 or more people are coming to the party
# it should print: The party is excellent!
#
# If there are 20 or more people coming to the party but the girl - boy ratio is not 1-1
# it should print: Quite a cool party!
#
# If there are less people coming than 20
# it should print: Average party...
#
# If no girls are coming, regardless the count of the people
# it should print: Sausage party

boys = input("Enter the number of boys coming in the party? ")
girls = input("Enter the number of girls coming in the party? ")
people = input("Enter the number of people coming in the party? ")

boys = int(boys)
girls = int(girls)
people = int(people)
total = (boys + girls + people)
gay = int(boys + people)


if boys == girls and total > 20: print("The party is excellent!")
if total >= 20 and total > girls: print("Quite a cool party!")
if total < 20 and girls != 0: print("Average party...")
if girls == 0: print("Sausage party :-D")