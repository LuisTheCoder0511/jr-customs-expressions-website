import json
import os

from scripts.backend import accounts, password


app_name = "JRCustomsExpressions"
appdata_path = os.path.join(os.getenv('APPDATA'), app_name)
json_data = {
    "account": {
        "username": None,
        "timestamp": None,
        "remember": None
    }
}


def write_file(data, file_name):
    global app_name
    global appdata_path
    os.makedirs(appdata_path, exist_ok=True)
    file_path = os.path.join(appdata_path, file_name)
    with open(file_path, 'w') as file:
        file.write(json.dumps(data, indent=4))


def check_user_file():
    global app_name
    global appdata_path
    file_path = os.path.join(appdata_path, "user.json")
    if not os.path.exists(appdata_path) or not os.path.exists(file_path):
        write_user()
        return False
    return True


def write_user(data=None):
    if not data:
        data = json_data
    write_file(data, "user.json")


def read_user():
    data = {}
    if not check_user_file():
        return data

    global app_name
    global appdata_path
    file_path = os.path.join(appdata_path, "user.json")
    with open(file_path, "r") as file:
        data = json.load(file)

    if data == json_data:
        return data

    if not accounts.timestamp_valid(data):
        write_user()
        data = json_data

    return data



def api(data, password_required=True):
    accounts.api(data)
    if password_required:
        password.api(data)

    del data['arg']
