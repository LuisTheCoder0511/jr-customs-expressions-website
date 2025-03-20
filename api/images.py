import time

from api.bucket.aws import aws
from api.database import db_images


def insert(url: str):
    aws.__upload__(url)
    url = f"https://{aws.bucket_name}.s3.amazonaws.com/uploads/{url}"
    db_images.__insert__(int(time.time()), url)


def delete(url: str):



def api(request_json):
    data = request_json.get("data")
    sql_method = request_json.get("sql_method")

    if sql_method == "update":
        delete(data["timestamp"])
        insert(data["url"])
        db_images.__insert__(int(time.time()), data["url"])

    if sql_method == "select_count":
        return db_images.__select_count__(data["url"])
    elif sql_method == "select_one":
        return db_images.__select_one__(data["timestamp"])
    elif sql_method == "insert":
        return insert(data["url"])
    elif sql_method == "delete":
        return db_images.__delete__(data["timestamp"])