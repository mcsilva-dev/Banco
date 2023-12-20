import sqlite3
from datetime import datetime


class Database:
    """
    This class provides an interface to a database.
    """

    def __init__(self):
        """
        Initialize the database connection.
        """
        self.conn = sqlite3.connect('teste.db')
        self.c = self.conn.cursor()

    def create_client_table(self):
        """
        Create the users table if it does not already exist.
        """
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            document TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            account_number TEXT NOT NULL,
            balance INTEGER
        )''')
        self.conn.commit()

    def create_movimentation_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS movimentations (
            id_movimentation INTEGER PRIMARY KEY,
            client_name TEXT NOT NULL,
            id_client INTEGER,
            value INTEGER,
            date_movimentation TEXT NOT NULL,
            FOREIGN KEY (id_client) REFERENCES users (id_client)
        )''')
        self.conn.commit()

    def insert_user(self, name: str, document: str, date_of_birth: str, phone_number: str, account_number: str,
                    balance: int):
        """
        Insert a new user into the database.

        Args:
            name (str): The name of the user.
            document (str): The document number of the user.
            date_of_birth (str): The date of birth of the user.
            phone_number (str): The phone number of the user.
            account_number (str): The account number of the user.
            balance (int): The balance of the user.

        Returns:
            None: If the user is inserted successfully.
            str: If the user is not inserted because a user with the same name and document number already exists.
        """
        for register in self.c.execute('''SELECT * FROM users'''):
            if register[1] == name and register[2] == document:
                print("Usuário ja registrado")
                return None
        self.c.execute('''INSERT INTO users (name, document, date_of_birth, phone_number, account_number, balance) 
                       VALUES (?,?,?,?,?,?)''',
                       (name, document, date_of_birth, phone_number, account_number, balance))
        self.conn.commit()

    def insert_movimentation(self, id_client, name: str, value: float, date):
        self.c.execute('''INSERT INTO movimentations (client_name, id_client, value, date_movimentation) 
                        VALUES (?,?,?,?)
                        ''',
                       (name, id_client, value, date, ))
        self.conn.commit()

    def name_consult(self, name):
        """
        Retrieve a list of users with the specified name from the database.

        Args:
            name (str): The name of the user.

        Returns:
            list: A list of users with the specified name.
        """
        self.c.execute('''SELECT * FROM users WHERE name = ?''', (name,))
        return [user for user in self.c.fetchall()]

    def document_consult(self, document):
        self.c.execute('''SELECT * FROM users WHERE document = ?''', (document,))
        return [user for user in self.c.fetchall()]

    def update_balance(self, new_balance, name):
        self.c.execute('''UPDATE users SET balance = ? WHERE name = ?''', (new_balance, name,))
        self.conn.commit()

    def consult_movimentation(self):
        self.c.execute('''SELECT users.name, movimentations.id_movimentation, movimentations.value, 
                        movimentations.date_movimentation 
                        FROM users 
                        JOIN movimentations on users.id = movimentations.id_client''')
        return [data for data in self.c.fetchall()]

    def close(self):
        """
        Close the database connection.
        """
        return self.conn.close()

if __name__ == '__main__':
    db = Database()
    db.create_client_table()
    db.create_movimentation_table()
    db.insert_user('Geraldo Luiz', document='109.876.543-21', phone_number='+55 33 9 84526418', account_number='77777',
                   date_of_birth='05/10/1990', balance=10000)
    db.insert_user('Paulo Jose', document='123.456.789-10', phone_number='+55 33 9 98451987', account_number='55566',
                   date_of_birth='22/06/1999', balance=15000)
    db.insert_movimentation(1, 'Geraldo Luiz', value=1200, date=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    data = db.consult_movimentation()
    print(data)
