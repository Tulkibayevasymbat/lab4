#Write a Python program to calculate the area of a trapezoid.

height = float(input("height: "))
first_value = float(input("Base, first value: "))
second_value = float(input("Base, second value: "))

# трапеция формула
area = 0.5 * (first_value + second_value) * height

print(f"Expected Output: {area}")

#output:
#height: 5
#first value: 5
#second value: 6
#Expected Output: 27.5