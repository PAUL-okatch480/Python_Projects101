#A number guessing game using python
import random
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("****** Welcome to the Number Guessing Game! *****")
print(f"Think of a number between {lowest_number} and {highest_number}.")

while is_running:
    guess=input("Enter your guess: ")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess <lowest_number or guess > highest_number:
            print("Your guess is out of range.")
            print(f"Please enter a number between {lowest_number} and {highest_number}.")
        elif guess < answer:
            print("Your guess is too low. Try again!")
        elif guess > answer:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the correct number {answer} in {guesses} attempts.")
            is_running = False
    else:
        print("The Guess must be a number between 1 and 100.")
        guess=int(input("Please enter your guess: "))

#now we build a game of rock paper scissors in python
import random
options= ("rock", "paper", "scissors")
is_running=True
while is_running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win! Rock beats scissors.")
    elif player == "paper" and computer == "rock":
        print("You win! Paper beats rock.")
    elif player == "scissors" and computer == "paper":
        print("You win! Scissors beats paper.")
    else:
        print("You lose!")
    if not input ("Play again? (y/n): ").lower() == "y":
        is_running = False
print("Thanks for playing!")
print("Goodbye!")