#a deep dive into string nethods in Python
username = input("Enter your username: ")
if len(username) > 12:
    print("Error: Username must not exceed 12 characters long.")
elif not username.find(" ") == -1:
    print("Error: Username must not contain spaces.")

elif not username.isalpha():
    print("Error: Username must only contain letters.")

else:
    print(f"Welcome, {username}!")
    print("It is such an honour to have you on board.")
#while loops
name = input("Enter your name: ")
while name == "":
    print("Error: Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")

print(f"Hello, {name}! Welcome to the program.")
print("Thank you for providing your name. Let's continue with the program.")
age = int(input("Enter your age: "))
while age < 0:
    print("Error: Age cannot be negative. Please enter a valid age.")
    age = input("Enter your age: ")

print(f"Thank you, {name}. You are {age} years old.")

food = input("Enter your favorite food(Enter q to quit): ").lower()
while food != "q":
    if food == "":
        print("Error: Food cannot be empty. Please enter your favorite food.")
    else:
        print(f"Your favorite food is {food}.")
    food = input("Enter your favorite food(Enter q to quit): ").lower()
print("Thank you for sharing your favorite food. Goodbye!")

#A compound interest formula
principal = 0
rate =0
time =0

while True:
    try:
        principal = float(input("Enter the principal amount: "))
        if principal < 0:
            print("Error: Principal amount cannot be negative. Please enter a valid amount.")
            continue
        break
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the principal amount.")

while True:
    try:
        rate = float(input("Enter the annual interest rate (in percentage): "))
        if rate < 0:
            print("Error: Interest rate cannot be negative. Please enter a valid rate.")
            continue
        break
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the interest rate.")

while True:
    try:
        time = float(input("Enter the time in years: "))
        if time < 0:
            print("Error: Time cannot be negative. Please enter a valid time.")
            continue
        break
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value for the time.")

print("From the {principal} principal amount, at an annual interest rate of {rate}%, over a period of {time} years.")
print(f"The Total will be : {principal * (1 + rate / 100) ** time:.2f}")

import time
my_time = int(input("Enter the time in seconds: "))
for i in range(my_time, 0, -1):
    seconds = i % 60
    minutes = (i // 60) % 60
    hours = (i // 3600) % 24

    time.sleep(1)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
print("Time's up!")
#nested loops
for x in range(4):
    for i in range(1,17):
        print(i, end=" ")   
    print()  # Move to the next line after each row

rows= int (input("Enter the number of rows: "))
column = int (input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")
for i in range(rows):
    for j in range(column):
        print(symbol, end=" ")
    print()  # Move to the next line after each row

#lists comprehension
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

#shopping cart program
foods = []
prices = []
total = 0.0

while True:
    food=input("Enter a food item to purchase (or type q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for {food}: "))
        foods.append(food)
        prices.append(price)
        total += price

print("Thank you for shopping with us!")
print("\n--- Your Shopping Cart ---")
for i in range(len(foods)):
    print(f"{foods[i]} - ${prices[i]:.2f}")
print(f"Total: ${total:.2f}")