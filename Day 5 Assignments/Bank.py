s = input("Enter your name: ")
balance = 0


class bank_info():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("Hello", owner, "! Welcome to your bank account!")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited! ", amount)
        print("\n Current Balance: ", self.balance)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))

        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
            print("\n Current Balance: ", self.balance)

        else:
            print("\n Insufficient balance  ")

    def again(self):
        repeat = input("\nDo you want to make more transactions?(y/n): ")
        if repeat == 'y':
            s.deposit()
            s.withdraw()
            s.again()


s = bank_info(s, balance)
s.deposit()
s.withdraw()
s.again()

