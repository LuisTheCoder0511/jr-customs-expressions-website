from sqlite3 import Error

from python_files.objects.profile import Profile


def __create_table__(database):
    statement = f"""CREATE TABLE IF NOT EXISTS profiles (
    code TEXT PRIMARY KEY NOT NULL,
    name TEXT,
    bio TEXT,
    email TEXT,
    phone TEXT,
    img BLOB,
    cart_id TEXT NOT NULL)"""
    database.cursor.execute(statement)


def __select_all__(database, column_name: str = '*'):
    database.__create_connection__()
    database.cursor.execute(f'SELECT {column_name} FROM profiles')
    result = database.cursor.fetchall()
    database.__close_connection__()
    return result


def __select_one__(database, key: str, value):
    database.__create_connection__()
    database.cursor.execute(f'SELECT * FROM profiles WHERE {key} = ?', (value,))
    result = database.cursor.fetchone()
    database.__close_connection__()
    return result


def __insert__(database, profile: Profile):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            INSERT OR IGNORE INTO profiles (
            code,
            name, 
            bio, 
            email, 
            phone, 
            img,
            cart_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (profile.code,
                  profile.name,
                  profile.bio,
                  profile.email,
                  profile.phone,
                  profile.img,
                  profile.cart_id))
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __update__(database, profile: Profile, data_key: str, data_value):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            UPDATE profiles 
            SET {data_key} = ? 
            WHERE code = ?
            ''', (data_value, profile.code))
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __delete__(database, profile: Profile):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
        DELETE FROM profiles 
        WHERE code = {profile.code}
        ''')
        database.__close_connection__()
    except Error as _:
        return False
    return True