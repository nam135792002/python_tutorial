doubles_01 = []
for x in range(1, 11):
    doubles_01.append(x * 2)
print(doubles_01)
    
doubles_02 = [x * 2 for x in range(1, 11)]
print(doubles_02)

triples = [y * 3 for y in range(1, 11)]
print(triples)

squares = [z * z for z in range(1, 11)]
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit.upper() for fruit in fruits]
print(fruit_chars)

numbers = [1, 2, 3, -4, 5, -6]
positive_num = [num for num in numbers if num >= 0]
negative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]

print(positive_num)
print(negative_num)
print(even_num)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)
