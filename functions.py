from database import Database

def menu(*args):
    print('MENU'.center(50, '-'))
    print("\nESCOLHA UMA OPÇÃO:\n")
    for index, value in enumerate(args):
        print(f'{index + 1} - {value.upper()}')

def name_consult(name):
    db = Database()
    for info in db.name_consult(name):
        print(f"Cliente: {info[1]}")
        print(f"Documento: {info[2]}")
        print(f"Data de nascimento: {info[3]}")
        print(f"Telefone: {info[4]}")
        print(f"Conta: {info[5]}")
        print(f"Saldo: {info[6]}\n\n")

def add_client(args):
    db = Database()
    db.create_table()
    db.insert_user(args.name, args.document_number, args.date_of_birth, args.phone_number, args.account_number, args.balance)
    db.close()