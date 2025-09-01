
class BankAccount:
    """
    A simple BankAccount class to manage deposits, withdrawals, and balance checks.
    """

    def __init__(self, name, balance=0.0):
        """
        Initialize the BankAccount with account holder's name and initial balance.

        Args:
            name (str): The name of the account holder.
            balance (float, optional): The starting balance. Defaults to 0.0.
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be positive.

        Returns:
            float: The new balance after deposit.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return self.balance
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.

        Args:
            amount (float): The amount to withdraw. Must be positive and <= balance.

        Returns:
            float: The new balance after withdrawal.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return self.balance
        if amount > self.balance:
            print("Insufficient funds.")
            return self.balance
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")
        return self.balance

    def get_balance(self):
        """
        Check the current account balance.

        Returns:
            float: The current balance.
        """
        print(f"Current balance is {self.balance}.")
        return self.balance

# --- Analysis and Explanation ---

# The BankAccount class models a simple bank account with basic operations.
# - The __init__ method initializes the account with a name and an optional starting balance.
# - The deposit method adds a positive amount to the balance, with input validation.
# - The withdraw method subtracts a positive amount from the balance if sufficient funds exist.
# - The get_balance method returns the current balance.
# Each method includes print statements for user feedback and returns the updated balance.
# This class can be extended with more features as needed.

# Example usage of the BankAccount class
if __name__ == "__main__":
    # Create a new bank account for Alice with an initial balance of 1000
    account = BankAccount("Alice", 1000)
    
    # Deposit 500
    account.deposit(500)
    
    # Withdraw 200
    account.withdraw(200)
    
    # Check balance
    account.get_balance()
