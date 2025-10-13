"""This module defines the Payee enumeration."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from enum import Enum

class Payee(Enum):
    """Represents the receiver of a payment."""

    ELECTRICITY = 1
    """The electricity payee."""
    
    INTERNET = 2 
    """The internet payee."""
    
    TELEPHONE = 3
    """The telephone payee."""
