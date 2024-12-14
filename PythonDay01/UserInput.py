my_name = str(input("What is your name?: "))
my_age = int(input("How old are you?: "))
my_age += 1

print(f"Hello {my_name}!")
print(f"I am {my_age} years ago.")

# Exercise 01: Rectangle Area Cals

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f"The area is: {area}cm²")

# Exercise 02: Shopping Cart Program
item = input("What item would you like to buy?: ")
price = int(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Your total is: {total}")