import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            document TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            account_number TEXT NOT NULL
        )''')
        self.conn.commit()
    
    def insert_user(self, name, document, date_of_birth, account_number):
        for register in self.c.execute('''SELECT * FROM users'''):
            if register[1] == name and register[2] == document:
                print("Usuário ja registrado")
                return None
        self.c.execute('''INSERT INTO users (name, document, date_of_birth, account_number) VALUES (?,?,?,?)''', (name, document, date_of_birth, account_number))
        self.conn.commit()
             
    
    def consult(self):
        self.c.execute('''SELECT * FROM users''')
        return [user for user in self.c.fetchall()]
    
    

# if __name__ == '__main__':
#     db = Database('teste', '1234567890', '123456789')
#     db.insert_user()
#     print(db.consult())