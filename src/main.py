# python packages grouped as per styling guidelines
import os.path
import csv

from colored import Fore, Back, Style

from bank_functions import create_account, get_account, view_balance, withdraw, deposit, remove_account

# Welcome Print message
print(f"\n{Fore.cyan}{Style.bold}Welcome to Terminal Bank{Style.reset}\n")

# Initialises current user and initial balance
current_user = None
initial_balance = 100

# Simple function for user input to return name variable
def ask_name():
    name = input(f"\n{Fore.yellow}Please enter your Name: {Style.reset}")
    return name

# Simple function to return PIN from user input. To be reused in multiple functions.
# print message of "invalid pin" will occur if input doesnt meet the criteria of being 4 digits
def ask_pin():
    pin = input(f"\n{Fore.yellow}Please enter a 4 digit PIN: {Style.reset}")
    if pin.isdigit() and len(pin) == 4:
        return pin
    else:
        print(f"{Fore.red}Invalid PIN\n{Style.reset}")    
        welcome_menu()

# Simple function to call where user input for amount is required. Value Error for negative integers
def ask_amount():
    try:
        amount = int(input(f"\n{Fore.yellow}Please enter amount: {Style.reset}"))
        if amount > 0:
            return amount
    except ValueError:
        print(f"{Fore.red}Error{Style.reset}")


def handle_create():
    name = ask_name()
    pin = ask_pin()
    create_account(main_file, name, pin, initial_balance)

# This function allows a print message telling the user if PIN input does not match file when accessing account
# Uses conditional to see if 'get_account" returns line of file, then sets line to 'current_user' object
def handle_access():
    pin = ask_pin()
    if get_account(main_file,pin) != None:
        current_user = get_account(main_file, pin)
        main_menu(main_file, current_user['name'], current_user['pin'], current_user['balance'])
    else:
        print(f"\n{Fore.red}Incorrect PIN{Style.reset}\n")
        welcome_menu()

# sets file name object.
main_file = "account_details.csv"

# uses package to see if file exists, if none, creates new file using csv writer. File is written with headings to three columns

if (not os.path.isfile(main_file)):
    account_details = open(main_file, "w")
    account_details.write("name,pin,balance\n")
    account_details.close()

# welcome menu exists within a function. user input required for selection, then multiple conditionals are 
# used to navigate through menu. internal recursion of the function is used to recall menu until user selects to exit.
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
        print (f"\n{Back.black}{Fore.white}Thanks for banking with Terminal Bank! See you again soon{Style.reset}")
        exit()
    else:
        print(f"\n{Fore.red}Please select from the options{Style.reset}\n")
        welcome_menu()



def main_menu(main_file, name, pin, balance):
    print(f"\n{Back.black}{Fore.white}Account - {name}{Style.reset}\n")
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
        get_balance = get_account(main_file, pin)
        final_balance = get_balance['balance']
        confirm = input(f"\n{Back.red}{Fore.white}Are you sure you want to remove account? Y/N: {Style.reset}")
        if confirm.upper() == "Y":
            remove_account(main_file, pin)
            print(f"\n{Back.blue}{Fore.white}Thanks {name}! Your account has been removed. Please take your ${final_balance}{Style.reset}\n")
            welcome_menu()
        elif confirm.upper() == "N":
            print(f"\nYour account has been kept, {name}. You still have ${final_balance} in your account")
            main_menu(main_file, name, pin, balance)
        else:
            print(f"{Fore.red}Invalid input{Style.reset}")
            main_menu(main_file, name, pin, balance)
    elif (choice == "5"):
        welcome_menu()
    else:
        print(f"{Fore.red}Please choose from the options provided{Style.reset}")
        main_menu(main_file, name, pin, balance)

# reads function first, starts application with welcome menu

welcome_menu()