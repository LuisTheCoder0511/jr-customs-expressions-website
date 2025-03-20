import time
import json

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
        lob_data = old_data[4]
        parsed_data = json.loads(str(lob_data))
        new_data = (
            old_data[0],
            old_data[1],
            old_data[2],
            old_data[3],
            parsed_data
        )
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
        return db_items.__insert__(data["timestamp"], data["name"], data["price"], data["quantity"], data["data"])
    elif sql_method == "update":
        if data["name"]:
            return db_items.__update_name__(data["timestamp"], data["name"])
        elif data["price"]:
            return db_items.__update_price__(data["timestamp"], data["price"])
        elif data["quantity"]:
            return db_items.__update_quantity__(data["timestamp"], data["quantity"])
        elif data["data"]:
            return db_items.__update_data__(data["timestamp"], data["data"])
    elif sql_method == "delete":
        return db_items.__delete__(data["timestamp"])
