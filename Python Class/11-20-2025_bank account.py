# Create a class "BankAccount"
class BankAccount:

    # Create a constructor with 2 parameters (owner and balance ) to create a bank account object
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private balance

    # Create a method called "balance" to show the balance of the account
    def balance(self):
        return self.__balance

    # Create a method called "deposit" to make a deposit with the amount in parameter.
    # If the deposit is inferior to zero, print "Deposit must be positive"
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive")
        else:
            self.__balance += amount
            print(f"Deposited ${amount}")

    # Create a method called "withdraw" to make a withdraw with the amount in the parameter.
    # If the withdraw is superior to the balance, print "Insufficient funds".
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}")


# infinite loop
account = BankAccount("Samone", 100)  # Example account

while True:
    # print a Menu
    print("\nMenu")
    print("1 - Check balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Logout")

    # enter your choice
    choice = input("Enter your choice: ")

    # if choice equal 1, Make a check balance
    if choice == "1":
        print(f"Your balance is: ${account.balance()}")

    # if choice equal 2, Make a deposit
    elif choice == "2":
        amount = int(input("Enter deposit amount: "))
        account.deposit(amount)

    # if choice equals 3, make a withdraw
    elif choice == "3":
        amount = int(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    # if choice equals 4, logout
    elif choice == "4":
        print("Logged out.")
        break

    # else, print(invalid choice!)
    else:
        print("Invalid choice!")


