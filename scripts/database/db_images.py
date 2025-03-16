from scripts.database.oracle import database

table_name = "Item"


def __create_table__():
    ItemID = "ItemID VARCHAR(10) PRIMARY KEY NOT NULL"
    Name = "Name VARCHAR(100) NOT NULL"
    Price = "Price VARCHAR(10) NOT NULL"
    Quantity = "Quantity INTEGER NOT NULL"
    Data = "Data CLOB CHECK (data is JSON)"
    pass


