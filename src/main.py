import os.path
import csv

from colored import Fore, Back, Style

from bank_functions import create_account, get_account, view_balance, withdraw, deposit

print(f"\n{Fore.cyan}Welcome to Terminal Bank{Style.reset}\n")

current_user = None
initial_balance = 100


def ask_name():
    name = input("Please enter your First Name: ")
    return name

def ask_pin():
    pin = input("Please enter a 4 digit PIN: ")
    if pin.isdigit() and len(pin) == 4:
        return pin
    else:
        print(f"{Fore.red}Invalid PIN\n{Style.reset}")    
        welcome_menu()

def handle_create():
    name = ask_name()
    pin = ask_pin()
    create_account(main_file, name, pin, initial_balance)

def handle_access():
    pin = ask_pin()
    current_user = get_account(main_file, pin)
    main_menu(main_file, current_user['name'], current_user['pin'], current_user['balance'])

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
        print("Please select from the options above")
        welcome_menu()



def main_menu(main_file, name, pin, balance):
    print(f"\nHello {name}!\n")
    print(f"\n{Fore.cyan}1. View Balance")
    print("2. Withdrawal")
    print("3. Deposit")
    print(f"4. Back\n{Style.reset}")

    user_choice = input(f"{Fore.yellow}Enter your selection from the options above: {Style.reset}")

    choice = user_choice


    if (choice == "1"):
        view_balance(main_file, name, balance)
        main_menu(main_file, name, pin, balance)
        
    elif (choice == "2"):
        withdraw(main_file, name, pin, balance)
        main_menu(main_file, name, pin, balance)
        
    elif (choice == "3"):
        deposit(main_file, name, pin, balance)
        main_menu(main_file, name, pin, balance)

    elif (choice == "4"):
        welcome_menu()
    
    else:
        print("Please choose from the options provided")


welcome_menu()