import os
import json
import hashlib

# Function to hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to create a new user account
def create_account():
    username = input("Enter username: ")
    password = hash_password(input("Enter password: "))
    
    user_data = {
        'username': username,
        'password': password,
        'inventory_file': f'{username}_inventory.json',
        'staff_file': f'{username}_staff.json'
    }
    
    with open(f'{username}_account.json', 'w') as user_file:
        json.dump(user_data, user_file)
    
    print("Account created successfully!")

# Function to login
def login():
    username = input("Enter username: ")
    password = hash_password(input("Enter password: "))
    
    try:
        with open(f'{username}_account.json', 'r') as user_file:
            user_data = json.load(user_file)
            
            if user_data['password'] == password:
                print("Login successful!")
                return user_data
            else:
                print("Invalid credentials. Please try again.")
    except FileNotFoundError:
        print("User not found. Please create an account.")

# Function to manage product inventory
def manage_inventory(username):
    inventory_file = username['inventory_file']
    
    try:
        with open(inventory_file, 'r') as file:
            inventory_data = json.load(file)
    except FileNotFoundError:
        inventory_data = {}

    while True:
        print("\nInventory Management:")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))

            if product_name in inventory_data:
                inventory_data[product_name] += quantity
            else:
                inventory_data[product_name] = quantity

            with open(inventory_file, 'w') as file:
                json.dump(inventory_data, file)
                
            print("Product added to inventory.")

        elif choice == '2':
            print("\nCurrent Inventory:")
            for product, quantity in inventory_data.items():
                print(f"{product}: {quantity}")

        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Function to manage staff
def manage_staff(username):
    staff_file = username['staff_file']

    try:
        with open(staff_file, 'r') as file:
            staff_data = json.load(file)
    except FileNotFoundError:
        staff_data = []

    while True:
        print("\nStaff Management:")
        print("1. Add Staff Member")
        print("2. View Staff Members")
        print("3. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            staff_name = input("Enter staff member name: ")
            staff_data.append(staff_name)

            with open(staff_file, 'w') as file:
                json.dump(staff_data, file)

            print("Staff member added.")

        elif choice == '2':
            print("\nCurrent Staff Members:")
            for staff_member in staff_data:
                print(staff_member)

        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# Main program
while True:
    print("\nSupermarket Management System:")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == '1':
        create_account()
    elif main_choice == '2':
        user_data = login()
        if user_data:
            while True:
                print("\nMain Menu:")
                print("1. Manage Inventory")
                print("2. Manage Staff")
                print("3. Logout")

                user_choice = input("Enter your choice: ")

                if user_choice == '1':
                    manage_inventory(user_data)
                elif user_choice == '2':
                    manage_staff(user_data)
                elif user_choice == '3':
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif main_choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
