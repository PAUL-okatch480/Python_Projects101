#A test into maths operators
#finding the circumference and area of a circle
import math
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"The circumference of the circle with radius {radius} is: {round(circumference, 2)} cm")
print(f"The area of the circle with radius {radius} is: {round(area, 2)} cm²")

#Finding the longest side of a right angeled triangle using Pythagoras theorem
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
hypotenuse = math.sqrt(pow(base, 2) + pow(height, 2))
print(f"The hypotenuse of the triangle with base {base} and height {height} is: {round(hypotenuse, 2)} cm")