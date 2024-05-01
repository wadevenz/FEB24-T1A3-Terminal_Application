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
    
def view_balance(main_file, name, balance):
    print (f"\n{Fore.blue}Hello {name}! You have ${balance} in your account!{Style.reset}\n")

def withdraw(main_file, name, pin, balance, amount):
    cum_balance = []
    with open(main_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (pin != row[1]):
                cum_balance.append(row)
            else:
                balance = int(row[2])
                if (amount > 0) and (amount <= balance):
                    new_balance = balance - amount
                    cum_balance.append([row[0], row[1], new_balance])
                    print(f"{Fore.blue}Thanks {row[0]}! You have withdrawn ${amount}, you now have ${new_balance} in your account!\n{Style.reset}")
                else:
                    print(f"{Fore.red}Incorrect Amount. Value must be below or equal to available balance and above $0{Style.reset}")
    with open(main_file, "w") as f:
        writer = csv.writer(f)
        writer.writerows(cum_balance)

def deposit(main_file, name, pin, balance, amount):
    pass
 
    