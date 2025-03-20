from api.database.oracle import database

TABLE_NAME = "Item"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"Timestamp INTEGER PRIMARY KEY,"
                 f"Name VARCHAR(255),"
                 f"Price VARCHAR(255),"
                 f"Quantity INTEGER,"
                 f"Data CLOB CHECK (Data is JSON))")
    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select_all__(offset: int, limit: int):
    database.__row_factory__()
    statement = (f"SELECT * FROM {TABLE_NAME} ORDER BY Timestamp DESC\n"
                 f"OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY")
    if database.__execute__(statement):
        print("Selected all rows successfully")
        return database.__fetch_all__()
    print("Failed to select all rows")
    return None


def __select_all_name__(offset: int, limit: int, name: str):
    database.__row_factory__()
    statement = (f"SELECT * FROM {TABLE_NAME} WHERE LOWER(Name) LIKE LOWER('{name}%') ORDER BY Timestamp DESC\n"
                 f"OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY\n")
    if database.__execute__(statement):
        print("Selected all name rows successfully")
        return database.__fetch_all__()
    print("Failed to select all name rows")
    return None


def __select_one__(timestamp: int):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE Timestamp = {timestamp}"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(timestamp: int, name: str, price: str, quantity: int, data):
    statement = f"INSERT INTO {TABLE_NAME} (Timestamp, Name, Price, Quantity, Data) VALUES (:1, :2, :3, :4, :5)"
    result = database.__execute__(statement, (timestamp, name, price, quantity, data))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def _update(timestamp: int, set_query: str):
    statement = f"UPDATE {TABLE_NAME} SET {set_query} WHERE Timestamp = {timestamp}"
    result = database.__execute__(statement)
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result


def __update_name__(timestamp: int, name: str):
    return _update(timestamp, f"NAME = '{name}'")


def __update_price__(timestamp: int, price: str):
    return _update(timestamp, f"PRICE = '{price}'")


def __update_quantity__(timestamp: int, quantity: int):
    return _update(timestamp, f"Quantity = '{quantity}'")


def __update_data__(timestamp: int, data):
    return _update(timestamp, f"Data = '{data}'")


def __delete__(timestamp: int):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE Timestamp = {timestamp}")
    if result:
        print("Item deleted successfully")
    else:
        print("Failed to delete item")
    return result
