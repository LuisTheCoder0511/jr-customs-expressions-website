from api.database.oracle import database

TABLE_NAME = "Image"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"Timestamp INTEGER PRIMARY KEY,"
                 f"URL VARCHAR(255)")
    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select_count__(url: str):
    statement = f"SELECT COUNT(*) FROM {TABLE_NAME} WHERE URL = '{url}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __select_one__(timestamp: int):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE Timestamp = {timestamp}"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(timestamp: int, url: str):
    statement = f"INSERT INTO {TABLE_NAME} (Timestamp, URL) VALUES (:1, :2)"
    result = database.__execute__(statement, (timestamp, url))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def __delete__(timestamp: int):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE Timestamp = {timestamp}")
    if result:
        print("image deleted successfully")
    else:
        print("Failed to delete image")
    return result