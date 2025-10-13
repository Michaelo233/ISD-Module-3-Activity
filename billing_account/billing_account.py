"""This module defines the BillingAccount class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from payee.payee import Payee

class BillingAccount():
    """A class to represent a user's balances for various utility bills.
    """

    def __init__(self):
        """Initializes a new instance of the BillingAccount class.
        
        All balances are initialized to zero.
        """
        self.__balances = {
            Payee.ELECTRICITY: 0.0,
            Payee.INTERNET: 0.0,
            Payee.TELEPHONE: 0.0
        }

    def add_balance(self, payee: Payee, amount: float):
        """Adds funds to the balance of a particular utility.

        Args:
            payee (Payee): The payee to which the funds will be applied.
            amount (float): The amount to apply to the balance.
        
        Raises: 
            ValueError: Raised when the amount is non-numeric.
        """

        if isinstance(amount, float):
            if payee in self.__balances:
                self.__balances[payee] += amount
        else:
            raise ValueError("Amount must be numeric.")
        

    def deduct_balance(self, payee: Payee, amount: float) -> None:
        """Deducts funds from the balance of a particular utility.

        Args:
            payee (Payee): The payee to which the funds will be 
                deducted.
            amount (float): The amount to deduct from the balance.
        
        Raises: 
            ValueError: Raised when the amount is non-numeric.
        """

        if isinstance(amount, float):
            if payee in self.__balances:
                self.__balances[payee] -= amount
        else:
            raise ValueError("Amount must be numeric.")

    def get_balance(self, payee: Payee) -> float | None:
        """Returns the balance of the specified utility.
        
        Args:
            utility (str): The utility of which the balance is 
                requested.
        
        Returns:
            float: The balance of the specified utility.
        """

        balance = None

        if payee in self.__balances:
            balance = self.__balances.get(payee, 0.0)

        return balance

    def __str__(self) -> str:
        """Returns a string representation of the BillingAccount object.
        
        Returns:
            string: A representation of the BillingAccount object.
        """
        
        return (f"Electricity Balance: ${self.__balances[Payee.ELECTRICITY]:,.2f}\n"
                f"Internet Balance: ${self.__balances[Payee.INTERNET]:,.2f}\n"
                f"Telephone Balance: ${self.__balances[Payee.TELEPHONE]:,.2f}")
