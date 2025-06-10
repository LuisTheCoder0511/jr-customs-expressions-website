import bcrypt, json, time

from static.py.api.database import db_passwords
from static.py.api.others import id_gens

def hash_password(plain_password: str) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(plain_password.encode(), salt)
    return hashed

def verify_password(plain_password: str, hashed_password: bytes):
    return bcrypt.checkpw(plain_password.encode(), hashed_password)

def __authenticate__(password_id: str, raw_password: str):
    data = db_passwords.__select__(password_id)
    hashed_password = data["password_hash"]
    verify_password(raw_password, hashed_password)

def __new_password__(raw_passwords):
    password_hash: bytes
    if raw_passwords[0] == raw_passwords[1]:
        password_hash = hash_password(raw_passwords[0])
    else:
        print("Passwords don't match")
        return {}

    timestamp = int(time.time())
    return {"password_hash": password_hash, "timestamp": timestamp}

def api(request_form):
    db_passwords.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    sql_method = json_data["sql_method"]
    data_password = json_data["data"]

    if sql_method == "select":
        __authenticate__(data_password["password_id"], data_password["raw_password"][0])

    elif sql_method == "insert":
        password_data = __new_password__(data_password["raw_passwords"])
        if not password_data:
            return False

        password_id = id_gens.generator(db_passwords.__select__, 32)

        if db_passwords.__insert__(password_id,
                                   password_data["password_hash"],
                                   password_data["timestamp"]):
            return True
        print("Something went wrong while creating password")
        return False

    elif sql_method == "update":
        password_data = __new_password__(data_password["raw_passwords"])
        if not password_data:
            return False

        if db_passwords.__update__(data_password["password_id"],
                                       password_data["password_hash"],
                                       password_data["timestamp"]):
            return True
        print("Something went wrong while updating password")
        return False
