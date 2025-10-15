"""This module defines the Payment class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class Payment:
    """Payment class for implementing payment patterns for bill payment."""
    def __init__(self, strategy: PaymentStrategy):
        """
        Initializes the payment strategies.

        Args:
            strategy (PaymentStrategy): The payment strategies used for 
                different bill payments.

        Raises:
            ValueError: When strategy is Invalid.
        """
        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy.")
    
    def pay_bill(self, account: BillingAccount, payee: Payee, 
                 amount: float) -> str:
        """
        Pay bill method, that pays bill using different strategies.

        Args:
            account (BillingAccount): The users billing account.
            payee (Payee): The bill the user is paying for.
            amount (float): The amount the user pays for the bill.

        Returns:
            message : formatted strings, depending on the strategy used.
        """
        
        return self.__strategy.process_payment(account, payee, amount)