#Write a Python program to calculate the area of regular polygon.
import math

num_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

print(f"The area of the polygon is: {area}")

#area = (n*s^2)/4*tan(pi/n)
#output: 
#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625