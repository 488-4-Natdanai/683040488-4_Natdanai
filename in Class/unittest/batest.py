# test_bank_account.py
import unittest
from ba import BankAccount

class BankAccountTest(unittest.TestCase):
    def setUp(self):
        # Run before each test
        self.account = BankAccount(initial_balance=1000)

    def tearDown(self):
        # Run after each test
        self.account.close()

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

        # Test for Bug 1: Should not allow negative initial balance
        with self.assertRaises(ValueError):
            negative_account = BankAccount(initial_balance=-100)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_negative_amount(self):
        # Test for Bug 2: Should not allow negative deposits
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdrawal(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdrawal_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_withdrawal_insufficient_funds(self):
        # Test for Bug 3: Should not allow withdrawals exceeding balance
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_closed_account_deposit(self):
        self.account.close()
        with self.assertRaises(ValueError):
            self.account.deposit(500)

    def test_closed_account_withdrawal(self):
        self.account.close()
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_account_close_resets_balance(self):
        # Test for Bug 4: Balance should be zero after closing
        self.account.close()
        self.assertEqual(self.account.balance, 0)


if __name__ == "__main__":
    unittest.main()
