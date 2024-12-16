# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ")
    
# print(f"Hello {name}")  

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to quit): ")
# print("bye")

# num = int(input("Enter a # between 1 - 10: "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10: "))
    
# print(f"Your number is {num}")

# Exercise 01: Compound interest caculator
principle = 0
while principle < 0:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")

rate = 0
while rate < 0:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")

time = 0
while time < 0:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
        
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")
        