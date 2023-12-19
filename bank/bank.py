from random import randint
from faker import Faker

class Bank:
    """
    This class represents a bank account.

    Args:
        create_date (datetime): The date the bank account was created.
        balance (int): The current balance of the bank account.
        account_number (str): The unique account number of the bank account.

    Attributes:
        create_date (datetime): The date the bank account was created.
        balance (int): The current balance of the bank account.
        account_number (str): The unique account number of the bank account.
    """

    def __init__(self, create_date):
        """
        Initialize a new Bank instance.
        """
        fake = Faker(['pt_BR'])
        self.create_date = create_date
        self.balance = randint(0, 100000)
        self.account_number = fake.credit_card_number()
    
    
        
    
    

