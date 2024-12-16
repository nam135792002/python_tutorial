# name = input("Enter your full name: ")
# phone_number = input("Enter your phone: ")

# result = name.find("N")
# result = name.rfind("Na")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# result = phone_number.replace("-"," ")

# print(result)

# Exercise 01:
# username = input("Enter a username: ")

# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}!")

# Exercise 02:
# credit_number = "1234-5678-9012-3456"

# print(credit_number[0:4])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# print(credit_number[::-1])

# Exercise 03:
price1 = 3000.14159
price2 = -9780.65
price3 = 1200.34

print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}")
print(f"Price 3 is {price3:+,.3f}")
