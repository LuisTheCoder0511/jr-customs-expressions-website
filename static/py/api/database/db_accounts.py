from static.py.api.database.oracle import database

TABLE_NAME = "Accounts"

def __create_table__():
    statement = (f"CREATE TABLE {TABLE_NAME} ("
                 f"AccountID VARCHAR(12),"
                 f"PasswordID VARCHAR(24),"
                 f"CartID VARCHAR(12),"
                 f"Username VARCHAR(25),"
                 f"OrderIDs CLOB CHECK (OrderIDs IS JSON),"
                 f"AccountData CLOB CHECK (AccountData is JSON))")
    if database.__execute__(statement):
        print("Table created successfully")
    else:
        print("Failed to create table")

def __drop_table__():
    if database.__execute__(f"DROP TABLE {TABLE_NAME}"):
        print("Table dropped successfully")
    else:
        print("Failed to drop table")


def __select_id__(accountID: str):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE AccountID = '{accountID}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None


def __select_username__(username: str):
    statement = f"SELECT * FROM {TABLE_NAME} WHERE Username = '{username}'"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None

def __select_all__():
    statement = f"SELECT * FROM {TABLE_NAME} ORDER BY AccountID DESC"
    if database.__execute__(statement):
        print("Selected row successfully")
        return database.__fetch_one__()
    print("Failed to select row")
    return None

def __insert__(account_id: str, password_id: str, cart_id: str, username: str):
    statement = (f"INSERT INTO {TABLE_NAME} (AccountID, PasswordID, CartID, Username, OrderIDs, AccountData) "
                 f"VALUES (:1, :2, :3, :4, :5, :6)")
    result = database.__execute__(statement, (account_id, password_id, cart_id, username, "{}", "{}"))
    if result:
        print("Inserted row successfully")
    else:
        print("Failed to insert row")
    return result


def _update(account_id: str, set_query: str):
    statement = f"UPDATE {TABLE_NAME} SET {set_query} WHERE AccountID = {account_id}"
    result = database.__execute__(statement)
    if result:
        print("Updated row successfully")
    else:
        print("Failed to update row")
    return result


def __update_username__(account_id: str, username: str):
    return _update(account_id, f"Username = '{username}'")


def __update_order_ids__(account_id: str, order_ids: str):
    return _update(account_id, f"OrderIDs = '{order_ids}'")


def __update_data__(account_id: str, account_data: str):
    return _update(account_id, f"AccountData = '{account_data}'")


def __delete__(account_id: str):
    result = database.__execute__(f"DELETE FROM {TABLE_NAME} WHERE AccountID = {account_id}")
    if result:
        print("Deleted row successfully")
    else:
        print("Failed to delete row")
    return result
