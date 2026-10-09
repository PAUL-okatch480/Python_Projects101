#python dictionaries
capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Germany': 'Berlin', 'India': 'New Delhi'}
for key in capitals.keys():
    print(f"The capital of {key} is {capitals[key]}.")
for key, value in capitals.items():
    print(f"{key} : {value}")

#a consession stand
menu={"Hot Dog": 2.50,
       "Hamburger": 3.00,
         "Cheeseburger": 3.50,
           "French Fries": 1.50,
             "Soda": 1.00,
             "Water": 0.75,
             "Popcorn": 2.00,
             "Candy": 1.25,
             "Ice Cream": 2.75,
             "Nachos": 3.25,
             "Pretzel": 2.00,
             "Chicken Nuggets": 4.00,
             "Pizza Slice": 3.00,
             "Salad": 3.50,
             "Fruit Cup": 2.50,
             "Smoothie": 4.00,
             "Coffee": 1.50,
             "Tea": 1.25,
             "Hot Chocolate": 2.00,
             "Milkshake": 3.50,
             "Bagel": 2.00,
             "Muffin": 2.50,
             "Croissant": 2.75,
             "Donut": 1.50,
             "Cookie": 1.25,
             "Brownie": 2.00,
             "Cupcake": 2.50,
             "Ice Cream Sundae": 3.75,
             "Waffle": 3.00,
             "Pancakes": 3.50,
             "French Toast": 3.25,
             "Omelette": 4.00,
             "Breakfast Burrito": 3.75,
             "Bagel Sandwich": 3.50, 
             "Breakfast Platter": 5.00,
             "Chicken Sandwich": 4.50,
             "Fish Sandwich": 4.75,
             "Veggie Burger": 4.00,
             "Grilled Cheese": 3.00}
cart=[]
total=0
print("Welcome to Oppin concession Stand!")
print("****** Menu *****")
for item, price in menu.items():
    print(f"{item:10}: ${price:.2f}")
print("******************")
while True:
    item=input("Enter the item you want to purchase (or type 'q' to quit): ")
    if item.lower() == 'q':
        break
    elif menu.get(item) is not None:
        cart.append(item)
print("--------------------------------------")
for item in cart:
    price = menu.get(item, 0)
    total += price
    print(f"{item:10}: ${price:.2f}")
print(f"Total: ${total:.2f}")