from sqlite3 import Error

from python_files.objects.cart import Cart


def __create_table__(database):
    statement = f"""CREATE TABLE IF NOT EXISTS carts (
    cart_id TEXT PRIMARY KEY NOT NULL,
    item_ids TEXT,
    price REAL)"""
    database.cursor.execute(statement)


def __select_all__(database, column_name: str = '*'):
    database.__create_connection__()
    database.cursor.execute(f'SELECT {column_name} FROM carts')
    result = database.cursor.fetchall()
    database.__close_connection__()
    return result


def __select_one__(database, key: str, value):
    database.__create_connection__()
    database.cursor.execute(f'SELECT * FROM carts WHERE {key} = ?', (value,))
    result = database.cursor.fetchone()
    database.__close_connection__()
    return result


def __insert__(database, cart: Cart):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            INSERT OR IGNORE INTO carts (
            cart_id,
            item_ids,
            price) 
            VALUES (?, ?, ?)
            ''', (cart.cart_id,
                  cart.item_ids,
                  cart.price))
        database.__close_connection__()
    except Error as e:
        print(e)
        return False
    return True


def __update__(database, item: Cart, data_key: str, data_value):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            UPDATE carts 
            SET {data_key} = ? 
            WHERE cart_id = ?
            ''', (data_value, item.cart_id))
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __delete__(database, item: Cart):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
        DELETE FROM carts 
        WHERE cart_id = {item.cart_id}
        ''')
        database.__close_connection__()
    except Error as _:
        return False
    return True