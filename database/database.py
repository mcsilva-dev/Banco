import sqlite3


class Database:

    def __init__(self, database):
        self.conn = sqlite3.connect(database + '.db')
        self.c = self.conn.cursor()

    def create_client_table(self):
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
            movimentation_type TEXT NOT NULL,
            value INTEGER,
            date_movimentation TEXT NOT NULL,
            FOREIGN KEY (id_client) REFERENCES users (id_client)
        )''')
        self.conn.commit()

    def insert_user(self, name: str, document: str, date_of_birth: str, phone_number: str, account_number: str,
                    balance: int):
        for register in self.c.execute('''SELECT * FROM users'''):
            if register[1] == name and register[2] == document:
                print("Usuário ja registrado")
                return None
        self.c.execute('''INSERT INTO users (name, document, date_of_birth, phone_number, account_number, balance) 
                       VALUES (?,?,?,?,?,?)''',
                       (str(name), str(document), str(date_of_birth), str(phone_number), str(account_number), int(balance)))
        self.conn.commit()

    def insert_movimentation(self, id_client, name: str, movimentation_type, value: float, date):
        self.create_movimentation_table()
        try:
            balance = self.name_consult(name)
            assert len(balance) > 0
            balance = balance[0]['balance']
        except AssertionError:
            return 1
        if movimentation_type == 'WITHDRAW':
            try:
                assert balance - value >= 0
                balance -= value
            except AssertionError:
                return 2
            self.update_balance(new_balance=balance, name=name)
        elif movimentation_type == 'DEPOSIT':
            balance += value
            self.update_balance(new_balance=balance, name=name)
        self.c.execute('''INSERT INTO movimentations (client_name, id_client, movimentation_type,
                        value, date_movimentation) 
                        VALUES (?,?,?,?,?)
                        ''',
                       (name, id_client, movimentation_type, value, date,))
        self.conn.commit()

    def name_consult(self, name):
        results = self.c.execute('''SELECT * FROM users WHERE name = ?''', (name, ))
        colums = [description[0] for description in results.description]
        return [dict(zip(colums, line)) for line in self.c.fetchall()]

    def document_consult(self, document):
        results = self.c.execute('''SELECT * FROM users WHERE document = ?''', (document,))
        colums = [description[0] for description in results.description]
        return [dict(zip(colums, line)) for line in self.c.fetchall()]

    def update_balance(self, new_balance, name):
        self.c.execute('''UPDATE users SET balance = ? WHERE name = ?''', (new_balance, name,))
        self.conn.commit()

    def consult_movimentation(self, id):
        results = self.c.execute('''SELECT users.name, movimentations.id_movimentation, movimentations.movimentation_type,
                        movimentations.value, movimentations.date_movimentation 
                        FROM users 
                        JOIN movimentations on users.id = movimentations.id_client
                        WHERE id = ?''', (id,))
        if results:
            columns = [column[0] for column in results.description]
            d = results.fetchall()
            d = [dict(zip(columns, row)) for row in d]
            return d
        else:
            return None

    def close(self):
        return self.conn.close()
