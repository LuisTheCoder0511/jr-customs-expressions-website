from static.py.api.database.oracle import database

TABLE_NAME = "Carts"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"CartID VARCHAR(12) PRIMARY KEY,"
                 f"CartData CLOB CHECK (CartData is JSON))")
    if database.execute(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")

def drop_table():
    if database.execute(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")

