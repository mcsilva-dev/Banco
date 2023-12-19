from client import Client
from database import Database
from faker import Faker
from functions import menu, add_client, name_consult, document_consult, update_balance
import re

if __name__ == '__main__':
    """
    This is the main function of the application. 
    It contains the main menu and the logic to execute the selected option.
    """
    options = ['Adicionar cliente', 'Consultar cliente', 'Realizar movimentação', 'Sair']
    while True:
        # calls the menu function and passes the options list as an argument
        menu(*options)
        try:
            # attempts to convert the user input to an integer and raises an exception if it is not possible
            option = int(input('Opção: '.upper()))
            if option <= 0 or option > len(options):
                raise IndexError
            # matches the selected option and executes the corresponding code block
            match option:
                case 1:
                    """
                    This function is used to add a new client to the database. It takes 
                    the user input for the client details and creates a new Client object. 
                    The object is then added to the database using the add_client function.
                    """
                    # creates a new Client object with the user input for the client details
                    client = Client(input('Nome do cliente: ').upper(),
                                    input('Documento: ').upper(),
                                    input('Data de nascimento: ').upper(),
                                    input('Numero de telefone (começar com +55): ').upper())
                    # adds the client object to the database using the add_client function
                    add_client(client)
                case 2:
                    """
                    This function is used to search for a client in the database based 
                    on their name. It takes the user input for the client name and searches 
                    the database using the name_consult function. If a client is found, 
                    their details are printed. If no client is found, a message is displayed.
                    """
                    # takes the user input for the client name and searches the database using the name_consult function
                    while True:
                        print('\nConsultar por;'.upper())
                        print('1 - NOME')
                        print('2 - DOCUMENTO')
                        try:
                            option = int(input('>> '))
                            assert option == 1 or option == 2
                            break
                        except AssertionError:
                            print('Opção inválida'.upper())
                            continue
                    match option:
                        case 1:
                            name = input('NOME: ')
                            data = name_consult(name)
                            if data:
                                for info in data:
                                    print(f"\nCliente: {info[1]}")
                                    print(f"Documento: {info[2]}")
                                    print(f"Data de nascimento: {info[3]}")
                                    print(f"Telefone: {info[4]}")
                                    print(f"Conta: {info[5]}")
                                    print(f"Saldo: {info[6]}\n")
                            else:
                                print('ERRO: CLIENTE NÃO LOCALIZADO NA BASE DE DADOS, OPERAÇÃO ABORTADA!\n')
                        case 2:
                            try:
                                document = input('NÚMERO DO DOCUMENTO: ')
                                assert re.compile(r'(\d{3}).(\d{3}).(\d{3})\-(\d{2})').fullmatch(document)
                                for info in document_consult(document):
                                    print(f"\nCliente: {info[1]}")
                                    print(f"Documento: {info[2]}")
                                    print(f"Data de nascimento: {info[3]}")
                                    print(f"Telefone: {info[4]}")
                                    print(f"Conta: {info[5]}")
                                    print(f"Saldo: {info[6]}\n")
                                break
                            except AssertionError:
                                print('Documento inválido (REF - xxx.xxx.xxx-xx), OPERAÇÃO ABORTADA!\n'.upper())
                case 3:
                    name = input('NOME: ')
                    data = name_consult(name)
                    if not data:
                        print('ERRO: CLIENTE NÃO LOCALIZADO NA BASE DE DADOS, OPERAÇÃO ABORTADA!\n')
                    else:
                        account = {}
                        for _ in data:
                            account['id'] = _[0]
                            account['name'] = _[1]
                            account['document'] = _[2]
                            account['date_of_birth'] = _[3]
                            account['phone_number'] = _[4]
                            account['account_number'] = _[5]
                            account['balance'] = _[6]
                        try:
                            account_number = input('NÚMERO DA CONTA: ')
                            print(account['account_number'])
                            assert account_number == account['account_number']

                        except AssertionError:
                            print('ERRO: NÚMERO DE CONTA DIVERGENTE, OPERAÇÃO ABORTADA!\n')
                        try:
                            balance = int(account['balance'])
                            value = int(input('VALOR DO SAQUE: '))
                            assert balance > value
                            balance -= value
                            print('SAQUE REALIZADO')
                            update_balance(balance, account['name'])
                        except AssertionError:
                            print('ERRO: VALOR EM CONTA INSUFICIENTE, OPERAÇÃO ABORTADA!')
                case 4:
                    break
        except (ValueError, IndexError):
            # prints an error message if the user input is not a valid option
            print('Opção inválida')
            continue