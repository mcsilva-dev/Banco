from random import randint

class Bank:
    def __init__(self, create_date):
        self.create_date = create_date
        self.balance = 0
        self.account_number = ''.join([str(randint(0, 9)) for number in range(8)])
        
    
    

