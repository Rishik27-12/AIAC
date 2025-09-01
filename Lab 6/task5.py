class BankAccount:
    def __init__(self, name, balance=0):
        """
        Initialize a new BankAccount instance.

        Args:
            name (str): The name of the account holder.
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw. Must be positive and <= balance.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """
        Return the current account balance.

        Returns:
            float: The current balance.
        """
        print(f"Current balance: {self.balance}")
        return self.balance

# Analysis:
# - The BankAccount class encapsulates account holder's name and balance.
# - deposit() adds money to the account, checking for positive amounts.
# - withdraw() removes money, ensuring sufficient funds and positive amounts.
# - get_balance() returns and prints the current balance.
# - All methods include basic input validation and user feedback.

# Example usage:
account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.get_balance()