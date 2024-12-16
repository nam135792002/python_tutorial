# Python quiz game
questions = ("Question 01: abc", "Question 02: def", 
             "Question 03: ghk", "Question 04: lmn",
             "Question 05: oix")

options = (("A. 1", "B. 2", "C. 3", "D. 4"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. 9", "B. 10", "C. 11", "D. 12"),
           ("A. 13", "B. 24", "C. 35", "D. 40"),
           ("A. 11", "B. 29", "C. 39", "D. 43"))

answers = ("A", "B", "C", "D", "B")

question_num = 0

guesses = []

score = 0

for question in questions:
    print("-"*30)
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ")
    guesses.append(guess.upper())
    if guess.upper() == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect! {answers[question_num]} is the correct answer")
    
    question_num += 1
    
print("-" * 20)
print(" " * 5 + "RESULTS" + " " * 5)
print("Answer: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
