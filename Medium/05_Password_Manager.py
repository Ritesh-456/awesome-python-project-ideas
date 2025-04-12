import time
import sys
import random

def smooth_flow(text, delay=0.05):
    """Prints each character of the text with a specified delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

passwords = {
    "facebook": {
        "user_name": "name",
        "user_password": "password"
    },
    "gmail": {
        "user_name": "another_name",
        "user_password": "another_password"
    }
}

numbers_string = '12345678910'
lowercase_string = 'abcdefghijklmnopqrstuvwxyz'
uppercase_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_symbols_string = "!@#$%^&*()-_+=[]\{}|;:\',.<>/?`~"

numbers_list = list(numbers_string)
lowercase_list = list(lowercase_string)
uppercase_list = list(uppercase_string)
special_symbols_list = list(special_symbols_string)

def generate_password(length=12):
    """Generates a random password of the specified length."""
    all_chars = numbers_list + lowercase_list + uppercase_list + special_symbols_list
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def suggest_passwords(num_suggestions=3, length=12):
    """Suggests a list of random passwords."""
    suggestions = []
    for _ in range(num_suggestions):
        suggestions.append(generate_password(length))
    return suggestions

def store_credentials(account_name, username, password):
    """Stores the provided credentials in the passwords dictionary."""
    passwords[account_name] = {
        "user_name": username,
        "user_password": password
    }
    smooth_flow(f"Credentials for {account_name} stored.", delay=0.02)

def retrieve_credentials(account_name):
    """Retrieves and displays the credentials for the given account."""
    if account_name in passwords:
        smooth_flow(f"Account: {account_name}", delay=0.02)
        smooth_flow(f"Username: {passwords[account_name]['user_name']}", delay=0.02)
        smooth_flow(f"Password: {passwords[account_name]['user_password']}", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def change_username(account_name, new_username):
    """Changes the username for the given account."""
    if account_name in passwords:
        passwords[account_name]["user_name"] = new_username
        smooth_flow(f"Username for {account_name} changed to {new_username}.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def change_password(account_name, new_password):
    """Changes the password for the given account."""
    if account_name in passwords:
        passwords[account_name]["user_password"] = new_password
        smooth_flow(f"Password for {account_name} changed.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def delete_account(account_name):
    """Deletes the account from the passwords dictionary."""
    if account_name in passwords:
        del passwords[account_name]
        smooth_flow(f"Account {account_name} deleted.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

while True:
    try:
        options = ("1. Store password\n2. Change password\n3. Change username\n4. Show password\n5. Suggest Password\n6. Delete account\n7. Exit")
        smooth_flow(options, delay=0.02)
        user_input = int(input("Enter your option: "))

        if user_input == 1:
            account = input("Enter account name: ")
            user = input("Enter username: ")
            password = input("Enter password: ")
            store_credentials(account, user, password)

        elif user_input == 2:
            account = input("Enter account name: ")
            new_password = input("Enter new password: ")
            change_password(account, new_password)
        elif user_input == 3:
            account = input("Enter account name: ")
            new_user = input("Enter new username: ")
            change_username(account, new_user)

        elif user_input == 4:
            account = input("Enter account name: ")
            retrieve_credentials(account)

        elif user_input == 5:
            suggestions = suggest_passwords()
            smooth_flow("Password Suggestions:", delay=0.02)
            for suggestion in suggestions:
                smooth_flow(suggestion, delay=0.02)

        elif user_input == 6:
            account = input("Enter account name to delete: ")
            delete_account(account)

        elif user_input == 7:
            smooth_flow("Exiting...", delay=0.02)
            break
        else:
            smooth_flow("Invalid option.", delay=0.02)

    except ValueError:
        smooth_flow("Invalid input. Please enter a number.", delay=0.02)