class BankAccount:
    
    min_balance = 1000

    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if self.balance>=BankAccount.min_balance:
            self.balance += amount
            print("deposited successfully.")
            print("Updated Balance:",self.balance)
        else:
            print("Invalid")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.min_balance and amount>0:
            self.balance -= amount
            print("withdrawn successfully")
            print("Remaining Balance:",self.balance)
        else:
            print("Withdrawal denied")
   
    def display_details(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.acc_no)
        print("Balance:", self.balance)
        print("Minimum Balance:", BankAccount.min_balance)
   
    @classmethod
    def update_min_balance(cls, new_balance):
        cls.min_balance = new_balance
        print("Minimum balance updated to:", cls.min_balance)

acc1 = BankAccount("Harshini", 12345, 5000)
acc1.deposit(2000)
acc1.withdraw(3000)
acc1.display_details()
BankAccount.update_min_balance(2000)
