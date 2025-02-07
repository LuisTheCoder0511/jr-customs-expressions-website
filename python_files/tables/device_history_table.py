from sqlite3 import Error

from python_files.objects.device import Device
from python_files import database


table_name = 'device_history'


def __create_table__():
    try:
        database.__create_connection__()
        statement = f"""CREATE TABLE IF NOT EXISTS {table_name} (
        device_id INT PRIMARY KEY NOT NULL,
        name TEXT,
        model TEXT,
        operating_system TEXT,
        ip_address TEXT)"""
        database.cursor.execute(statement)
        database.__close_connection__()
    except Error as _:
        return False
    return True


def __insert__(device: Device):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
            INSERT OR IGNORE INTO {table_name} (
            device_id,
            name, 
            model, 
            operating_system, 
            ip_address) 
            VALUES (?, ?, ?, ?, ?)
            ''', (
                device.device_id,
                device.name,
                device.model,
                device.operating_system,
                device.ip_address
                )
        )
        database.__close_connection__()
    except Error as _:
        return False
    return True


# def __update__(database, device: Device, data_key: str, data_value):
#     try:
#         database.__create_connection__()
#         database.cursor.execute(f'''
#             UPDATE {table_name}
#             SET {data_key} = ?
#             WHERE item_id = ?
#             ''', (data_value, item.item_id))
#         database.__close_connection__()
#     except Error as _:
#         return False
#     return True


def __delete__(device_id):
    try:
        database.__create_connection__()
        database.cursor.execute(f'''
        DELETE FROM {table_name} 
        WHERE device_id = {device_id}
        ''')
        database.__close_connection__()
    except Error as _:
        return False
    return True
