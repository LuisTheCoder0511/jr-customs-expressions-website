import oracledb

from python_files.oracle.oracle import database

table_name = "Item"


def __create_table__():
    try:
        value = "ID_TIMESTAMP INTEGER PRIMARY KEY,\nData CLOB CHECK (data is JSON)"
        statement = f"CREATE TABLE {table_name} (\n{value}\n)"
        print(statement)
        database.__execute__(statement)
    except oracledb.Error as e:
        print(e)
        return False
    return True


def __drop_table__():
    try:
        database.__drop_table__(table_name)
    except oracledb.Error as _:
        print("Table does not exist!")


def __select_all__(offset: int, row_limit: int):
    database.__row_factory__()
    prefix = f"SELECT * FROM {table_name}\nORDER BY ID_TIMESTAMP DESC\n"
    suffix = f"OFFSET {offset} ROWS FETCH NEXT {row_limit} ROWS ONLY"
    statement = f"{prefix}{suffix}"
    database.__execute__(statement)
    return database.__fetch_all__()


def __select_list__(timestamp_list: tuple[int]):
    database.__row_factory__()
    prefix = f"SELECT * FROM {table_name}\nORDER BY ID_TIMESTAMP\n"
    suffix = f"WHERE ID_TIMESTAMP IN {timestamp_list}"
    database.__execute__(f"{prefix}{suffix}")
    return database.__fetch_all__()


def __select_one__(timestamp: int):
    database.__execute__(f"SELECT * FROM {table_name} WHERE ID_TIMESTAMP = {timestamp}")
    return database.__fetch_one__()


def __insert__(timestamp, arg):
    print("Inserting...")
    statement = f"INSERT INTO {table_name} (ID_TIMESTAMP, Data) VALUES (:1, :2)"
    print(statement)
    result = database.__execute__(statement, (timestamp, arg))
    if result:
        print("Inserted successfully!")
    return result


def __update__(timestamp: int, data):
    try:
        statement = f"UPDATE {table_name} SET Data = {data} WHERE ID_TIMESTAMP = {timestamp}"
        database.__execute__(statement)
    except Exception as e:
        print(e.args)
        return False
    return True


def __delete__(timestamp: int):
    try:
        database.__execute__(f"DELETE FROM {table_name} WHERE ID_TIMESTAMP = {timestamp}")
    except Exception as e:
        print(e.args)
        return False
    return True
