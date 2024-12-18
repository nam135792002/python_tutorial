# Exaple 01: 
word = "APPLE"

letter = input("Guess a letter in the secret word: ")
if letter not in word:
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

# Example 02:
students = {"Nguyen", "Phuong", "Nam"}
student = input("Enter the name of a student: ")

if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

# Example 03:
grades = {"Nguyen": "A",
          "Phuong": "B",
          "Nam": "C",
          "Ri": "B"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades.get(student)}")
else:
    print(f"{student} was not found")

# Example 04:
email = "phuongnama32112002@gmail.com"
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
