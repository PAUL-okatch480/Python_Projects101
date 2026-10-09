#confitional statements
#do some code if a certain condition is tru, else do something else
age=int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


response= input("Would you like to order some food? (yes/no): ")
if response.lower() == "yes":
    print("Great! Let's see what we have on the menu.")
else:
    print("No worriess!, maybe next time.")

#A simple calculator using conditional statements
operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{round(result,3)}")
elif operator == "-":
    result = num1 - num2
    print(f"{round(result,3)}")
elif operator == "*":
    result = num1 * num2
    print(f"{round(result,3)}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{round(result,3)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")   

#Coming up with a weight converter
weight = float(input("Enter your current weight: "))
unit = input("Enter the unit of your weight (kg/g): ").lower()
if unit == "kg":
    converted_weight = weight * 1000
    unit= "Grams"
    print(f"Your weight in grams is: {round(converted_weight, 2)} g")
elif unit == "g":
    converted_weight = weight / 1000
    unit= "Kilograms"
    print(f"Your weight in kilograms is: {round(converted_weight, 2)} kg")
else:
    print("Error: Invalid unit. Please enter 'kg' or 'g'.")

#A temeperature converter using conditional statements
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C/F): ").lower()
if unit == "c":
    converted_temperature = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {round(converted_temperature, 2)} °F")

elif unit == "f":
    converted_temperature = (temperature - 32) * 5/9
    print(f"The temperature in Celsius is: {round(converted_temperature, 2)} °C")

else:
    print("Error: Invalid unit. Please enter 'C' or 'F'.")
print("Thank you for using the temperature converter!")
