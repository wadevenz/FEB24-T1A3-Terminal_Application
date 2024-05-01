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
    pass

def test_withdraw():
    pass

def test_deposit():
    amount = 100
    balance = 100
    new_balance = amount + balance
    main_file = 'test_account.csv'
    assert new_balance != None
    assert new_balance == 200


