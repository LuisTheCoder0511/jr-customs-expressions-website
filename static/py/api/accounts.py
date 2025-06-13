import json

from static.py.api.bucket.backblaze import backblaze
from static.py.api.database import db_accounts
from static.py.api.others import id_gens

def __select_id__(account_id: str):
    data = db_accounts.__select_id__(account_id)
    return data

def __select_username__(username: str):
    data = db_accounts.__select_username__(username)
    return data

def api(request_form, request_files, method):
    db_accounts.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    account = json_data["data"]

    if method == "select_username":
        return __select_username__(account["username"])

    elif method == "insert":
        account_id = id_gens.generator(db_accounts.__select_id__, 12)
        if db_accounts.__insert__(account_id,
                                    account["password_id"],
                                    account["cart_id"],
                                    account["username"]):
            return True
        print("Something went wrong while creating account!")
        return False

    elif method == "update":
        account_id = account["account_id"]
        if account["username"]:
            result = db_accounts.__update_username__(account["account_id"], account["username"])
            if not result:
                return result

        if account["order_ids"]:
            result = db_accounts.__update_order_ids__(account["account_id"], account["order_ids"])
            if not result:
                return result

        if account["account_data"]:
            if account["account_data"]["upload_img"]:
                files = request_files["files"]

                url_name = f"user_image={account_id}"
                backblaze.__upload__(files[0], url_name)

            result = db_accounts.__update_data__(account["account_id"], account["account_data"])
            if not result:
                return result

        return True

    elif method == "delete":
        return db_accounts.__delete__(account["account_id"])
