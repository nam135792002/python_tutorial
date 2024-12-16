# fruit = ["apple", "orange", "banana", "coconut"]

# # print(fruit[::-1])

# # for x in fruit:
# #     print(x)
    
# # print(len(fruit))

# print(fruit)

# fruit[0] = "ri"
# print(fruit)

# fruit.append("nguyen")
# print(fruit)

# fruit.remove("ri")
# print(fruit)

# fruit.insert(1, "ri")
# print(fruit)

# fruit.sort()
# print(fruit)

# fruit.reverse()
# print(fruit)

# print(fruit.index("coconut"))

# fruit[1] = "coconut"
# print(fruit.count("coconut"))

# fruit.clear()
# print(fruit)

# Exercise 01: Shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q/Q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = int(input(f"Enter the price of a {food}: "))
#         foods.append(food)
#         prices.append(price)
        
# print("----- YOUR CART -----")

# for food in foods:
#     print(food)

# for price in prices:
#     total += price

# print(f"Your total is {total}VND")

# Exercise 02: 2D Collections
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[0][0])
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
