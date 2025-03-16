from scripts.database.oracle import database

table_name = "Account"


def __create_table__():
    AccountID = "AccountID VARCHAR(6) PRIMARY KEY NOT NULL"
    Username = "Username VARCHAR(24) NOT NULL UNIQUE"
    Name = "Name VARCHAR(100) NOT NULL"
    Data = "Data CLOB CHECK (data is JSON)"

    values = ",\n".join([AccountID, Username, Name, Data])
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


def __select_username__(username: str):
    database.__execute__(f"SELECT * FROM {table_name} WHERE Username = '{username}'")
    return database.__fetch_one__()


def __insert__(accountID: str, username: str, name: str, arg):
    print("Inserting...")
    statement = f"INSERT INTO {table_name} (AccountID, Username, Name, Data) VALUES (:1, :2, :3, :4)"
    print(statement)
    result = database.__execute__(statement, (accountID, username, name, arg))
    if result:
        print("Inserted successfully!")
    return result


def __update__(timestamp: int, name: str, data):
    try:
        statement = f"UPDATE {table_name} SET (Name, Data) = ({name} {data}) WHERE Timestamp = {timestamp}"
        database.__execute__(statement)
    except Exception as e:
        print(e.args)
        return False
    return True


