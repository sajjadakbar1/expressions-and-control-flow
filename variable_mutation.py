a = 3
# make the "a" variable's value bigger by 10
a = a + 9
print(a)

b = 100
# make b smaller by 7
b = b - 94
print(b)

c = 44
# please double c's value
c = c + c
print(c)

d = 125
# please divide by 5 d's value
d = d / 5
print(d)

e = 8
# please cube of e's value
e = e ** 3
print(e)

f1 = 123
f2 = 345
# tell if f1 is bigger than f2 (pras a boolean)
if f1 > f2: print("f1 > f2")
else: print("f2 > f1")

g1 = 350
g2 = 200
# tell if the double of g2 is bigger than g1 (pras a boolean)
g2 = g2 + g2
if g2 > g1: print("g2 > g1")
else: print("g2 > g1")

h = 1357988018575474
# tell if 11 is a divisor of h (pras a boolean)
                                        
list_1 = [13579880185754741357988018575474]

result = list (filter (lambda x: (x % 11 == 0), list_1))

print("Number that is divisible by 11: ", result)             

i1 = 10
i2 = 3
# tell if i1 is higher than i2 squared and smaller than i2 cubed (pras a boolean)

j = 1521
# tell if j is divisible by 3 or 5 (pras a boolean)
my_list = [1521]

result = list (filter (lambda x: (x % 3 or 5 == 0), my_list))

print("Number that is divisible by 3 OR 5: ", result)