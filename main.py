from client import Client
from functions import menu, add_client, name_consult, document_consult, movimentation, history_movimentation

if __name__ == '__main__':
    """
    This is the main function of the application. 
    It contains the main menu and the logic to execute the selected option.
    """
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
                    """
                    This function is used to add a new client to the database. It takes 
                    the user input for the client details and creates a new Client object. 
                    The object is then added to the database using the add_client function.
                    """
                    # creates a new Client object with the user input for the client details
                    print()
                    print("ADICIONANDO NOVO CLIENTE".center(50, '-'))
                    try:
                        client = Client(input('NOME DO CLIENTE: '),
                                        input('DOCUMENTO: '),
                                        input('DATA DE NASCIMENTO: '),
                                        input('NÚMERO DE TELEFONE (COMEÇAR COM +55): '),
                                        int(input('DEPOSITO INICIAL: ')))
                    except Exception as error:
                        print('ERRO: DADOS INCOMPATIVEIS, OPERAÇÃO ABORTADA!')
                        continue
                    # adds the client object to the database using the add_client function
                    add_client(client, 'database')
                    print('CLIENTE ADICIONADA A BASE DE DADOS\n')
                case 2:
                    """
                    This function is used to search for a client in the database based 
                    on their name. It takes the user input for the client name and searches 
                    the database using the name_consult function. If a client is found, 
                    their details are printed. If no client is found, a message is displayed.
                    """
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
                                print()
                                print('RESULTADO DA BUSCA'.center(50, '-'))
                                print(f"\nid: {client['id']}")
                                print(f"Cliente: {client['name']}")
                                print(f"Documento: {client['document']}")
                                print(f"Data de nascimento: {client['date_of_birth']}")
                                print(f"Telefone: {client['phone_number']}\n")
                            else:
                                print('ERRO: CLIENTE NÃO LOCALIZADO NA BASE DE DADOS, OPERAÇÃO ABORTADA!\n')
                        case 2:
                            try:
                                document = input('NÚMERO DO DOCUMENTO: ')
                                data = document_consult(document, 'database')
                                if data:
                                    client = data[0]
                                    print()
                                    print('RESULTADO DA BUSCA'.center(50, '-'))
                                    print(f"\nid: {client['id']}")
                                    print(f"Cliente: {client['name']}")
                                    print(f"Documento: {client['document']}")
                                    print(f"Data de nascimento: {client['date_of_birth']}")
                                    print(f"Telefone: {client['phone_number']}")
                                    continue
                                print('ERRO: DOCUMENTO INVÁLIDO, OPERAÇÃO ABORTADA!\n')
                            except AssertionError:
                                print('Documento inválido (REF - xxx.xxx.xxx-xx), OPERAÇÃO ABORTADA!\n'.upper())
                case 3:
                    print()
                    print("MENU DE OPERAÇÕES".center(50, '-'))
                    print("\n1 - SAQUE\n2 - DEPOSITO")
                    try:
                        opr_type = int(input('>> '))
                        assert opr_type == 1 or opr_type == 2
                        opr_type = 'WITHDRAW' if opr_type == 1 else 'DEPOSIT'
                    except AssertionError:
                        print('ERRO: OPERAÇÃO INVÁLIDA, OPERAÇÃO ABORTADA!\n')
                        continue
                    name = input('NOME: ')
                    data = name_consult(name, 'database')
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
                            print('OPERAÇÃO REALIZADA')
                            movimentation(account['name'], 'database', value, opr_type)
                        except AssertionError:
                            print('ERRO: VALOR EM CONTA INSUFICIENTE, OPERAÇÃO ABORTADA!\n')
                case 4:
                    print()
                    print('HISTÓRICO DE MOVIMENTAÇÕES'.center(50, '-'))
                    document = input('DOCUMENTO: ')
                    account = input('NUMERO DA CONTA: ')
                    results = history_movimentation(document, account, 'database')
                    if results:
                        for _ in results:
                            print('-' * 50)
                            print(f'ID: {_["id_movimentation"]}')
                            print(f'TIPO: {_["movimentation_type"]}')
                            print(f'VALOR: R${_["value"]}')
                            print(f"DATA: {_['date_movimentation']}")
                            print('-' * 50)
                        continue
                    print("ERRO: NENHUMA MOVIMENTAÇÃO ENCONTRADA, OPERAÇÃO ABORTADA!")
                case 5:
                    break
        except (ValueError, IndexError):
            # prints an error message if the user input is not a valid option
            print('Opção inválida')
            continue
