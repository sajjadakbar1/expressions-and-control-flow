# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

def volumeCuboid( l , h , w ):
    return (l * h * w)
      
def surfaceAreaCuboid( l , h , w ):
    return (2 * l * w + 2 * w * h + 2 * l * h)
  
# driver function
l = float(input("Enter length: "))
h = float(input("Enter height: "))
w = float(input("Enter width: "))

print("Volume =" , volumeCuboid(l, h, w))
print("Total Surface Area =", surfaceAreaCuboid(l, h, w))