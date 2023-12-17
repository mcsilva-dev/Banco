from random import randint
from faker import Faker

class Bank:
    def __init__(self, create_date):
        fake = Faker(['pt_BR'])
        self.create_date = create_date
        self.balance = 0
        self.account_number = fake.credit_card_number()
    
    
        
    
    

