import math

friend = 10

friend = friend ** 2
print(friend)

remainder = friend % 3
print(remainder)

x = 3.14
y = -4
z = 5

result = round(x)
print(result)

result = abs(y)
print(result)

result = pow(4,3)
print(result)

result = max(x,y,z)
print(result)

print(math.pi)
print(math.e)

result = math.sqrt(x)
print(result)

t = 9.9
result = math.ceil(t)
result = math.floor(t)
print(result)

# Exercise 01:
radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

# Exercise 02:
radius = float(input('Enter the radius of a circle: '))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm²")

# Exercise 03:
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side c = {c}")
