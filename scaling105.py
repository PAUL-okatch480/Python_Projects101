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
