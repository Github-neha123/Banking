class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" Deposited ${amount:.2f}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(" Insufficient balance.")
        else:
            self.balance -= amount
            print(f" Withdrew ${amount:.2f}")

    def check_balance(self):
        print(f" Current Balance: ${self.balance:.2f}")

    def display_details(self):
        print("\n Account Details")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            print(" Account already exists.")
            return

        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Deposit: "))
        self.accounts[acc_no] = BankAccount(acc_no, name, balance)
        print(" Account created successfully!")

    def get_account(self):
        acc_no = input("Enter Account Number: ")
        account = self.accounts.get(acc_no)
        if not account:
            print(" Account not found.")
        return account


def main():
    bank = Bank()

    while True:
        print("\n BANKING SYSTEM MENU")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. View Account Details")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            account = bank.get_account()
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)

        elif choice == "3":
            account = bank.get_account()
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)

        elif choice == "4":
            account = bank.get_account()
            if account:
                account.check_balance()

        elif choice == "5":
            account = bank.get_account()
            if account:
                account.display_details()

        elif choice == "6":
            print(" Thank you for using the Banking System.")
            break

        else:
            print(" Invalid option. Please try again.")


if __name__ == "__main__":
    main()