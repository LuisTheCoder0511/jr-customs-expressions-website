import time
import json

from static.py.api.bucket.backblaze import backblaze
from static.py.api.database import db_products
from static.py.api.format import format


def __select_all__(offset: int, limit: int, name: str = ""):
    if not name:
        select_all = db_products.__select_all__(offset, limit)
    else:
        select_all = db_products.__select_all_name__(offset, limit, name)

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


def __select_one__(product_id):
    old_data = db_products.__select_one__(product_id)

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
        "ProductID": old_data[0],
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
    db_products.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    sql_method = json_data["sql_method"]
    product = json_data["data"]

    if sql_method == "select_all":
        return __select_all__(json_data["offset"], json_data["limit"], product["name"])

    elif sql_method == "select_one":
        return __select_one__(product["product_id"])

    elif sql_method == "insert":
        file = request_files.get("file")
        price = format.currency(product["price"])

        if not format.currency_match(price):
            print("Price not matching! Cancelled insertion")
            return False

        if db_products.__insert__(product["name"],
                                  product["price"],
                                  product["quantity"],
                                  product["product_data"]):

            product_images = product["product_data"]["images"]
            for url in product_images:
                backblaze.__upload__(file, url)
            return True

        print("Something went wrong while inserting product!")
        return False

    elif sql_method == "update":
        if product["name"]:
            result = db_products.__update_name__(product["product_id"], product["name"])
            if not result:
                return result

        if product["price"]:
            price = format.currency(product["price"])
            print(price)
            if not format.currency_match(price):
                return False
            result = db_products.__update_price__(product["product_id"], price)
            if not result:
                return result

        if product["quantity"]:
            result = db_products.__update_quantity__(product["product_id"], product["quantity"])
            if not result:
                return result

        if product["product_data"]:
            result = db_products.__update_data__(product["product_id"], product["product_data"])
            if not result:
                return result

        return True
    elif sql_method == "delete":
        return db_products.__delete__(product["product_id"])
