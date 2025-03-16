from scripts.database.oracle import database

table_name = "Password"


def __create_table__():
    AccountID = "AccountID VARCHAR(6) PRIMARY KEY NOT NULL"
    Data = "Password BLOB"

    values = ",\n".join([AccountID, Data])
    statement = f"CREATE TABLE {table_name} (\n{values}\n)"
    print(statement)
    if not database.__execute__(statement):
        print("Table cannot be created!")


def __drop_table__():
    if not database.__drop_table__(table_name):
        print("Table not found")


def __select_id__(AccountID: str):
    database.__execute__(f"SELECT * FROM {table_name} WHERE AccountID = '{AccountID}'")
    return database.__fetch_one__()


def __insert__(accountID: str, password: bytes):
    print("Inserting...")
    statement = f"INSERT INTO {table_name} (AccountID, Password) VALUES (:1, :2)"
    print(statement)
    result = database.__execute__(statement, (accountID, password))
    if result:
        print("Inserted successfully!")
    return result


def __update__(accountID: str, password: bytes):
    try:
        statement = f"UPDATE {table_name} SET (Password) = ({password}) WHERE AccountID = {accountID}"
        database.__execute__(statement)
    except Exception as e:
        print(e.args)
        return False
    return True
