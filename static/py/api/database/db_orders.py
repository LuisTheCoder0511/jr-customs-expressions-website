from static.py.api.database.oracle import database

TABLE_NAME = "Orders"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"OrderID INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                 f"AccountID VARCHAR(12),"
                 f"OrderTimestamp INTEGER,"
                 f"OrderData CLOB CHECK (OrderData is JSON))")

    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")

def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")

def __select_all_limit__(offset: int, limit: int):
    database.__row_factory__()
    statement = (f"SELECT * FROM {TABLE_NAME} ORDER BY OrderID DESC\n"
                 f"OFFSET {offset} ROWS FETCH NEXT {limit} ROWS ONLY")
    if database.__execute__(statement):
        print("Selected all rows successfully")
        return database.__fetch_all__()
    print("Failed to select all rows")
    return None

def __select_all__():
    database.__row_factory__()
    statement = f"SELECT * FROM {TABLE_NAME} ORDER BY OrderID DESC"
    if database.__execute__(statement):
        print("Selected all rows successfully")
        return database.__fetch_all__()
    print("Failed to select all rows")
    return None

def __select_one__(order_id: int):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE OrderID = {order_id}"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None

def __insert__(account_id: str, order_timestamp: int, order_data: str):
    statement = (f"INSERT INTO {TABLE_NAME} (AccountID, OrderTimestamp, OrderData) "
                 f"VALUES (:1, :2, :3)")
    result = database.__execute__(statement, account_id, order_timestamp, order_data)
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result

def __delete__(order_id: int):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE OrderID = {order_id}")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result