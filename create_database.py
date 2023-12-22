from database import Database
import csv

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
                       ['account_number'],
                       int(_['balance']))
