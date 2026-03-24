class bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.deposit(amount)
            return True
        return False

    def __str__(self):
        return f"Account Name: {self.name}, Balance: {self.balance}"


class bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, initial_balance):
        account = bank_account(name, initial_balance)
        self.accounts.append(account)
        return account

    def find_account(self, name):
        if name is None:
            return None
        name = name.strip().lower()
        for account in self.accounts:
            if account.name.strip().lower() == name:
                return account
        return None
    
    def transfer(self, from_account_name, to_account_name, amount):
        from_account = self.find_account(from_account_name)
        to_account = self.find_account(to_account_name)

        if from_account and to_account:
            return from_account.transfer(amount, to_account)
        return False
    


my_bank = bank()
alice_account = my_bank.create_account("Alice", 1000)
bob_account = my_bank.create_account("Bob", 500)


print("select an option:")
print("1. Deposit")
print("2. Withdrawal")
print("3. Transfer")
option = input("Enter option number: ")

if option == "1":
    amount = int(input("Enter deposit amount: "))
    alice_account.deposit(amount)
    print(alice_account)
elif option == "2":
    amount = int(input("Enter withdrawal amount: "))
    if alice_account.withdrawal(amount):
        print("Withdrawal successful.")
    else:
        print("Insufficient funds.")
    print(alice_account)
elif option == "3":
    amount = int(input("Enter transfer amount: "))
    transfer_to = input("Enter recipient name: ")
    recipient = my_bank.find_account(transfer_to)
    if not recipient:
        print("Recipient not found.")
    elif my_bank.transfer("Alice", transfer_to, amount):
        print("Transfer successful.")
    else:
        print("Transfer failed.")
    print(alice_account)
    print(bob_account)
else:
    print("Invalid option.")