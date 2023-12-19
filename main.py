from client import Client
from database import Database
from faker import Faker
from functions import menu, add_client, name_consult
import re



if __name__ == '__main__':
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
                    add_client(client)
                case 2:
                    name = input('Digite o nome do cliente: '.upper())
                    name_consult(name)
                case 3:
                    break
        except (ValueError, IndexError):
            print('Opção inválida')
            continue
        
   