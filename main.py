from client import Client
from database import Database
from faker import Faker
import re


def menu(*args):
    print('MENU'.center(50, '-'))
    print("\nESCOLHA UMA OPÇÃO:\n")
    for index, value in enumerate(args):
        print(f'{index + 1} - {value.upper()}')

def consulta(name):
    db = Database()
    for info in db.name_consult(name):
        print(f"Cliente: {info[1]}")
        print(f"Documento: {info[2]}")
        print(f"Data de nascimento: {info[3]}")
        print(f"Telefone: {info[4]}")
        print(f"Conta: {info[5]}")
        print(f"Saldo: {info[6]}\n\n")

def adicionar_client(args):
    db = Database()
    db.create_table()
    db.insert_user(args.name, args.document_number, args.date_of_birth, args.phone_number, args.account_number, args.balance)
    db.close()



if __name__ == '__main__':
    # fake = Faker(['pt_BR'])
    # Faker.seed(0)
    # for _ in range(100):
    #     client = Client(fake.name(), fake.cpf(), str(fake.date_of_birth()), fake.cellphone_number()).create_account()
    #     db = Database()
    #     db.create_table()
    #     db.insert_user(client.name, client.document_number, client.date_of_birth, client.phone_number, client.account_number, client.balance)
    #     db.close()
    options = ['Adicionar cliente', 'Consultar cliente', 'Sair']
    while True:
        menu(*options)
        try:
            option = int(input('Digite a opção: '.upper()))
            if option <= 0 or option > len(options):
                raise IndexError
            match option:
                case 1:
                    client = Client(input('Digite o nome do cliente: '.upper()), 
                                    input('Digite o documento do cliente: '.upper()), 
                                    input('Digite a data de nascimento do cliente: '.upper()), 
                                    input('Digite o telefone do cliente: '.upper())).create_account()
                    adicionar_client(client)
                case 2:
                    name = input('Digite o nome do cliente: '.upper())
                    consulta(name)
                case 3:
                    break
        except (ValueError, IndexError):
            print('Opção inválida')
            continue
        
   