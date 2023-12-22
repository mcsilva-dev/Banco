from database import Database
import re


def menu(*args):
    print('MENU PRINCIPAL'.center(50, '-'))
    print("\nESCOLHA UMA OPÇÃO:\n")
    for index, value in enumerate(args):
        print(f'{index + 1} - {value.upper()}')


def show_results(data):
    print()
    print('RESULTADO DA BUSCA'.center(50, '-'))
    print(f"\nid: {data['id']}")
    print(f"Cliente: {data['name']}")
    print(f"Documento: {data['document']}")
    print(f"Data de nascimento: {data['date_of_birth']}")
    print(f"Telefone: {data['phone_number']}\n")


def name_consult(name, database):
    db = Database(database)
    results = db.name_consult(name)
    db.close()
    return results


def document_consult(document, database):
    db = Database(database)
    results = db.document_consult(document)
    db.close()
    return results if len(results) > 0 else None


def add_client(args, database):
    db = Database(database)
    db.create_client_table()
    db.insert_user(args.name, args.document_number, args.date_of_birth, args.phone_number, args.account_number,
                   args.balance)
    db.close()


def transactions(name, database, value, transaction_type):
    from datetime import datetime
    client = name_consult(name, database)
    if len(client):
        db = Database(database)
        db.insert_transaction(name=client[0]['name'],
                                value=value,
                                transaction_type=transaction_type,
                                id_client=client[0]['id'],
                                date=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


def history_transactions(document, account_number, database):
    try:
        assert re.compile(r'(\d{3}).(\d{3}).(\d{3})-(\d{2})').fullmatch(document)
    except AssertionError:
        return 1
    try:
        results = document_consult(document, database)
        assert results
        assert results[0]['account_number'] == account_number
        db = Database(database)
        results = db.consult_transactions(results[0]['id'])
        return [_ for _ in results]
    except AssertionError:
        return None
