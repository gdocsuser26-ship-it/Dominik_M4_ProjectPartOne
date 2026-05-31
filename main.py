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

# Partr 2: Function to search and update the inventory
item = input("Enter the item name: ")
if item in Inventory_list:
    print(item,"is available in the inventory.", Inventory_list[item]['Category'],', at:', Inventory_list[item]['Price'],',', Inventory_list[item]['Quantity'], 'at hand')
    while True:
        operator = input("Do you want to update the quantity(1), price(2), delete(0), exit(ENTER)? : ")
        if operator =='1':
            try:
                new_quantity = int(input('New quantity: '))
                Inventory_list[item]['Quantity'] = new_quantity
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")
        elif operator == '2':
            new_price = input('New price: ')
            Inventory_list[item]['Price'] = new_price
        elif operator == '0':
            del Inventory_list[item]
            print(item, 'has been removed from the inventory.')
            break
        elif operator == '':
            break
        else:            
            print("Invalid input. Please enter 1, 2, 0, or press ENTER to exit.")
else:
    print(item,"is not available in the inventory. Would you like to add it? (yes/no): ")
    add_item = input()
    if add_item == 'yes':
        category = input("Enter the category: ")
        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")
            quantity = 0
        price = input("Enter the price: ")
        Inventory_list[item] = {'Category': category, 'Quantity': quantity, 'Price': price}
        print(item, 'has been added to the inventory, Current inventory: ')
        for product, data in Inventory_list.items():
            print(product, ':', data)

    else:
       print ("Item not added to the inventory, current inventory: ")
       for product, data in Inventory_list.items():
            print(product, ':', data)


    