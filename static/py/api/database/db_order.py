from static.py.api.database.oracle import database

TABLE_NAME = "Orders"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"OrderID INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,"
                 f"AccountID INTEGER NOT NULL,"
                 f"OrderData CLOB CHECK (OrderData is JSON))")

