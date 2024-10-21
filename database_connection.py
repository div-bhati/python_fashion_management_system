import mysql.connector

def create_connection(host='localhost', user='root', password='12345678', database='fashion_management_system'):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection
