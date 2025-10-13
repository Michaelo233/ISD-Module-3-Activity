"""This module defines the PaymentStrategy class."""

__author__ = "Michael Obikwere"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    @abstractmethod
    def process_payment(self, account: BillingAccount, payee:Payee, amount: float) ->str:
        
        pass