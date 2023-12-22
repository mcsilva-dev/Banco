from database import Database


def menu(*args):
    print('MENU PRINCIPAL'.center(50, '-'))
    print("\nESCOLHA UMA OPÇÃO:\n")
    for index, value in enumerate(args):
        print(f'{index + 1} - {value.upper()}')


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


def movimentation(name, database, value, movimentation_type):
    from datetime import datetime
    client = name_consult(name, database)
    if len(client):
        db = Database(database)
        db.insert_movimentation(name=client[0]['name'],
                                value=value,
                                movimentation_type=movimentation_type,
                                id_client=client[0]['id'],
                                date=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


def history_movimentation(document, account_number, database):
    try:
        results = document_consult(document, database)
        assert len(results)
        assert results[0]['account_number'] == account_number
        db = Database(database)
        results = db.consult_movimentation(results[0]['id'])
        return [_ for _ in results]
    except AssertionError:
        return None
