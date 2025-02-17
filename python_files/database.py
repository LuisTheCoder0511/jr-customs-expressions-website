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


def __create_table__(table_name: str, args):
    prefix = f"CREATE TABLE IF NOT EXISTS {table_name}"
    cursor.execute(f"{prefix} {args}")


def __select_all__(table_name: str, limit: int, offset: int, column_name: str = '*'):
    global cursor
    cursor.row_factory = lambda curs, row: row
    cursor.execute(f'SELECT {column_name} FROM {table_name} LIMIT {limit} OFFSET {offset}')
    return cursor.fetchall()


def __select_all_equal__(table_name: str, where_key: str, where_value: str):
    global cursor
    cursor.row_factory = lambda curs, row: row
    cursor.execute(f'SELECT * FROM {table_name} WHERE {where_key} = {where_value}')
    return cursor.fetchall()


def __select_all_like__(table_name: str, where_key: str, where_value: str):
    global cursor
    cursor.row_factory = lambda curs, row: row
    cursor.execute(f"SELECT * FROM {table_name} WHERE {where_key} LIKE '%{where_value}%'")
    return cursor.fetchall()


def __select_one__(table_name: str, key: str, value):
    global cursor
    cursor.execute(f'SELECT * FROM {table_name} WHERE {key} = ?', (value,))
    return cursor.fetchone()


def __insert__(table_name: str, statement, args):
    try:
        prefix = f"INSERT INTO {table_name}"
        __execute__(f"{prefix} {statement}", args)
    except Error as e:
        print(e.args)
        return False
    return True


def __update__(table_name: str, data_key: str, data_value, where_value):
    try:
        statement = f"UPDATE {table_name} SET {data_key} = ? WHERE ID = ?"
        __execute__(statement, (data_value, where_value))
    except Error as _:
        return False
    return True


def __delete__(table_name: str, where_value):
    try:
        __execute__(f"DELETE FROM {table_name} WHERE ID = ?", (where_value,))
    except Error as _:
        return False
    return True


def __execute__(statement: str, parameters: tuple):
    cursor.execute(statement, parameters)

