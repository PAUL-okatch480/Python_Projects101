#python user input
name=input("Enter your name: ")
age=input("Enter your age: ")
age=int(age)  # Convert age to an integer
age = age + 1  # Increment age by 1
print(f"Hello, {name}! Welcome to the scaling101 program.")
print(f"Next year, you will be {age} years old.")
#calculate the area of a rectangle
length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
area=length*width
print(f"The area of the rectangle is {area} cm².")

#a simple shopping cart program
item=input("Enter the item you want to buy: ")
price=float(input(f"Enter the price of {item}: "))
quantity=int(input(f"Enter the quantity of {item} you want to buy: "))
total=price * quantity
print(f"You have purchased {quantity} {item} /s for a total of ${total:.2f}.")
print("Thank you for shopping with us!")
print("Have a great day!")
print("KARIBU TENA!")