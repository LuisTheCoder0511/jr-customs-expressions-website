from scripts.database import db_accounts
from scripts.generator import string_ids
import time


def insert(data):
    if select_username(data):
        data['exists'] = True
        return False
    data['exists'] = False
    while True:
        AccountID = string_ids.generate(6)
        if not db_accounts.__select_id__(AccountID):
            data['AccountID'] = AccountID
            break

    return db_accounts.__insert__(data['AccountID'], data['username'], data['name'], "{}")


def select_username(data):
    username = data['username']
    query = db_accounts.__select_username__(username)
    if query:
        data['AccountID'] = query[0]
        data['name'] = query[2]
        data['userArgs'] = query[3]
    return query


def select_id(data):
    AccountID = data['AccountID']
    return db_accounts.__select_id__(AccountID)


def update():
    pass


def delete():
    pass


def timestamp_valid(data):
    account = data["account"]
    account_timestamp = account["timestamp"]
    account_remember = account["remember"]

    timestamp_value = 3_600
    if account_remember:
        timestamp_value *= 336
    else:
        timestamp_value *= 8

    timestamp_value /= 60

    current_timestamp = int(time.time() - account_timestamp)
    print(f"Current: {current_timestamp}")
    print(f"Timestamp: {timestamp_value}")
    return current_timestamp < timestamp_value


def api(data):
    if data["arg"] == 'insert':
        insert(data)
    elif data["arg"] == 'select':
        if not select_username(data):
            data['exists'] = False
        else:
            data['exists'] = True

    elif data["arg"] == 'select_id':
        select_id(data)

    return data
