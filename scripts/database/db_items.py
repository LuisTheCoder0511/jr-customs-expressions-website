from scripts.database.oracle import database

table_name = "Item"


def __create_table__():
    Timestamp = "Timestamp INTEGER PRIMARY KEY"
    Name = "Name VARCHAR(255)"
    Price = "Price VARCHAR(10)"
    Quantity = "Quantity INTEGER"
    Data = "Data CLOB CHECK (data is JSON)"

    values = ",\n".join([Timestamp, Name, Price, Quantity, Data])
    statement = f"CREATE TABLE {table_name} (\n{values}\n)"
    print(statement)
    if not database.__execute__(statement):
        print("Table cannot be created!")


def __drop_table__():
    if not database.__drop_table__(table_name):
        print("Table not found")


def __select_all__(offset: int, row_limit: int):
    database.__row_factory__()
    prefix = f"SELECT * FROM {table_name}\nORDER BY Timestamp DESC\n"
    suffix = f"OFFSET {offset} ROWS FETCH NEXT {row_limit} ROWS ONLY"
    statement = f"{prefix}{suffix}"
    print(f"Statement: {statement}")
    database.__execute__(statement)
    return database.__fetch_all__()


def __select_list__(timestamp_list: tuple[int]):
    database.__row_factory__()
    prefix = f"SELECT * FROM {table_name}\nORDER BY Timestamp\n"
    suffix = f"WHERE Timestamp IN {timestamp_list}"
    database.__execute__(f"{prefix}{suffix}")
    return database.__fetch_all__()


def __select_one__(timestamp: int):
    database.__execute__(f"SELECT * FROM {table_name} WHERE Timestamp = {timestamp}")
    return database.__fetch_one__()


def __insert__(timestamp: int, name: str, price: str, quantity: int, data):
    print("Inserting...")
    statement = f"INSERT INTO {table_name} (Timestamp, Name, Price, Quantity, Data) VALUES (:1, :2, :3, :4, :5)"
    print(statement)
    result = database.__execute__(statement, (timestamp, name, price, quantity, data))
    if result:
        print("Inserted successfully!")
    return result


def __update__(timestamp: int, name: str, price: str, quantity: int, data):
    try:
        statement = (f"UPDATE {table_name} SET (Name, Price, Quantity, Data) = ({name} {price} {quantity} {data}) "
                     f"WHERE Timestamp = {timestamp}")
        database.__execute__(statement)
    except Exception as e:
        print(e.args)
        return False
    return True


def __delete__(timestamp: int):
    try:
        database.__execute__(f"DELETE FROM {table_name} WHERE Timestamp = {timestamp}")
    except Exception as e:
        print(e.args)
        return False
    return True
