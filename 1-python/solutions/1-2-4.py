#Challenge 1-2-4¶
'''
Write a program to create a shopping list.

loop until "quit" is entered. input a grocery item input a quantity save the item as the key in the dictionary 
and quantity as the value if the item is in the dictionary already, add the quantity to the existing value.

'''

items = {} # initializes an empty dictionary

while True:
    item = input("Enter an item: ")
    if item == "quit":
        print("Exiting program")
        break
    
    qty = int(input("Enter a quantity: "))
    if item in items.keys():#checks if item in dictionary, keys()function displays all the keys in the dictionary 
        items[item] = items[item] + qty # updates quantity
    else:
        items[item] = qty # item not found so add key and value to dictionary
    print("ITEMS:", items) # prints after update
print(f"Final List: {items}") # prints after exiting

        
        