import sqlite3
from sqlite3 import Error


name = 'database/test'
connection: sqlite3.Connection
cursor: sqlite3.Cursor


def __create_connection__():
    try:
        global connection
        global cursor
        connection = sqlite3.connect(f'{name}.db')
        cursor = connection.cursor()
        print("Connection to database is open!")
    except Error as e:
        print(f"Error connecting to database: {e}")


def __close_connection__():
    try:
        global connection
        global cursor
        connection.commit()
        connection.close()
        print("Connection to database is closed!")
    except Error as e:
        print(f"Error closing connection to database: {e}")


def __select_all__(table_name: str, column_name: str = '*'):
    __create_connection__()
    global cursor
    cursor.row_factory = lambda curs, row: row[0]
    cursor.execute(f'SELECT {column_name} FROM {table_name}')
    result = cursor.fetchall()
    __close_connection__()
    return result


def __select_one__(table_name: str, key: str, value):
    __create_connection__()
    global cursor
    cursor.execute(f'SELECT * FROM {table_name} WHERE {key} = ?', (value,))
    result = cursor.fetchone()
    __close_connection__()
    return result

