from database import Database


def menu(*args):
    """
    Prints a menu with options.

    Parameters:
    args -- a list of options to be displayed in the menu.
    """
    print('MENU PRINCIPAL'.center(50, '-'))
    print("\nESCOLHA UMA OPÇÃO:\n")
    for index, value in enumerate(args):
        print(f'{index + 1} - {value.upper()}')


def name_consult(name, database):
    """
    Searches the database for clients with a given name.

    Parameters:
    name -- the name of the client to search for.

    Returns:
    A list of tuples, where each tuple represents a client record, containing the client's
    name, document number, date of birth, phone number, account number, and balance.
    """
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
    """
    Adds a new client to the database.

    Parameters:
    args -- a namedtuple containing the client's information: name, document number, 
    date of birth, phone number, account number, and balance.
    """
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