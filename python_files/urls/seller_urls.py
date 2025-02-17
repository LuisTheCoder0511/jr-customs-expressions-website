import json
import struct

from flask import Blueprint, request, jsonify
from python_files.objects.item import Item
from python_files.tables import items
from python_files import database

blueprint = Blueprint('seller-item', __name__, url_prefix="/seller-item")


def convert_bytes(data):
    str_value = json.dumps(data)
    byte_encode = str_value.encode('utf-8')
    len_bytes = struct.pack('>I', len(byte_encode))
    return len_bytes + byte_encode


def reconvert_bytes(data):
    len_bytes = data[:4]
    length = struct.unpack('>I', len_bytes)[0]

    byte_encode = data[4:4 + length]

    str_value = byte_encode.decode('utf-8')

    return json.loads(str_value)


def add(data):
    name = data['name']
    description = data['description']

    image = convert_bytes(data['image'])
    categoryIDs = convert_bytes(data['categoryIDs'])

    price = data['price']
    quantity = data['quantity']
    meta = data['meta']

    current_item = Item(name,
                        description,
                        image,
                        categoryIDs,
                        price,
                        quantity,
                        meta)

    if not items.__retrieve_id__(current_item):
        result = items.__insert__(current_item)
        print(f"Insert... {result}")
        items.__retrieve_id__(current_item)
        return True

    return False


def get(data):
    name = data['name']
    return None


def get_all(data):
    limit = data['limit']
    offset = data['offset']
    filter_name = data['filter']
    if not filter:
        return items.__select_all__(limit, offset)
    return items.__select_all_where__("name", filter_name, False)


def delete():
    pass


@blueprint.route('/', methods=['POST', 'GET'])
def seller_item():
    data = request.get_json()
    arg = data['arg']
    get_data = {}
    success = False

    print("Executing")

    database.__create_connection__()
    if arg == "add":
        success = add(data)

    elif arg == "get_all":
        get_data = get_all(data)
        index = 0
        for item in get_data:
            current_item = list(item)
            image_bytes = current_item[3]
            categoryIDs_bytes = current_item[4]
            image = reconvert_bytes(image_bytes)
            categoryIDs = reconvert_bytes(categoryIDs_bytes)
            current_item[3] = image
            current_item[4] = categoryIDs
            get_data[index] = tuple(current_item)
            index += 1

        success = True

    elif arg == "get":
        get_data = get(data)

    elif arg == "delete":
        pass

    database.__close_connection__()
    return jsonify({"response": "ok", "success": success, "get": get_data})
