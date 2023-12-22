from client import Client
from random import randint
from create_database import create_database
from functions import menu, add_client, name_consult, document_consult, transactions, history_transactions, show_results
import os

if __name__ == '__main__':
    if not os.path.isfile('database.db'):
        print('INICIANDO... ')
        create_database()
    options = ['Adicionar cliente', 'Consultar cliente', 'Realizar movimentação', 'histórico de movimentações', 'Sair']
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
                    # creates a new Client object with the user input for the client details
                    print()
                    print("ADICIONANDO NOVO CLIENTE".center(50, '-'))
                    try:
                        account_number = ''
                        for _ in range(16):
                            account_number += str(randint(0,9))
                        client = Client(input('NOME DO CLIENTE: '),
                                        input('DOCUMENTO: '),
                                        input('DATA DE NASCIMENTO: '),
                                        input('NÚMERO DE TELEFONE (COMEÇAR COM +55): '),
                                        int(input('DEPOSITO INICIAL: ')),
                                        account_number)
                    except Exception as error:
                        print('ERRO: DADOS INCOMPATIVEIS, OPERAÇÃO ABORTADA!')
                        continue
                    # adds the client object to the database using the add_client function
                    add_client(client, 'database.db')
                    print('CLIENTE ADICIONADO(A) AO BANCO DE DADOS\n')
                case 2:
                    # takes the user input for the client name and searches the database using the name_consult function
                    while True:
                        print()
                        print('BUSCAR CLIENTE POR'.center(50, '-'))
                        print('\n1 - NOME\n2 - DOCUMENTO')
                        print()
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
                            data = name_consult(name, 'database')
                            if data:
                                client = data[0]
                                show_results(client)
                            else:
                                print('ERRO: CLIENTE NÃO LOCALIZADO NA BASE DE DADOS, OPERAÇÃO ABORTADA!\n')
                        case 2:
                            try:
                                document = input('NÚMERO DO DOCUMENTO: ')
                                data = document_consult(document, 'database')
                                if data:
                                    client = data[0]
                                    show_results(client)
                                    continue
                                print('DOCUMENTO NÃO ENCONTRADO NA BASE DE DADOS!\n')
                            except AssertionError:
                                print('Documento inválido (REF - xxx.xxx.xxx-xx), OPERAÇÃO ABORTADA!\n'.upper())
                case 3:
                    print()
                    print("MENU DE OPERAÇÕES".center(50, '-'))
                    print("\n1 - SAQUE\n2 - DEPOSITO")
                    try:
                        opr_type = int(input('>> '))
                        assert opr_type == 1 or opr_type == 2
                        opr_type = 'SAQUE' if opr_type == 1 else 'DEPOSITO'
                    except AssertionError:
                        print('ERRO: OPERAÇÃO INVÁLIDA, OPERAÇÃO ABORTADA!\n')
                        continue
                    document = input('DOCUMENTO (xxx.xxx.xxx-xx): ')
                    data = document_consult(document, 'database')
                    if not data:
                        print('ERRO: CLIENTE NÃO LOCALIZADO NA BASE DE DADOS, OPERAÇÃO ABORTADA!\n')
                    else:
                        account = data[0]
                        try:
                            account_number = input('NÚMERO DA CONTA: ')
                            assert account_number == account['account_number']
                        except AssertionError:
                            print('ERRO: NÚMERO DE CONTA DIVERGENTE, OPERAÇÃO ABORTADA!\n')
                            continue
                        try:
                            balance = int(account['balance'])
                            value = int(input('VALOR: '))
                            assert balance > value
                            balance -= value
                            print('OPERAÇÃO REALIZADA COM SUCESSO!')
                            transactions(account['name'], 'database', value, opr_type)
                        except AssertionError:
                            print('ERRO: VALOR EM CONTA INSUFICIENTE, OPERAÇÃO ABORTADA!\n')
                case 4:
                    print()
                    print('HISTÓRICO DE MOVIMENTAÇÕES'.center(50, '-'))
                    document = input('\nDOCUMENTO (xxx.xxx.xxx-xx): ')
                    account = input('NUMERO DA CONTA: ')
                    results = history_transactions(document, account, 'database')
                    if isinstance(results, list):
                        if len(results) > 0:
                            for _ in results:
                                print('-' * 50)
                                print(f'ID: {_["id_transaction"]}')
                                print(f'TIPO: {_["transaction_type"]}')
                                print(f'VALOR: R${_["value"]}')
                                print(f"DATA: {_['date_transaction']}")
                                print('-' * 50)
                        else:
                            print('\nNENHUMA OPERAÇÃO REGISTRADA. \n')
                        continue
                    elif results == 1:
                        print('ERRO: DOCUMENTO INVÁLIDO, OPERAÇÃO ABORTADA!\n')
                        continue
                    print("ERRO: NENHUMA MOVIMENTAÇÃO ENCONTRADA, OPERAÇÃO ABORTADA!\n")
                case 5:
                    break
        except (ValueError, IndexError):
            # prints an error message if the user input is not a valid option
            print('Opção inválida')
            continue
