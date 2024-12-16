import random

low = 1
hight = 100

# number = random.randint(low, hight)
# print(number)

# number = random.random();
# print(number)

# options = ("Nam", "Huy", "Vy", "Dieu", "Tra", "Hoa", "Tra")
# option = random.choice(options)
# print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
