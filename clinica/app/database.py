import pymysql

def connect_to_database():
    connection = pymysql.connect(
        host='localhost',
        user='admin',
        password='RoyML',
        database='clinica',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection