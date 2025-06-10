from static.py.api.database.oracle import database

TABLE_NAME = "Passwords"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"PasswordID VARCHAR(12) PRIMARY KEY,"
                 f"PasswordHash BLOB,"
                 f"Timestamp INTEGER)")
    if database.execute(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def drop_table():
    if database.execute(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select__(password_id: str):
    statement = f"SELECT PasswordID FROM {TABLE_NAME} WHERE PasswordID = '{password_id}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(password_id: str, hashed_password: bytes, timestamp: int):
    statement = (f"INSERT INTO {TABLE_NAME} (PasswordID, PasswordHash, Timestamp) "
                 f"VALUES (:1, :2, :3)")
    result = database.execute(statement, (password_id, hashed_password, timestamp))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def __update__(password_id: str, hashed_password: bytes, timestamp: int):
    statement = (f"UPDATE {TABLE_NAME}"
                 f"SET PasswordHash = (:1),"
                 f"Timestamp = (:2) "
                 f"WHERE PasswordID = '{password_id}'")
    result = database.execute(statement, (hashed_password, timestamp))
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
