import json

from static.py.api.database.oracle import database

TABLE_NAME = "Accounts"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"AccountID VARCHAR(12),"
                 f"Username VARCHAR(25),"
                 f"Name VARCHAR(50),"
                 f"Bio VARCHAR(500),"
                 f"Phone VARCHAR(10),"
                 f"Email VARCHAR(50),"
                 f"Password CLOB,"
                 f"Data CLOB CHECK (Data is JSON))")
    if database.execute(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")


def drop_table():
    if database.execute(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select_one__(accountID: str):
    statement = f"SELECT AccountID FROM {TABLE_NAME} WHERE AccountID = {accountID}"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __insert__(account_data):
    statement = (f"INSERT INTO {TABLE_NAME} (AccountID, Username, Name, Bio, Phone, Email, Password, Data) "
                 f"VALUES (:1, :2, :3, :4, :5, :6, :7, :8)")
    result = database.execute(statement, (
        account_data['AccountID'],
        account_data['Username'],
        account_data['Name'],
        account_data['Bio'],
        account_data['Phone'],
        account_data['Email'],
        account_data['Password'],
        account_data['Data']
    ))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def _update(accountID: str, set_query: str):
    statement = f"UPDATE {TABLE_NAME} SET {set_query} WHERE AccountID = {accountID}"
    result = database.execute(statement)
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result


def __update_username__(accountID: str, username: str):
    return _update(accountID, f"Username = '{username}'")


def __update_name__(accountID: str, name: str):
    return _update(accountID, f"Name = '{name}'")


def __update_bio__(accountID: str, bio: str):
    return _update(accountID, f"Bio = '{bio}'")


def __update_phone__(accountID: str, phone: str):
    return _update(accountID, f"Phone = '{phone}'")


def __update_email__(accountID: str, email: str):
    return _update(accountID, f"Email = '{email}'")


def __update_password__(accountID: str, password):
    return _update(accountID, f"Password = '{password}'")


def __update_data__(accountID: str, data: dict):
    return _update(accountID, f"Data = {json.dumps(data)}")


def __delete__(accountID: str):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE AccountID = {accountID}")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result
