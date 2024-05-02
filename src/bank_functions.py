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
    
def view_balance(main_file, name, pin):
    get_balance = get_account(main_file, pin)
    balance = get_balance['balance']
    print (f"\n{Fore.blue}Hello {name}! You have ${balance} in your account!{Style.reset}\n")

def withdraw(main_file, name, pin, balance, amount):
    app_balance = []
    try:
        with open(main_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if (pin != row[1]):
                    app_balance.append(row)
                else:
                    balance = int(row[2])
                    if amount <= balance:
                        new_balance = balance - amount
                        app_balance.append([name,pin,new_balance])
                        print(f"{Fore.blue}Thanks {name}! You have withdrawn ${amount}, you now have ${new_balance} in your account!\n{Style.reset}")
                        # return new_balance
                    else:
                        print(f"{Fore.red}Insufficient Funds{Style.reset}")
                        app_balance.append ([name,pin,balance])
                        continue
        with open(main_file, "w") as f:
            writer = csv.writer(f)
            writer.writerows(app_balance)
    except TypeError:
        print(f"{Fore.red}Please enter valid input{Style.reset}")

    

def deposit(main_file, name, pin, balance, amount):
    app_balance = []
    try:
        with open(main_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if (pin != row[1]):
                    app_balance.append(row)
                else:
                    balance = int(row[2])
                    new_balance = balance + amount
                    app_balance.append([name,pin,new_balance])
                    print(f"{Fore.blue}Thanks {name}! You have deposited ${amount}, you now have ${new_balance} in your account!\n{Style.reset}")
                    # return new_balance
        with open(main_file, "w") as f:
            writer = csv.writer(f)
            writer.writerows(app_balance)
    except TypeError:
        print(f"{Fore.red}Please enter valid input{Style.reset}")
 
def remove_account(main_file, pin):
    new_file = []
    with open(main_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if (pin != row[1]):
                    new_file.append(row) 
                else:
                    return row[2]
    with open(main_file, "w") as f:
            writer = csv.writer(f)
            writer.writerows(new_file)