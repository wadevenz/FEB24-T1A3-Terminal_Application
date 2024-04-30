import os.path
import csv

from colored import Fore, Back, Style

print(f"\n{Fore.cyan}Welcome to Terminal Bank{Style.reset}\n")

current_user = None
initial_balance = 100

def ask_name():
    name = input("Please enter your First Name: ")
    return name

def ask_pin():
    pin = input("Please enter a 4 digit PIN: ")
    if not pin.isdigit():
        print ("Please use only numbers!")
    elif len(pin) != 4:
        print("Valid PIN must be 4 digits!")
    else:
        return pin

def handle_create():
    name = ask_name()
    pin = ask_pin()
    create_account(main_file, name, pin, initial_balance)

def handle_access():
    pin = ask_pin()
    current_user = get_account(main_file, pin)
    main_menu()

main_file = "account_details.csv"

if (not os.path.isfile(main_file)):
    account_details = open(main_file, "w")
    account_details.write("name,pin,balance\n")
    account_details.close()

