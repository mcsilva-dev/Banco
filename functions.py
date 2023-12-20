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


def name_consult(name):
    """
    Searches the database for clients with a given name.

    Parameters:
    name -- the name of the client to search for.

    Returns:
    A list of tuples, where each tuple represents a client record, containing the client's
    name, document number, date of birth, phone number, account number, and balance.
    """
    db = Database()
    results = db.name_consult(name)
    db.close()
    return results


def document_consult(document):
    db = Database()
    results = db.document_consult(document)
    db.close()
    return results if len(results) > 0 else None


def add_client(args):
    """
    Adds a new client to the database.

    Parameters:
    args -- a namedtuple containing the client's information: name, document number, 
    date of birth, phone number, account number, and balance.
    """
    db = Database()
    db.create_client_table()
    db.insert_user(args.name, args.document_number, args.date_of_birth, args.phone_number, args.account_number,
                   args.balance)
    db.close()


def update_balance(new_balance, name):
    db = Database()
    db.update_balance(new_balance, name)
    db.close()