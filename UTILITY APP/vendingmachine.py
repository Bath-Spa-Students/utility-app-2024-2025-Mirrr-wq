# store the items and categorize them 
items = {
    "Chocolates": {
        1: {"name": "Dairy Milk Chocolate", "price": 3.00},
        2: {"name": "Mars Bar", "price": 2.50},
        3: {"name": "KitKat", "price": 2.50}
    },
    "Beverages": {
        4: {"name": "Cold Coffee", "price": 2.50},
        5: {"name": "Orange Juice", "price": 3.00},
        6: {"name": "Apple Juice", "price": 2.00},
        7: {"name": "mango juice" , "price" : 3.50}
    },
    "Snacks": {
        8: {"name": "Lays Chips", "price": 1.50},
        9: {"name": "Pringles", "price": 2.00},
        10: {"name": "Oreo Biscuits", "price": 1.00}
    }
}

# this code will display the items as per menu for the user

def display_items():
    print("\n !!! WELCOME TO MY VENDING MACHINE, HERE IS THE MENU. !!!")
    for category, category_items in items.items():
        print(f"\n{category}:")
        print("-" * 30)
        for code, item in category_items.items():
            print(f"{code}. {item['name']} - £{item['price']:.2f}")

#this code will ask the user to insert money for the item they selected from the menu.

# if the money inserted is not enough the vending machine will cancel the transaction.

def get_money():
    while True:
        try:
            money = float(input("\nPlease insert money (in £): "))
            if money > 0:
                return money
            else:
                print("Please insert a valid amount!")
        except ValueError:
            print("Please enter a valid number!")

# this code will ask the user to select the item from the menu

def get_choice():
    while True:
        try:
            choice = int(input("\nEnter item code (1-10): "))

            # this code will check if the selected item number is there on the list
            
            for category_items in items.values():
                if choice in category_items:
                    return choice, category_items[choice]
            print("Invalid item code! Please try again."),
        except ValueError:
            print("Please enter a valid number!")

# this code will display the iten name and the price and will ask the user tpo insert the amount of money as per the menu

# if the inserted amount is not enough itll ask the user to insert more money and will cancel the transaction

def main():
    
    while True:
        display_items()
        choice, selected_item = get_choice()
        
        # this code will show the item selected and will show the price for the perticular item.

        print(f"\nYou selected: {selected_item['name']}")
        print(f"Price: £{selected_item['price']:.2f}")
        
        money = get_money()

        # this code will give the change if user inserts more money than its required

        if money >= selected_item['price']:
            change = money - selected_item['price']
            print(f"\nDispensing {selected_item['name']}...")
            if change > 0:
                print(f"Your change: £{change:.2f}")
            print("Thank you for your purchase!")
        else:
            print("\nNot enough money! Transaction cancelled.")
            print(f"Returning £{money:.2f}")

        # after one transaction this code will ask the user if they want to buy something else

        # if they say yes the whole menu will show again from which the user can select what they want to buy.

        another = input("\nWould you like to buy something else? (yes/no): ").lower()
        if another != 'yes':
            print("\nTHANKYOU FOR USING MY VENDING MACHINE, COME BACK SOON")
            break


if __name__ == "__main__":
    main()