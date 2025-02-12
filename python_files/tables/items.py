from python_files.objects.item import Item
from python_files import database


table_name = "Item"


def __create_table__():
    args = f"""(ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            categoryID INTEGER,
            price REAL,
            quantity INTEGER,
            meta TEXT)
            """
    database.__create_table__(table_name, args)


def __retrieve_id__(item: Item):
    data = database.__select_one__(table_name, "name", item.name)
    if not data:
        return False
    item.__set_id__(data[0])
    return True


def __get_item__(name: str):
    data = database.__select_one__(table_name, "name", name)
    if not data:
        return None

    item = Item(data[1], data[2], data[3], data[4], data[5], data[6])
    item.__set_id__(data[0])
    return item


def __select_all__(filter: str = '*'):
    data = database.__select_all__(table_name, filter)
    print(data)


def __select_list__(where_key: str, where_value):
    data = database.__select_list__(table_name, where_key, where_value)
    print(data)


def __insert__(item: Item):
    statement = "(name, description, categoryID, price, quantity, meta) VALUES (?, ?, ?, ?, ?, ?)"
    args = (item.name, item.description, item.categoryID, item.price, item.quantity, item.meta)
    return database.__insert__(table_name, statement, args)


def __update__(item: Item, data_key: str, data_value):
    database.__update__(table_name, data_key, data_value, item.ID)


def __delete__(item: Item):
    database.__delete__(table_name, item.ID)


database.__create_connection__()
__create_table__()
current_item = Item("blip", "", 0, 9.99, 1, "")
if not __retrieve_id__(current_item):
    result = __insert__(current_item)
    print(f"Insert... {result}")
    __retrieve_id__(current_item)

print(current_item.__dict__)
current_item = __get_item__("name")
__select_all__()
__select_list__("categoryID", 0)
database.__close_connection__()
