class BankAccount():
    account_number = 0
    account_holder = ""
    balance = 0
    def __init__(self, acc_num:int,  acc_hold:str, acc_bal:int) -> None:
        self.account_number = acc_num
        self.account_holder = acc_hold
        self.balance = acc_bal
    def printInfo(self):
        if(self):
            print(f"This account belongs to {self.account_holder}")
            print(f"Summ on balance is {round(self.balance)}")
            print(f"Account number is {self.account_number}")
        else:
            print("No data to print")
    def addFunds(self, funds:int):
        if(funds>=0):
            self.balance+=funds
            print("Funds were added")
            return self.balance
        else:
            return "You cannot add a negative amount of money"
    def withdrawFunds(self, funds:int) -> str:
        if(self.balance>0 and self.balance >= funds):
            self.balance -= funds
            return("funds was succesfully withdrawed")
        else:
            if(self.balance < funds):
                return ("You don`t have enough amount of money")
            else: 
                return("You don`t have money at all")
            
            
