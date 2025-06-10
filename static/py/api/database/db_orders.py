from static.py.api.database.oracle import database

TABLE_NAME = "Orders"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"OrderID INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                 f"AccountID VARCHAR(12)"
                 f"Timestamp INTEGER,"
                 f"OrderData CLOB CHECK (OrderData is JSON))")

    if database.execute(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")

def drop_table():
    if database.execute(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")