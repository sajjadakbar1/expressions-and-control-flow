#  Create a function that takes two strings as a parameter
#  Returns the starting index where the second one is starting in the first one
#  Returns `-1` if the second string is not in the first one

# def substr(str, keyword):
#     return -1

# #  Example
# # should print: `17`
# print(substr("This is what I'm searching in", "searching"))

# # should print: `-1`
# print(substr("This is what I'm searching in", "not"))

def substr(str, keyword):
    if str == keyword:
        return -1
    else:
        for str, keyword in zip(str, keyword):
            if str != keyword:
                return str

str1 = input("Enter your first string: ")
str2 = input("Enter your second string: ")
print(substr(str1, str2))