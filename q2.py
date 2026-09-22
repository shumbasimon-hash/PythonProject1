class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance   # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Current balance:", self.__balance)


# Create an account
account = BankAccount("ACC001", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(300)

# Display balance
account.display_balance()

# Direct modification is not allowed in the normal way
# account.__balance = 50000