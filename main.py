from client import Client
from database import Database
import re



if __name__ == '__main__':
    client1 = Client('Maria', '123.456.789-10', '29/08/1990').create_account()
    print(client1.name)
    print(client1.document_number)
    print(client1.date_of_birth)
    print(client1.account_number)
    
    print()    
        
    client2 = Client('Jose', '109.876.543-21', '10/06/1984').create_account()
    print(client2.name)
    print(client2.document_number)
    print(client2.date_of_birth)
    print(client2.account_number)