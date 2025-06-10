from static.py.api.database.oracle import database

TABLE_NAME = "Accounts"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"AccountID VARCHAR(12),"
                 f"Username VARCHAR(25),"
                 
                 f"AccountData CLOB CHECK (AccountData is JSON))")
    if database.execute(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def drop_table():
    if database.execute(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select__(accountID: str):
    statement = f"SELECT AccountID FROM {TABLE_NAME} WHERE AccountID = '{accountID}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(account_id: str, username: str, account_data: str):
    statement = (f"INSERT INTO {TABLE_NAME} (AccountID, Username, AccountData) "
                 f"VALUES (:1, :2, :3)")
    result = database.execute(statement, (account_id, username, account_data))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def _update(account_id: str, set_query: str):
    statement = f"UPDATE {TABLE_NAME} SET {set_query} WHERE AccountID = {account_id}"
    result = database.execute(statement)
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result


def __update_username__(account_id: str, username: str):
    return _update(account_id, f"Username = '{username}'")


def __update_data__(account_id: str, account_data: str):
    return _update(account_id, f"AccountData = '{account_data}'")


def __delete__(account_id: str):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE AccountID = {account_id}")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result
