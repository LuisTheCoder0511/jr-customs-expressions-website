import bcrypt

from scripts.database import db_passwords


def encrypt_password(password):
    salt = bcrypt.gensalt()
    return hash_password(password, salt)


def hash_password(password, salt):
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def verify_password(password, targetHash):
    current_hash = password.encode('utf-8')
    return bcrypt.checkpw(current_hash, targetHash)


def insert(data):
    hashed_password = data['hashed_password']
    return db_passwords.__insert__(data['AccountID'], hashed_password)


def select_id(data):
    AccountID = data['AccountID']
    return db_passwords.__select_id__(AccountID)


def update():
    pass


def delete():
    pass


def api(data):
    if not data['exists'] and data['arg'] == "insert":
        insert(data)
    if data['exists'] and data['arg'] == "select":
        hashed_password = select_id(data)[1].read()
        data["invalid"] = not verify_password(data["password"], hashed_password)
