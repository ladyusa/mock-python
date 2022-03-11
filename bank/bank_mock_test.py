import unittest
from unittest.mock import Mock
from bank import BankAccount, Bank

class BankTest(unittest.TestCase):

    def test_transfer(self):

        # create mock objects
        mock_account_A = Mock()
        mock_account_B = Mock()
        mock_account_A.get_name.return_value = "A"
        mock_account_B.get_name.return_value = "B"

        # create CUT and setting up
        bank = Bank("Test Bank")
        bank.add_account(mock_account_A)
        bank.add_account(mock_account_B)

        # call method under test
        bank.transfer("A", "B", 1000)

        # ตรวจสอบที่ mock object
        mock_account_A.withdraw.assert_called_with(1000)
        mock_account_B.deposit.assert_called_with(1000)
