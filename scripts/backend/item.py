import concurrent.futures
import json
from time import time

from scripts.database import db_items


pool: concurrent.futures.ThreadPoolExecutor


def deserialize_item(get_all, index, get_data):
    current_item = get_all[index][4]
    load_item = json.loads(str(current_item))
    get_data[index]["Data"] = load_item


def insert(data):
    print(data)
    pass


def select(data):
    timestamp = data['timestamp']
    return db_items.__select_one__(timestamp)


def select_all(data):
    limit = data['limit']
    offset = data['offset']
    get_all: list = []
    if data['filter'] == "None":
        get_all = db_items.__select_all__(offset, limit)

    print(get_all)
    print("Items parsing...")
    start = time()
    index = 0
    global pool
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    get_data = []
    while index < len(get_all):
        current_item = get_all[index]
        current_data = {
            "Timestamp": current_item[0],
            "Name": current_item[1],
            "Price": current_item[2],
            "Quantity": current_item[3],
        }

        get_data.append(current_data)
        pool.submit(deserialize_item, get_all, index, get_data)
        index += 1

    print(f"Total pools: {index}")
    pool.shutdown(wait=True)
    print(f"{time() - start} ms")

    return get_data


def update():
    pass


def delete():
    pass


def api(data):
    if data["arg"] == 'select':
        select(data)
    elif data["arg"] == 'select_all':
        get_data = select_all(data)
        print(get_data)
        data["get_data"] = get_data

    del data['arg']
    return data
