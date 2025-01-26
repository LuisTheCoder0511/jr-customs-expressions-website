from sqlite3 import Error

from python_files.objects.item import Item


def __create_table__(database):
    statement = f"""CREATE TABLE IF NOT EXISTS items (
    item_id TEXT PRIMARY KEY NOT NULL,
    name TEXT,
    description TEXT,
    price REAL,
    quantity REAL,
    initial_date DATETIME,
    metadata BLOB)"""
    database.cursor.execute(statement)


def __select_all__(database, column_name: str = '*'):
    database.__create_connection__()
    database.cursor.execute(f'SELECT {column_name} FROM items')
    result = database.cursor.fetchall()
    database.__close_connection__()
    return result


def __select_one__(database, key: str, value):
    database.__create_connection__()
    database.cursor.execute(f'SELECT * FROM items WHERE {key} = ?', (value,))
    result = database.cursor.fetchone()
    database.__close_connection__()
    return result


def __insert__(database, item: Item):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            INSERT OR IGNORE INTO items (
            item_id,
            name, 
            description, 
            price, 
            quantity, 
            initial_date, 
            metadata) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (item.item_id,
                  item.name,
                  item.description,
                  item.price,
                  item.quantity,
                  item.initial_date,
                  item.metadata))
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __update__(database, item: Item, data_key: str, data_value):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            UPDATE items 
            SET {data_key} = ? 
            WHERE item_id = ?
            ''', (data_value, item.item_id))
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __delete__(database, item: Item):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
        DELETE FROM items 
        WHERE item_id = {item.item_id}
        ''')
        database.__close_connection__()
    except Error as _:
        return False
    return True