import time
import json

from api.bucket.backblaze import backblaze
from api.database import db_items


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
        lob_data = old_data[5]
        parsed_data = json.loads(str(lob_data))
        new_data = {
            "Timestamp": old_data[0],
            "Name": old_data[1],
            "Price": old_data[2],
            "Quantity": old_data[3],
            "HasImage": old_data[4],
            "MetaData": parsed_data
        }
        if old_data[4] == 1:
            new_data["url"] = backblaze.__get_url__(f"{old_data[0]}.png")

        select_all[index] = new_data
        index += 1
    benchmark_time = time.time() - benchmark_time
    print(f"Benchmark time: {benchmark_time} ms")
    return select_all


def api(request_json):
    data = request_json.get("data")
    sql_method = request_json.get("sql_method")
    if sql_method == "select_all":
        return __select_all__(request_json["offset"], request_json["limit"], data["name"])

    elif sql_method == "select_one":
        return db_items.__select_one__(data["timestamp"])

    elif sql_method == "insert":
        if db_items.__insert__(data["timestamp"], data["name"], data["price"], data["quantity"], data["has_image"], data["data"]):
            if not data["has_image"] or backblaze.__upload__(data["filename"], data["timestamp"]):
                return True
            print("Something went wrong! Removing item!")
            db_items.__delete__(data["timestamp"])

        return False

    elif sql_method == "update":
        if data["name"]:
            result = db_items.__update_name__(data["timestamp"], data["name"])
            if not result:
                return result

        if data["price"]:
            result = db_items.__update_price__(data["timestamp"], data["price"])
            if not result:
                return result

        if data["quantity"]:
            result = db_items.__update_quantity__(data["timestamp"], data["quantity"])
            if not result:
                return result

        if data["data"]:
            result = db_items.__update_data__(data["timestamp"], data["data"])
            if not result:
                return result

        if data["has_image"]:
            result = db_items.__update_has_image__(data["timestamp"], data["has_image"])
            if not result:
                return result

        return True
    elif sql_method == "delete":
        return db_items.__delete__(data["timestamp"])
