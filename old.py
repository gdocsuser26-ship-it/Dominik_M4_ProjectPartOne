item = input("Enter the item name: ")
if item in Inventory_list:
    # prints the inventory of the item
    print(item,"is available in the inventory.", Inventory_list[item]['Category'],', at:', Inventory_list[item]['Price'],',', Inventory_list[item]['Quantity'], 'at hand')
    while True:
        operator = input("Do you want to update the quantity(1), price(2), delete(0), exit(ENTER)? : ")
        if operator =='1':
    # adjust the quantity
            try:
                new_quantity = int(input('New quantity: '))
                Inventory_list[item]['Quantity'] = new_quantity
            except ValueError:
                print('Invalid input.',item,'has been added with quantity 0')
    #adjust the price
        elif operator == '2':
            new_price = input('New price: ')
            Inventory_list[item]['Price'] = new_price
    # delets the item
        elif operator == '0':
            del Inventory_list[item]
            print(item, 'has been removed from the inventory.')
            break
    # ends the loop
        elif operator == '':
            break
        else:            
            print("Invalid input. Please enter 1, 2, 0, or press ENTER to exit.")
else:
    print(item,"is not available in the inventory. Would you like to add it? (yes/no): ")
    add_item = input()
    # adds the item
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
    # prints the inventory
    else:
       print ("Item not added to the inventory, current inventory: ")
       for product, data in Inventory_list.items():
            print(product, ':', data)
