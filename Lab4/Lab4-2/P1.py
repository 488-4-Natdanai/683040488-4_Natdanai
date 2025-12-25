from bank import BankAccount

john = BankAccount("John", "saving", 500)
tim = BankAccount("Tim", "loan", -1_000_000)
sarah_saving = BankAccount("Sarah")

john.deposit(3000)
john.withdraw(3500)

tim.pay_loan(500_000)
tim.get_loan(3_000_000)

sarah_saving.deposit(50_000_000)
sarah_loan = BankAccount("Sarah", "loan", -100_000_000)
accounts = [john, tim, sarah_saving, sarah_loan]

for acc in accounts:
    acc.print_customer()
BankAccount.clac_interest(1000, 5, 100)
john.change_branch_name()
print(f"{john.name}'s branch is now {john.branch_name}")