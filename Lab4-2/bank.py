class BankAccount:
    # Class attribute
    branch_name = "KKU Complex"
    branch_number = 1724
    last_loan_number = 0
    last_saving_number = 0

    # Private class attributes
    # account types
    __type_saving = 1
    __type_loan = 2

    # Constructor
    def __init__(self, name, acc_type="saving", balance=0):
        self.name = name
        self.type = acc_type
        self.balance = balance

        if acc_type == "saving":
            BankAccount.last_saving_number += 1
            self.account_number = f"{BankAccount.branch_number}-{BankAccount.__type_saving}-{BankAccount.last_saving_number}"
        elif acc_type == "loan":
            BankAccount.last_loan_number += 1
            self.account_number = f"{BankAccount.branch_number}-{BankAccount.__type_loan}-{BankAccount.last_loan_number}"

    def print_customer(self):
        print("----- Customer Record -----")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Account type: {self.type}")
        print(f"Balance: {self.balance}")
        print("----- End Record -----\n")

    def change_branch_name(cls):
        cls.branch_name = input("Branch name: ")
    
    # Instance methods
    def deposit(self, amount=0):
        if self.type == "saving":
            self.balance += amount
    
    def withdraw(self, amount=0):
        if self.type == "saving":
            self.balance -= amount
    
    def pay_loan(self, amount=0):
        if self.type == "loan":
            self.balance += amount
    
    def get_loan(self, amount=0):
        if self.type == "loan" and self.balance >= -50000:
            self.balance -= amount
        
        #static
    def clac_interest(bal, int_rate, payment):
        print("----- Loan Plan -----")
        y = 0
        while True:
            y += 1
            bal = bal+(bal*(int_rate*0.01))
            if bal - payment < 0:
                payment = bal
            bala = bal - payment
            print(F"Year {y}: loan = {bal:.2f}   payment {payment:.2f}   bal = {bala:.2f}")
            bal = bala
            if bal == 0:
                print("----- End Plan -----")
                break


                

    