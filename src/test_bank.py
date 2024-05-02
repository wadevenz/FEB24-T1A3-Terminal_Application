import pytest
import os.path

from bank_functions import create_account, get_account, withdraw, deposit

main_file = "test_account.csv"

if (not os.path.isfile(main_file)):
    account_details = open(main_file, "w")
    account_details.write("name,pin,balance\n")
    account_details.close()

def test_create_account():
    name = 'Wade'
    pin = '1111'
    balance = "100"
    main_file = 'test_account.csv'
    create_account(main_file, name, pin, balance)
    user = get_account(main_file, pin,)
    print(user)
    assert user != None
    assert user['name'] == name
    assert user['pin'] == pin
    assert user['balance'] == '100'
    assert user['balance'] != '-50'
    

def test_withdraw():
    name = 'Watson'
    pin = '5555'
    amount = 20
    balance = 80
    main_file = 'test_account.csv'
    create_account(main_file, name, pin, balance)
    new_balance = withdraw(main_file, name, pin, balance, amount)
    assert new_balance != None
    assert new_balance == 60
    assert pin != '2222'
    assert new_balance != 120
    assert new_balance != 'twenty'
    assert balance != 300

def test_deposit():
    name = 'Wade'
    pin = '2222'
    amount = 100
    balance = 45
    main_file = 'test_account.csv'
    create_account(main_file, name, pin, balance)
    new_balance = deposit(main_file, name, pin, balance, amount)
    assert new_balance != None
    assert new_balance == 145
    assert pin == '2222'
    assert new_balance != -50
    assert new_balance != 'Two hundred'
    assert balance != 300



# tested last as it also serves to test other created accounts

def test_get_account():
    assert get_account ('fake.csv', '1111') == None
    assert get_account ('test_account.csv','1111') == {'name':'Wade','pin': '1111','balance':'100'}
    assert get_account ('test_account.csv','9876') != {'name':'Wade','pin': '1111','balance':'100'}
    assert get_account ('test_account.csv','5555') == {'name':'Watson','pin': '5555','balance':'80'}
    assert get_account ('test_account.csv','1111') != {'name':'Wade','pin': '2222','balance':'200'}
