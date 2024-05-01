import os.path
import csv

from colored import Fore, Back, Style

from bank_functions import create_account, get_account, view_balance, withdraw, deposit, remove_account

print(f"\n{Fore.cyan}{Style.bold}Welcome to Terminal Bank{Style.reset}\n")

current_user = None
initial_balance = 100


def ask_name():
    name = input("Please enter your Name: ")
    return name

def ask_pin():
    pin = input("Please enter a 4 digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        return pin
    else:
        print(f"{Fore.red}Invalid PIN\n{Style.reset}")    
        welcome_menu()


def ask_amount():
    try:
        amount = float(input("Please enter amount: "))
        if amount > 0:
            return amount
    except ValueError:
        print(f"{Fore.red}Error{Style.reset}")


def handle_create():
    name = ask_name()
    pin = ask_pin()
    create_account(main_file, name, pin, initial_balance)

def handle_access():
    pin = ask_pin()
    if get_account(main_file,pin) != None:
        current_user = get_account(main_file, pin)
        main_menu(main_file, current_user['name'], current_user['pin'], current_user['balance'])
    else:
        print(f"\n{Fore.red}Incorrect PIN{Style.reset}\n")
        welcome_menu()

main_file = "account_details.csv"

if (not os.path.isfile(main_file)):
    account_details = open(main_file, "w")
    account_details.write("name,pin,balance\n")
    account_details.close()

def welcome_menu():
    print(f"{Fore.cyan}1. Create Account")
    print(f"2. Access Account")
    print(f"3. Exit{Style.reset}\n")

    user_selection = input(f"{Fore.yellow}Enter your selection from the options above: {Style.reset}")

    selection = user_selection

    if (selection == "1"):
        handle_create()
        welcome_menu()

    elif (selection == "2"):
        handle_access()

    elif (selection == "3"):
        print ("Thanks for banking with Terminal Bank! See you again soon")
        exit()
    else:
        print(f"\n{Fore.red}Please select from the options{Style.reset}\n")
        welcome_menu()



def main_menu(main_file, name, pin, balance):
    print(f"\n{Back.black}Account - {name}{Style.reset}\n")
    print(f"\n{Fore.cyan}1. View Balance")
    print("2. Withdrawal")
    print("3. Deposit")
    print("4. Remove Account")
    print(f"5. Back\n{Style.reset}")

    user_choice = input(f"{Fore.yellow}Enter your selection from the options provided: {Style.reset}")

    choice = user_choice

    if (choice == "1"):
        view_balance(main_file, name, pin)
        main_menu(main_file, name, pin, balance)
            
    elif (choice == "2"):
        amount = ask_amount()
        withdraw(main_file, name, pin, balance, amount)
        main_menu(main_file, name, pin, balance)

    elif (choice == "3"):
        amount = ask_amount()
        deposit(main_file, name, pin, balance, amount)
        main_menu(main_file, name, pin, balance)

    elif (choice == "4"):
        confirm = input("Are you sure you want to remove account? Y/N: ")
        if confirm.upper() == "Y":
            remove_account(main_file, pin)
            print(f"\nThanks {name}! Your account has been removed. Please take your ${balance}\n")
            welcome_menu()
        else:
            main_menu(main_file, name, pin, balance)

    elif (choice == "5"):
        welcome_menu()
        
    else:
        print(f"{Fore.red}Please choose from the options provided{Style.reset}")
        main_menu(main_file, name, pin, balance)


welcome_menu()