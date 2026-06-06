# Part 1: Set up the inventory 
Inventory_list = {
    'Apple':{'Category':'Fruit', 'Quantity': 50, 'Price': '$0.50'},
    'Bacon':{'Category':'Meat', 'Quantity': 25, 'Price': '$4.50'},
    'Banana':{'Category':'Fruit', 'Quantity': 100, 'Price': '$0.30'},
    'Bread':{'Category':'Bakery', 'Quantity': 30, 'Price': '$2.00'},
    'Carrots':{'Category':'Produce', 'Quantity': 60, 'Price': '$1.00 per lb'},
    "Chicken breast": {"Category": "Meat", "Quantity": 50, "Price": "$5.00 per lb"},
    "Coffee": {"Category": "Beverage", "Quantity": 20, "Price": "$8.00 per lb"},
    "Eggs": {"Category": "Dairy", "Quantity": 40, "Price": "$2.50 per dozen"},
    "Ground Beef": {"Category": "Meat", "Quantity": 40, "Price": "$4.00 per lb"},
    "Lettuce": {"Category": "Produce", "Quantity": 40, "Price": "$1.50"},
    "Milk": {"Category": "Dairy", "Quantity": 25, "Price": "$3.00 per gallon"},
    "Orange Juice": {"Category": "Beverage", "Quantity": 30, "Price": "$4.00 per gallon"},
    "Peanut Butter": {"Category": "Pantry", "Quantity": 25, "Price": "$3.00"},
    "Rice": {"Category": "Pantry", "Quantity": 100, "Price": "$1.20 per lb"}
    }

# Part 2: Functions to search, print and update the inventory
def print_inventory():
    print("Current inventory:")
    for product, data in Inventory_list.items():
        print(product,':', data)   

def search_inventory(item):
    if item in Inventory_list:
        print(item,"is available in the inventory.", Inventory_list[item]['Category'],', at:', Inventory_list[item]['Price'],',', Inventory_list[item]['Quantity'], 'at hand')
        return input("Do you want to update the quantity(1), price(2), category(3), DELETE(D), exit(anything else)? : ")
    else:
        print(item,"is not available in the inventory.")
        return input("Do you want to add it? (yes/no): ")
        
def new_Category(item):
    new_Category = input("Enter the new category for  "+ item + ": ")
    Inventory_list[item]['Category'] = new_Category
    print(item, 'category has been updated')
    print_item(item)

def new_Price(item):
    new_Price = input("Enter the price for : "+ item +': ')
    Inventory_list[item]['Price'] = new_Price
    print(item, 'price has been updated')
    print_item(item)

def new_Quantity(item):  
    #Error handling for quantity input   
    try:
        new_quantity = int(input('New quantity: '))
        Inventory_list[item]['Quantity'] = new_quantity
        print(item, 'quantity has been updated')
        print_item(item)
    except ValueError:
                print('Invalid input.',item,'has been added with quantity 0')

def delete_item(item):
    del Inventory_list[item]
    print(item, 'has been removed from the inventory.') 

def add_item(item):
    Inventory_list[item] = {}
    new_Category(item)
    new_Price(item)
    new_Quantity(item)
    print(item, 'has been added to the inventory, Current inventory: ')
    print_item(item)

def print_item(item):
    print(item, ':', Inventory_list[item])
    


# Part 3: Main program 

initial_menu = input(" Do you want to view the current inventory? (ENTER), or search specific item? (S) : ")
      
if initial_menu == 'S':    
     item = input("Enter the item name: ")
     operator = search_inventory(item)
     if operator =='1':
        new_Quantity(item)

     elif operator == '2':
        new_Price(item)

     elif operator == '3':
        new_Category(item)

     elif operator == 'D':
        delete_item(item)
        print_inventory()

     elif operator == 'yes':
        add_item(item)
     else:   
        print("Exiting the program. Current inventory: ")
        print_inventory()   
else:
     print_inventory() 
    









    