"""This module defines the PenaltyStrategy class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PenaltyStrategy(PaymentStrategy):
    """
    Penalty strategy class for bill payments not paid in full.
    """
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """
        Process payment that applies penalty to partially paid bills.

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
            penalty_charge = 10.0
            account.add_balance(payee, penalty_charge)
            balance = account.get_balance(payee)
            message = (f"Insufficient payment. Added penalty fee of "
                +f"${penalty_charge:.2f}. New balace: ${balance:,.2f}.")
        
        return message