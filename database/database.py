import sqlite3

class Database:
    """
    This class provides an interface to a database.
    """

    def __init__(self):
        """
        Initialize the database connection.
        """
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()

    def create_table(self):
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
    
    def insert_user(self, name: str, document: str, date_of_birth: str, phone_number: str, account_number: str, balance: int):
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

    def close(self):
        """
        Close the database connection.
        """
        return self.conn.close()
