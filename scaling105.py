#2D lists
vegetables=["Carrot", "Potato", "Tomato"]
fruits=["Apple", "Banana", "Mango"]
meats=["Chicken", "Beef", "Pork"]

collections = [["Carrot", "Potato", "Tomato"],
                ["Apple", "Banana", "Mango"],
                  ["Chicken", "Beef", "Pork"]]
for collection in collections:
    for collection_item in collection:
        print(collection_item, end=" ")
    print()  # Move to the next line after each collection
#a telephone number pad
number_pad = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             ["*", 0, "#"]]
for number in number_pad:
    for num in number:
        print(num, end=" ")
    print()  # Move to the next line after each row
print("The number pad is a display of numbers and symbols arranged in a grid format.")
print("It is commonly used for dialing phone numbers or entering numerical data.")

#A pyhon quiz game
questions=("What is the capital of France?",
           "What is the largest planet in our solar system?",
           "What is the chemical symbol for gold?",
           "What is the square root of 64?",
           "What is the currency of Japan?")
options=(("A) London", "B) Paris", "C) Berlin", "D) Rome"),
         ("A) Mars", "B) Venus", "C) Jupiter", "D) Neptune"),
         ("A) Ag", "B) Au", "C) Fe", "D) Cu"),
         ("A) 8", "B) 16", "C) 32", "D) 64"),
         ("A) Yuan", "B) Yen", "C) Won", "D) Ruble"))
answers=("B", "C", "B", "A", "B")
guesses=[]
score=0
question_number=0
for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_number]:
        print(option)
    guess=input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is: {answers[question_number]}")

    question_number+= 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("******************** RESULTS ********************")
print("Answers: ", end="")
for answer in answers:
    print(answer, end="")
print()  # Move to the next line after printing all answers
print("\nGuesses: ", end="")
for guess in guess:
    print(guess, end="")
print()  # Move to the next line after printing all guesses

score=int((score/len(questions))*100)
print(f"Your score is :{score}%")
if score >= 80:
    print("Congratulations! You passed the quiz.")
else:
    print("Sorry, you did not pass the quiz. Better luck next time!")
    print("Thank you for playing the quiz game. Goodbye!")
