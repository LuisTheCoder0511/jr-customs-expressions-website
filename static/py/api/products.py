import time
import json

from static.py.api.bucket.backblaze import backblaze
from static.py.api.database import db_products
from static.py.api.others import format, id_gens
from static.py.api.others.parser import parse_lob_data


def __select_all__(offset: int, limit: int, name: str = ""):
    if not name:
        select_all = db_products.__select_all_limit__(offset, limit)
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


def __select_one__(product_id: str):
    old_data = db_products.__select_one__(product_id)

    benchmark_time = time.time()

    new_data = parse_data(old_data)

    benchmark_time = time.time() - benchmark_time
    print(f"Benchmark time: {benchmark_time} ms")
    return new_data


def parse_data(old_data):
    parsed_data = parse_lob_data(old_data[4])

    new_data = {
        "ProductID": old_data[0],
        "Name": old_data[1],
        "Price": old_data[2],
        "Quantity": old_data[3],
        "ProductData": parsed_data,
        "ImageURLs": []
    }
    images = parsed_data["images"]
    for url_name in images:
        image_url = backblaze.__get_url__(url_name)
        new_data["ImageURLs"].append(image_url)

    return new_data


def api(request_form, request_files, method):
    db_products.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    product = json_data["data"]

    product_id = product["product_id"]
    product_name = product["name"]
    product_price = product["price"]
    product_quantity = product["quantity"]
    product_data = product["product_data"]

    if method == "select_all":
        return __select_all__(json_data["offset"], json_data["limit"], product_name)

    elif method == "select_one":
        return __select_one__(product_id)

    elif method == "insert":
        product_id = id_gens.generator(db_products.__select_one__, 12)

        files = request_files
        price = format.currency(product_price)

        if not format.currency_match(price):
            print("Price not matching! Cancelled insertion")
            return False

        if db_products.__insert__(product_id,
                                  product_name,
                                  product_price,
                                  product_quantity,
                                  product_data):

            index = 0
            while index <= len(files):
                url_name = f"product_image={product_id} ({index})"
                backblaze.__upload__(files[index], url_name)
                index += 1
            return True

        print("Something went wrong while creating product!")
        return False

    elif method == "update":
        if product_name:
            result = db_products.__update_name__(product_id, product_name)
            if not result:
                return result

        if product_price:
            price = format.currency(product_price)
            print(price)
            if not format.currency_match(price):
                return False
            result = db_products.__update_price__(product_id, price)
            if not result:
                return result

        if product_price:
            result = db_products.__update_quantity__(product_id, product_quantity)
            if not result:
                return result

        if product_data:
            result = db_products.__update_data__(product_id, product_data)
            if not result:
                return result

        return True
    elif method == "delete":
        return db_products.__delete__(product_id)
