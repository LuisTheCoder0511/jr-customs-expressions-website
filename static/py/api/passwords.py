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
    hashed_password = __read_lob_password__(data[1])
    return verify_password(raw_password, hashed_password)

def __new_password__(raw_password):
    password_hash = hash_password(raw_password)
    timestamp = int(time.time())
    return {"password_hash": password_hash, "timestamp": timestamp}

def __read_lob_password__(lob_password):
    load_password = lob_password.read()
    return load_password

def api(request_form, method):
    db_passwords.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    data_password = json_data["data"]

    if method == "authenticate":
        return __authenticate__(data_password["password_id"], data_password["raw_password"])

    elif method == "insert":
        password_data = __new_password__(data_password["raw_password"])
        password_id = id_gens.generator(db_passwords.__select__, 24)

        if db_passwords.__insert__(password_id,
                                   password_data["password_hash"],
                                   password_data["timestamp"]):
            return {"status": True, "password_id": password_id}
        print("Something went wrong while creating password")
        return False

    elif method == "update":
        password_data = __new_password__(data_password["raw_password"])

        if db_passwords.__update__(data_password["password_id"],
                                       password_data["password_hash"],
                                       password_data["timestamp"]):
            return True
        print("Something went wrong while updating password")
        return False

    elif method == "delete":
        return db_passwords.__delete__(data_password["password_id"])