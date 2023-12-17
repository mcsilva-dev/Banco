from bank import Bank
from database import Database
from datetime import datetime
import re

class Client(Bank):
    def __init__(self, name, document_number, date_of_birth, phone_number):
        self.name = name
        if re.compile(r'(\d{3}).(\d{3}).(\d{3})\-(\d{2})').fullmatch(document_number):
            self.document_number = document_number
        else:
            raise ValueError('Documento inválido')
        if re.compile(r'(\d{4})\-(\d{2})\-(\d{2})').fullmatch(date_of_birth):
            self.date_of_birth = date_of_birth
        else:
            raise ValueError('Data de nascimento inválida')
        if re.compile(r'^(\+55).*$').fullmatch(phone_number):
            self.phone_number = phone_number
        else:
            raise ValueError("Formato de telefone inválido")
        
    def create_account(self):
        super().__init__(f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}')
        return self
        
