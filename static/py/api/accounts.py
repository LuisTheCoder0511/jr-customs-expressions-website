import json

from static.py.api.bucket.backblaze import backblaze
from static.py.api.database import db_accounts
from static.py.api.others import id_gens

def __select__(account_id: str):
    data = db_accounts.__select__(account_id)
    print(data)
    return data

def api(request_form, request_files):
    db_accounts.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    sql_method = json_data["sql_method"]
    account = json_data["data"]

    if sql_method == "select":
        return __select__(account["account_id"])

    elif sql_method == "insert":
        account_id = id_gens.generator(db_accounts.__select__, 12)

        files = request_files

        if db_accounts.__insert__(account_id,
                                  account["username"],
                                  account["account_data"]):
            url_name = f"user_image={account_id}"
            backblaze.__upload__(files[0], url_name)
            return True
        print("Something went wrong while creating account!")
        return False

    elif sql_method == "update":
        if account["username"]:
            result = db_accounts.__update_username__(account["account_id"], account["username"])
            if not result:
                return result

        if account["account_data"]:
            result = db_accounts.__update_data__(account["account_id"], account["account_data"])
            if not result:
                return result

        return True

    elif sql_method == "delete":
        return db_accounts.__delete__(account["account_id"])
