from sqlite3 import Error

from python_files.objects.cart import Cart
from python_files import database


table_name = 'CARTS'


def __create_table__():
    prefix = f"CREATE TABLE IF NOT EXISTS {table_name}"
    arg1 = "ID INT FOREIGN KEY REFERENCES ACCOUNT(ID) ON DELETE CASCADE"
    arg2 = "ItemIDs BLOB NOT NULL"
    database.cursor.execute(f"{prefix} ({arg1}, {arg2})")


def __insert__(cart: Cart):
    try:
        statement = "INSERT OR IGNORE INTO {table_name} (ID, ItemIDs) VALUES (?, ?)"
        database.__execute__(statement, (cart.ID, cart.ItemIDs))
    except Error as e:
        print(e)
        return False
    return True


def __update__(cart: Cart, data_key: str, data_value):
    try:
        statement = f"UPDATE {table_name} SET {data_key} = ? WHERE ID = ?"
        database.__execute__(statement, (data_value, cart.ID))
    except Error as _:
        return False
    return True


def __delete__(cart: Cart):
    try:
        statement = f"DELETE FROM {table_name} WHERE ID = ?"
        database.__execute__(statement, (cart.ID,))
    except Error as _:
        return False
    return True
