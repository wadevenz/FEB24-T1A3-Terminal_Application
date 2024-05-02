import pytest

from bank_functions import create_account, get_account, withdraw, deposit


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

def test_get_account():
    assert get_account ('fake.csv', '1111') == None
    assert get_account ('test_account.csv','1111') == {'name':'Wade','pin': '1111','balance':'100'}
    assert get_account ('test_account.csv','9876') != {'name':'Wade','pin': '1111','balance':'100'}
    assert get_account ('test_account.csv','9876') == {'name':'Sherlock','pin': '9876','balance':'200'}
    assert get_account ('test_account.csv','1111') != {'name':'Wade','pin': '1111','balance':'200'}

# to test following functions, temporary 'return = new_balance' added within the functions

def test_withdraw():
    name = 'Watson'
    pin = '5555'
    amount = 20
    balance = 100
    main_file = 'test_account.csv'
    create_account(main_file, name, pin, balance)
    new_balance = withdraw(main_file, name, pin, balance, amount)
    assert new_balance != None
    assert new_balance == 80
    assert pin != '2222'
    assert new_balance != 120
    assert new_balance != 'twenty'
    assert balance != 300

def test_deposit():
    name = 'Wade'
    pin = '2222'
    amount = 100
    balance = 100
    main_file = 'test_account.csv'
    create_account(main_file, name, pin, balance)
    new_balance = deposit(main_file, name, pin, balance, amount)
    assert new_balance != None
    assert new_balance == 200
    assert pin == '2222'
    assert new_balance != -50
    assert new_balance != 'Two hundred'
    assert balance != 300


