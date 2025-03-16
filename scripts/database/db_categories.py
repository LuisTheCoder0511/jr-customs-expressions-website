from scripts.database.oracle import database

table_name = "Category"


def __create_table__():
    Name = "Name VARCHAR(50) PRIMARY KEY NOT NULL"
    Data = "Data CLOB CHECK (data is JSON)"

    values = ",\n".join([Name, Data])
    statement = f"CREATE TABLE {table_name} (\n{values}\n)"
    print(statement)
    if not database.__execute__(statement):
        print("Table cannot be created!")


def __drop_table__():
    if not database.__drop_table__(table_name):
        print("Table not found")


def __select__(column_name: str):
    statement = f"SELECT * FROM {table_name} WHERE Name = '{column_name}'"
    database.__execute__(statement)
    return database.__fetch_one__()


def __insert__(name: str, data):
    statement = f"INSERT INTO {table_name} (Name, Data) VALUES (:1, :2)"
    print(statement)
    result = database.__execute__(statement, (name, data))
    if result:
        print("Inserted successfully!")
    return result


def __update__(name: str, data):
    try:
        statement = f"UPDATE {table_name} SET Data = ({data}) WHERE Name = '{name}'"
        database.__execute__(statement)
    except Exception as e:
        print(e.args)
        return False
    return True


def __delete__(name: str):
    statement = f"DELETE FROM {table_name} WHERE Name = '{name}'"
    database.__execute__(statement)
