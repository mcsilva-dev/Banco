from bank import Bank
from database import Database
from datetime import datetime
import re


class Client(Bank):
    """
    This class represents a client of a bank. It inherits from the Bank class, which provides the basic functionality of
    a bank account.

    Args:
        name (str): The name of the client.
        document_number (str): The document number of the client, in the format XXX.XXX.XXX-XX.
        date_of_birth (str): The date of birth of the client, in the format YYYY-MM-DD.
        phone_number (str): The phone number of the client, in the format +55xxxxxxxxx.

    Raises:
        AssertionError: If the document number, date of birth, or phone number is not in the correct format.

    Attributes:
        name (str): The name of the client.
        document_number (str): The document number of the client, in the format XXX.XXX.XXX-XX.
        date_of_birth (str): The date of birth of the client, in the format YYYY-MM-DD.
        phone_number (str): The phone number of the client, in the format +55xxxxxxxxx.
        accounts (list): A list of accounts held by the client.
    """

    def __init__(self, name, document_number, date_of_birth, phone_number, value):
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
        super().__init__(datetime.now().strftime("%d/%m/%Y"), value)
