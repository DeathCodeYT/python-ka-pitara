# Advance Bank Account Project

class BankAccount:
    _accounts = {}

    def __new__(cls,account_number,account_holder,initial_balance=0):
        if account_number in cls._accounts:
            print(f"Account {account_number} already exists. Returning Existing instance")
            return cls._accounts[account_number]
        else:
            instance = super().__new__(cls)
            cls._accounts[account_number] = instance
            return instance

    def __init__(self,account_number,account_holder,initial_balance=0):
        if hasattr(self,"_initialized"):
            return 
        else:
            self.account_number = account_number
            self.account_holder = account_holder
            self.balance = initial_balance
            self._initialized = True
            print(f"Account {self.account_number} for {self.account_holder} created with balance: {self.balance}")
    
    def deposit(self,amount):
        if amount < 0:
            print("Deposite amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self,amount):
        if amount < 0:
            print("Deposite amount must be positive.")
        elif self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance: {self.balance}")

    def get_balance(self):
        print(f"Current balance for A/C {self.account_number}({self.account_holder}): {self.balance}")
        
    def __repr__(self):
        return f"BankAccount(A/C): {self.account_number}, Holder:{self.account_holder}, Balance:{self.balance}"

    @classmethod
    def create_new_account(cls,acc_num,holder_name,initial_amt=0):
        print(f"Using classmethod to create account: {acc_num}")
        return cls(acc_num,holder_name,initial_amt)
    

ac1 = BankAccount(1001,"Aryan",1000)
ac1.deposit(1200)

ac2 = BankAccount(1002,"Vansh")
ac2.deposit(3000)

ac1.withdraw(976)
ac2.withdraw(850)

ac1.get_balance()
ac2.get_balance()

ac3 = BankAccount(1001,"Rupali",500000)
ac3.get_balance()

ac4 = BankAccount.create_new_account(1002,"Deathcode",1000)

print(ac1)
print(ac2)
print(ac3)
print(ac4)
