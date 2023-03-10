massInKg = 81.2
heightInM = 1.78

#Print the Body mass index (BMI) based on these values

# Input from the users  
weight = float(input("Enter you Weight: "));
height = float(input("Enter you Height in meters: "));
print("Your Body Mass Index (BMI) is: ", round(weight / (height * height), 2))