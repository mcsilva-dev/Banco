from client import Client
from database import Database
import re



if __name__ == '__main__':
    client = Client('Maria', '123.456.789-10', '29/08/1990')
    client.create_account()
    client.database_register()
    client = Client('Jose', '109.876.543-21', '10/06/1984')
    client.create_account()
    client.database_register()
    db = Database()
    for info in db.consult():
        print(f"Cliente: {info[1]}")
        print(f"Documento: {info[2]}")
        print(f"Data de nascimento: {info[3]}")
        print(f"Conta: {info[4]}\n\n")
    db.conn.close()