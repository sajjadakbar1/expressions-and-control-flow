# Write a program that asks for an integer that is a distance in miles,
# then it converts that value to kilometers and prints it

distance = input("Please enter the distance in miles: ")
miles_to_km = str(1.61)
distance_in_km = int(distance * miles_to_km)
print("Total distance into kilometers in " + str(distance_in_km) +" miles.")