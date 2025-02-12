from sqlite3 import Error

from python_files.objects.account import Account
from python_files import database


table_name = 'Account'


def __create_table__():
    prefix = f"CREATE TABLE IF NOT EXISTS {table_name}"
    arg1 = "ID INT PRIMARY KEY AUTO_INCREMENT"
    arg2 = "username TEXT NOT NULL"
    arg3 = "bio TEXT"
    arg4 = "email TEXT"
    arg5 = "phone TEXT"
    database.cursor.execute(f"{prefix} ({arg1}, {arg2}, {arg3}, {arg4}, {arg5})")


def __insert__(account: Account):
    try:
        prefix = f"INSERT INTO {table_name}"
        statement = "(ID, username, bio, email, phone)"
        args = (account.ID, account.username, account.bio, account.email, account.phone)
        database.__execute__(f"{prefix} {statement}", args)
    except Error as _:
        return False
    return True


def __update__(account: Account, data_key: str, data_value):
    try:
        statement = f"UPDATE {table_name} SET {data_key} = ? WHERE ID = ?"
        database.__execute__(statement, (data_value, account.ID))
    except Error as _:
        return False
    return True


def __delete__(account: Account):
    try:
        database.__execute__(f"DELETE FROM {table_name} WHERE ID = ?", (account.ID,))
    except Error as _:
        return False
    return True
