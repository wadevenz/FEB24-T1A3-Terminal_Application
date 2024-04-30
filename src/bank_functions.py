import csv

from colored import Fore, Back, Style


def create_account(main_file, name, pin, balance):

    if get_account(main_file, pin) != None:
        print(f"\n{Fore.red}Same PIN already exists, please choose another.{Style.reset}\n")
    else:
        with open(main_file, "a") as f:
            writer = csv.writer(f)
            writer.writerow([name, pin, balance])
            print(f"\n{Fore.white}{Back.black}Thanks for opening an account with us {name}! As a bonus, ${balance} has been deposited into your account.{Style.reset}\n")
        
def get_account(main_file, pin):
    try:
        with open(main_file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['pin'] == pin:
                    return row
    except FileNotFoundError:
        return None
    
def view_balance(main_file, name, pin, balance):
    print (f"\n{Fore.blue}Hello {name}! You have ${balance} in your account!{Style.reset}\n")

def withdraw():
    pass

def deposit():
    pass
 
    