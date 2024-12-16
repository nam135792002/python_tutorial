menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("-" * 10 + " MENU " + "-" * 10)
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-" * 28)

while True:
    food = input("Select a item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
   
print("-" * 10 + " YOUR ORDER " + "-" * 10)     
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Total is: ${total:.2f}")
