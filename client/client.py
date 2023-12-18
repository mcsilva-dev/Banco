from bank import Bank
from database import Database
from datetime import datetime
import re

class Client(Bank):
    def __init__(self, name, document_number, date_of_birth, phone_number):
        assert re.compile(r'(\d{3}).(\d{3}).(\d{3})\-(\d{2})').fullmatch(document_number), 'Documento inválido'
        assert re.compile(r'(\d{4})\-(\d{2})\-(\d{2})').fullmatch(date_of_birth), 'Data de nascimento inválida'
        assert re.compile(r'^(\+55).*$').fullmatch(phone_number), 'Formato de telefone inválido'
        
        self.name = name
        self.document_number = document_number
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        
    def create_account(self):
        super().__init__(f'{datetime.now().day}/{datetime.now().month}/{datetime.now().year}')
        return self
        
