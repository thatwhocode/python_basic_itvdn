from .main import BankAccount


def test_creating_check():
    acc = BankAccount(1, "Stanislav", 0)
    assert acc.account_number == 1
    assert acc.account_holder == "Stanislav"
    assert acc.balance == 0
    
def test_zero_balance_withdraw():
    acc = BankAccount(1, "Stanislav", 0)
    assert acc.withdrawFunds(500) == "You don`t have enough amount of money"

def test_withdrawing():
    acc = BankAccount(1, "Stanislav", 300)
    
    assert acc.withdrawFunds(200) == "funds was succesfully withdrawed"

def test_adding_funds():
    acc = BankAccount(1, "Stanislav", 200)
    
    assert acc.addFunds(-100) == "You cannot add a negative amount of money"
    assert acc.addFunds(100) == 300