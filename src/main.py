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