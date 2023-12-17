from client import Client
from database import Database
from faker import Faker
import re



if __name__ == '__main__':
    fake = Faker(['pt_BR'])
    Faker.seed(0)
    for _ in range(100):
        client = Client(fake.name(), fake.cpf(), str(fake.date_of_birth()), fake.cellphone_number()).create_account()
        db = Database()
        db.create_table()
        db.insert_user(client.name, client.document_number, client.date_of_birth, client.phone_number, client.account_number, client.balance)
        db.close()
    db = Database()
    for info in db.consult():
        print(f"Cliente: {info[1]}")
        print(f"Documento: {info[2]}")
        print(f"Data de nascimento: {info[3]}")
        print(f"Telefone: {info[4]}")
        print(f"Conta: {info[5]}")
        print(f"Saldo: {info[6]}\n\n")