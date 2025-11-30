class BankAccount:
    def __init__ (self, account_holder):
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit (self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited R{amount:.2f}")
        else:
            print("The amount must be greater than zero")
        pass

    def withdraw (self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Successfully withdrawn R {amount:.2f} ")
        else:
            print("Insufficient funds ")
        pass

    def display_balance(self):
        print("Current balance: ", self.balance)
        pass

my_account = BankAccount("Denzel")
my_account.deposit(1000)
my_account.withdraw(500)
my_account.deposit(75)
my_account.withdraw(6000)
my_account.display_balance()


        

