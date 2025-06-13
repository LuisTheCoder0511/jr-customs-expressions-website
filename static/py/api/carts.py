import json

from static.py.api.database import db_carts
from static.py.api.others import id_gens

def __select__(cart_id: str):
    data = db_carts.__select__(cart_id)
    return data

def api(request_form, method):
    db_carts.__create_table__()

    data = request_form.get("data")
    json_data = json.loads(data)
    cart = json_data["data"]

    if method == "select":
        return __select__(cart)

    if method == "insert":
        cart_id = id_gens.generator(db_carts.__select__, 12)
        if db_carts.__insert__(cart_id):
            return {"status": True, "cart_id": cart_id}
        print("Something went wrong while creating cart!")
        return False

    elif method == "update":
        if cart["cart_data"]:
            result = db_carts.__update__(cart["cart_id"], cart["cart_data"])
            if not result:
                return result

        return True

    elif method == "delete":
        return db_carts.__delete__(cart["cart_id"])
