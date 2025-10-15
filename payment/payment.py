"""This module defines the Payment class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class Payment:
    def __init__(self, strategy: PaymentStrategy):
        
        if isinstance(strategy, PaymentStrategy):
            self.__strategy = strategy
        else:
            raise ValueError("Invalid Strategy.")
    
    def pay_bill(self, account: BillingAccount, payee: Payee, 
                 amount: float):
        
        return self.__strategy.process_payment(account, payee, amount)