"""This module defines the PartialPaymentStrategy class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from patterns.strategy.payment_strategy import PaymentStrategy
from billing_account.billing_account import BillingAccount

class PartialPaymentStrategy(PaymentStrategy):

    def process_payment(self, account, payee, amount):
        BillingAccount.deduct_balance(payee, amount)
        balance = BillingAccount.get_balance(payee, amount)
        if balance <= 0:
            message = (f"Processed payment of ${amount:,.2f}. "
                       + f"New balance: ${balance:,.2f}.")
        else:
            message = (f"Partial payment of ${amount:,.2f} accepted. "
                       + f"New balance: ${balance:,.2f}.")
            
        return message