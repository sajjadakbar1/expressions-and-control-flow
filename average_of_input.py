# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

# creating an empty list
lst = []
  
# number of elements as input
n = int(input("Enter total numbers you want: "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    lst.append(ele) # adding the element
      
# start parameter is not provided
Sum = str(sum(lst))
print("You entered numbers: "+str(lst))
print('\n'"Sum of your entered numbers are: "+Sum)

# To get average of a list
def Average(lst):
    return sum(lst) / len(lst)
 
# Driver Code
average = Average(lst)
 
# Printing average of the list
print("Average of your entered numbers is: ", round(average, 2))