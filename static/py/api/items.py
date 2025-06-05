import time
import json

from static.py.api.bucket.backblaze import backblaze
from static.py.api.database import db_items
from static.py.api.format import format


def __select_all__(offset: int, limit: int, name: str = ""):
    if not name:
        select_all = db_items.__select_all__(offset, limit)
    else:
        select_all = db_items.__select_all_name__(offset, limit, name)

    print("Parsing...")
    benchmark_time = time.time()
    index = 0
    while index < len(select_all):
        old_data = select_all[index]

        new_data = parse_data(old_data)

        select_all[index] = new_data
        index += 1

    benchmark_time = time.time() - benchmark_time
    print(f"Benchmark time: {benchmark_time} ms")
    return select_all


def __select_one__(timestamp):
    old_data = db_items.__select_one__(timestamp)

    benchmark_time = time.time()

    new_data = parse_data(old_data)

    benchmark_time = time.time() - benchmark_time
    print(f"Benchmark time: {benchmark_time} ms")
    return new_data


def parse_data(old_data):
    if not (type(old_data[5]) == dict):
        lob_data = old_data[5]
        parsed_data = json.loads(str(lob_data))
    else:
        parsed_data = old_data[5]

    new_data = {
        "Timestamp": old_data[0],
        "Name": old_data[1],
        "Price": old_data[2],
        "Quantity": old_data[3],
        "HasImage": old_data[4],
        "MetaData": parsed_data
    }
    if old_data[4] == 1:
        new_data["url"] = backblaze.__get_url__(f"{old_data[0]}")

    return new_data


def api(request_form, request_files):
    db_items.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    sql_method = json_data["sql_method"]
    item_data = json_data["data"]
    if sql_method == "select_all":
        return __select_all__(json_data["offset"], json_data["limit"], item_data["name"])

    elif sql_method == "select_one":
        return __select_one__(item_data["timestamp"])

    elif sql_method == "insert":
        file = request_files.get("file")
        price = format.currency(item_data["price"])
        json_data["timestamp"] = int(time.time())
        if db_items.__insert__(json_data["timestamp"],
                               item_data["name"],
                               item_data["price"],
                               item_data["quantity"],
                               item_data["has_image"],
                               item_data["data"]):
            if (not item_data["has_image"]
                    or backblaze.__upload__(file, str(json_data["timestamp"]))
                        or format.currency_match(price)):
                return True
            print("Something went wrong! Removing item!")
            db_items.__delete__(json_data["timestamp"])

        return False

    elif sql_method == "update":
        if item_data["name"]:
            result = db_items.__update_name__(item_data["timestamp"], item_data["name"])
            if not result:
                return result

        if item_data["price"]:
            price = format.currency(item_data["price"])
            print(price)
            if not format.currency_match(price):
                return False
            result = db_items.__update_price__(item_data["timestamp"], price)
            if not result:
                return result

        if item_data["quantity"]:
            result = db_items.__update_quantity__(item_data["timestamp"], item_data["quantity"])
            if not result:
                return result

        if item_data["data"]:
            result = db_items.__update_data__(item_data["timestamp"], item_data["data"])
            if not result:
                return result

        if item_data["has_image"]:
            result = db_items.__update_has_image__(item_data["timestamp"], item_data["has_image"])
            if not result:
                return result

        return True
    elif sql_method == "delete":
        return db_items.__delete__(item_data["timestamp"])
