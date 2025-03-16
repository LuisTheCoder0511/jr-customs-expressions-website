import concurrent.futures
import json
from time import time

from python_files.test import test_item
from python_files.objects.item import Item
from python_files.database import item_db

pool: concurrent.futures.ThreadPoolExecutor


def execute(get_data):
    data = get_data['data']
    status = get_data['status']
    arg = data['arg']
    if arg == "add":
        status = add(data, status)

    elif arg == "get_all":
        data = get_all(data)

    elif arg == "get":
        data = get(data)
        if not data:
            status = "no item exists"

    elif arg == "update":
        status = update(data, status)

    elif arg == "delete":
        status = delete(data, status)

    get_data['data'] = data
    get_data['status'] = status


def add(data, status):
    status = test_item.add(data, status)

    if not status == "success":
        return status

    name = data['name']
    description = data['description']

    image = data['image']
    categoryIDs = data['categoryIDs']

    price = data['price']
    quantity = data['quantity']
    meta = data['meta']

    timestamp = int(time())

    current_item = Item(timestamp,
                        name,
                        description,
                        image,
                        categoryIDs,
                        price,
                        quantity,
                        meta)
    json_item = json.dumps(current_item.__dict__)
    print(json_item)
    result = item_db.__insert__(timestamp, json_item)
    print(f"Insert... {result}")
    return status


def get(data):
    timestamp = data['timestamp']
    return item_db.__select_one__(timestamp)


def deserialize_clob(select_all, index, get_data):
    current_item = select_all[index][1]
    load_item = json.loads(str(current_item))
    get_data[index] = load_item


def get_all(data):
    limit = data['limit']
    offset = data['offset']
    filter_name = data['filter']
    select_all: list = []
    if not filter_name:
        select_all = item_db.__select_all__(offset, limit)

    print("Items parsing...")
    start = time()
    index = 0
    global pool
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    get_data = []
    while index < len(select_all):
        get_data.append(None)
        pool.submit(deserialize_clob, select_all, index, get_data)
        index += 1

    pool.shutdown(wait=True)
    print(f"{time() - start} ms")

    return get_data


def update(data, status):
    get_data = get(data)
    if not get_data:
        status = "no item exists"
    else:
        item = Item(get_data['timestamp'],
                    get_data['name'],
                    get_data['description'],
                    get_data['image'],
                    get_data['categoryIDs'],
                    get_data['price'],
                    get_data['quantity'],
                    get_data['meta'])
        json_item = json.dumps(item.__dict__)

        item_db.__update__(item.timestamp, json_item)
    return status


def delete(data, status):
    get_data = get(data)
    if not get_data:
        status = "no item exists"
    else:
        item_db.__delete__(get_data["timestamp"])
    return status
