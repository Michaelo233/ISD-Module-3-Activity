"""This module defines the PartialPaymentStrategy class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PartialPaymentStrategy(PaymentStrategy):
    """
    Partial Payment Strategy class, that checks when partial payments
    are made to the users account.
    """
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """
        Process payment for partially made payments.

        Args:
            account (BillingAccount): The users billing account.
            payee (Payee): The bill the user is paying for.
            amount (float): The amount the user pays for the bill.

        Returns:
            message : formatted strings, depending on how much the user 
            paid for his bills. 
        """
        account.deduct_balance(payee, amount)
        balance = account.get_balance(payee)
        if balance <= 0:
            message = (f"Processed payment of ${amount:,.2f}. "
                       + f"New balance: ${balance:,.2f}.")
        else:
            message = (f"Partial payment of ${amount:,.2f} accepted. "
                       + f"New balance: ${balance:,.2f}.")
            
        return message