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
        

    def withdraw (self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Successfully withdrawn R {amount:.2f} ")
        else:
            print("Insufficient funds ")
        

    def display_balance(self):
        print("Current balance: ", self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate
        self.balance +=interest
        print(f"Interest of R{interest} added")

    def withdraw(self, amount):
        fee = 10
        if amount <= self.balance + fee:
            self.balance =self.balance - amount -fee
            print(f"Amount of {amount:.2f} withdrawn, Remaining balance",self.balance)
        else:
            print("Insufficient funds")

savings = SavingsAccount("Denzel")
savings.deposit(1000)
savings.add_interest(0.05) # Should add R50
savings.display_balance()  # Should be R1050
savings.withdraw(100)      # Should actually subtract R110 (100 + 10 fee)
savings.display_balance()