import time

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years ago!")
    print("Happy birthday to you!")
    print()
    
happy_birthday("Nam", 23)
happy_birthday("Phuong", 25)
happy_birthday("Nguyen", 48)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("Ri Nguyen", 42.50, "21/01")

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(3, 10))
print(divide(10, 5))

def create_name(first: str, last: str) -> str:
    first = first.strip().title()
    last = last.strip().title()
    return f"{first} {last}"

full_name = create_name("  nam   ", "   nguyen phuong      ")
print(full_name)

# Default arguments
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1, 0))

def count(end, start = 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")
    
count(10)

# Keyword arguments
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")
    
hello("Hello", title="Mr.", last="Ri", first="Nguyen")

# Keyword arguments
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=455, last=7890)
print(phone_num)

# *args & **kwargs
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")
        
display_name("Dr.", "Nguyen", "Phuong", "Nam")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="Nguyen Gia Tri St", city="Ho Chi Minh City",
              state="Binh Thanh District", zip="7701235")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    if "apt" in kwargs:
        print(f"{kwargs.get("street")} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get("street")}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")

shipping_label("Dr.", "Nguyen", "Phuong", "Nam",
               street="Nguyen Gia Tri St", apt="100",
               city="Ho Chi Minh City", state="Binh Thanh District", 
               zip="770124")

