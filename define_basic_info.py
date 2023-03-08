# Define several things as a variable then print their values
# Your name as a string
# Your age as an integer
# Your height in meters as a float
# Whether you are married or not as a boolean

a = input("What is your name? ")
b = input("What is your age? ")
c = input("What is your height? ")

print(a)
print(int(b))
print(float(c))

martial_status = input("Are you married? ")
if martial_status == ("yes"): print("You are married.")
else: print(martial_status+" "+ "You are unmarried.")
