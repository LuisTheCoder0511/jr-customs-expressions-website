import sqlite3
from sqlite3 import Error


class Database:

    def __init__(self, name):
        self.name = name

    def __create_connection__(self):
        try:
            self.connection = sqlite3.connect(f'{self.name}.db')
            self.cursor = self.connection.cursor()
            print("Connection to database is open!")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def __close_connection__(self):
        try:
            self.connection.commit()
            self.connection.close()
            print("Connection to database is closed!")
        except Error as e:
            print(f"Error closing connection to database: {e}")

    def __create_table__(self, table_name, arguments):
        self.__create_connection__()
        statement = f"""\
        CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY,\
        {arguments})
        """
        print(statement)
        self.cursor.execute(statement)
        self.__close_connection__()

    def __select_all__(self, table_name: str, column_name: str = '*'):
        self.__create_connection__()
        self.cursor.execute(f'SELECT {column_name} FROM {table_name}')
        result = self.cursor.fetchall()
        self.__close_connection__()
        return result

    def __select_one__(self, table_name: str, key: str, value):
        self.__create_connection__()
        self.cursor.execute(f'SELECT * FROM {table_name} WHERE {key} = ?', (value,))
        result = self.cursor.fetchone()
        self.__close_connection__()
        return result

    def __insert__(self, table_name, keys, values):
        question_arr = ['?'] * len(values)
        questions = ",".join(question_arr)
        try:
            self.__create_connection__()
            self.cursor.execute(f'''
                INSERT INTO {table_name} 
                ({keys}) VALUES ({questions})
                ''', values)
            self.__close_connection__()
        except Error as _:
            return False
        return True

    def __update__(self, table_name, unique_key, unique_value, data_key, data_value):
        self.cursor.execute(f'''
            UPDATE {table_name} 
            SET {data_key} = ? 
            WHERE {unique_key} = ?
            ''', (data_value, unique_value))

    def __delete__(self, table_name, key, value):
        self.cursor.execute(f'''
            DELETE FROM {table_name} 
            WHERE {key} = '{value}'
            ''')
