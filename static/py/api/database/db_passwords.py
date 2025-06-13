from static.py.api.database.oracle import database

TABLE_NAME = "Passwords"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"PasswordID VARCHAR(24) PRIMARY KEY,"
                 f"PasswordHash BLOB,"
                 f"PasswordTimestamp INTEGER)")
    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select__(password_id: str):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE PasswordID = '{password_id}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __select_all__():
    database.__row_factory__()
    statement = f"SELECT * FROM {TABLE_NAME} ORDER BY PasswordID DESC"
    if database.__execute__(statement):
        print("Selected all rows successfully")
        return database.__fetch_all__()
    print("Failed to select all rows")
    return None


def __insert__(password_id: str, hashed_password: bytes, timestamp: int):
    statement = (f"INSERT INTO {TABLE_NAME} (PasswordID, PasswordHash, PasswordTimestamp) "
                 f"VALUES (:1, :2, :3)")
    result = database.__execute__(statement, (password_id, hashed_password, timestamp))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def __update__(password_id: str, hashed_password: bytes, timestamp: int):
    statement = (f"UPDATE {TABLE_NAME} "
                 f"SET PasswordHash = (:1), "
                 f"PasswordTimestamp = (:2) "
                 f"WHERE PasswordID = '{password_id}'")
    result = database.__execute__(statement, (hashed_password, timestamp))
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result

def __delete__(password_id: str):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE PasswordID = '{password_id}'")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result
