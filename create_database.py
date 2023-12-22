from database import Database
import csv


def create_database():
    db = Database('database')
    db.create_client_table()
    db.create_movimentation_table()

    with open('database.csv', 'r+') as archive:
        data = csv.DictReader(archive)
        for _ in data:
            db.insert_user(_['name'],
                           _['document'],
                           _['date_of_birth'],
                           str(_['phone_number']),
                           _['account_number'],
                           int(_['balance']))

    db.close()
