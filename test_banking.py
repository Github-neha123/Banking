import unittest
from banking_system import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        acc = BankAccount("101", "John", 100)
        acc.deposit(50)
        self.assertEqual(acc.balance, 150)

    def test_withdraw(self):
        acc = BankAccount("102", "Jane", 200)
        acc.withdraw(50)
        self.assertEqual(acc.balance, 150)

    def test_insufficient_balance(self):
        acc = BankAccount("103", "Mike", 100)
        acc.withdraw(200)
        self.assertEqual(acc.balance, 100)

if __name__ == "__main__":
    unittest.main()