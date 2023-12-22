from bank import Bank
from datetime import datetime
import re


class Client(Bank):
    def __init__(self, name, document_number, date_of_birth, phone_number, value, account_number):
        """
        Initalizes a new Client object.
        """
        assert re.compile(r'(\d{3}).(\d{3}).(\d{3})-(\d{2})').fullmatch(document_number), 'Documento inválido'
        assert re.compile(r'(\d{2})/(\d{2})/(\d{4})').fullmatch(date_of_birth), 'Data de nascimento inválida'
        assert re.compile(r'^(\+55).*$').fullmatch(phone_number), 'Formato de telefone inválido'

        self.name = name
        self.document_number = document_number
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        super().__init__(datetime.now().strftime("%d/%m/%Y"), value, account_number)
