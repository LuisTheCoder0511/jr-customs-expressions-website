from static.py.api.database.oracle import database

TABLE_NAME = "Carts"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"CartID VARCHAR(12) PRIMARY KEY,"
                 f"CartData CLOB CHECK (CartData is JSON))")
    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")

def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")

def __select__(cart_id: str):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE CartID = '{cart_id}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None

def __select_all__():
    statement = f"SELECT * FROM {TABLE_NAME} ORDER BY CartID DESC"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None

def __insert__(cart_id: str):
    statement = (f"INSERT INTO {TABLE_NAME} (CartID, CartData) "
                 f"VALUES (:1, :2)")
    result = database.__execute__(statement, (cart_id, "{}"))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result

def __update__(cart_id: str, cart_data):
    statement = (f"UPDATE {TABLE_NAME} "
                 f"SET CartData = (:1) "
                 f"WHERE CartID = '{cart_id}'")
    result = database.__execute__(statement, cart_data)
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result

def __delete__(cart_id: str):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE CartID = '{cart_id}'")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result