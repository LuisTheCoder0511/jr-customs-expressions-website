from static.py.api.database.oracle import database

TABLE_NAME = "Webpage"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"ID INTEGER PRIMARY KEY,"
                 f"Data CLOB CHECK (Data is JSON))")
    if database.__execute__(statement):
        print("Table created successfully")
        return True
    else:
        print("Failed to create table")
        return False


def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select__():
    database.__row_factory__()
    statement = f"SELECT * FROM {TABLE_NAME} WHERE ID = 1"
    if database.__execute__(statement):
        print("Table selected successfully")
        return database.__fetch_one__()
    else:
        print("Failed to select table")

def __select_all__():
    statement = f"SELECT * FROM {TABLE_NAME} ORDER BY ID DESC"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(data: str):
    statement = f"INSERT INTO {TABLE_NAME} (ID, Data) VALUES (:1, :2)"
    result = database.__execute__(statement, (1, data))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def __update__(data: str):
    statement = f"UPDATE {TABLE_NAME} SET Data = (Data) WHERE ID = (ID)"
    result = database.__execute__(statement, (1, data))
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result
