from flask import Blueprint, request
import json

from python_files import database
from python_files.tables import items, profiles, carts
from python_files.objects import item, profile, cart
from python_files.codegen import CodeGenerator

blueprint = Blueprint('base', __name__, url_prefix='/db')


@blueprint.route("/profile#get", methods=['GET'])
def profile_http_get():
    account = request.get_json()
    name = account["name"]
    datas = profiles.__select_one__(database, "name", name)
    if __is_mobile__():
        return json.dumps({'task': 'json_get: ' + datas})
    return json.dumps(datas)


@blueprint.route("/profile#add", methods=['POST'])
def profile_http_add():
    codes = __code_generator__("profiles", "code")
    json_data = request.get_json()
    current_profile = profile.Profile(
        codes,
        json_data["name"],
        json_data["bio"],
        json_data["email"],
        json_data["phone"],
        json_data["img"],
        json_data["cart_id"],
    )
    profiles.__insert__(database, current_profile)
    return json_data


@blueprint.route("/seller#get", methods=['GET'])
def seller_http_get():
    datas = database.__select_all__("items")
    if __is_mobile__():
        return json.dumps({'task': 'json_get: ' + datas})
    return json.dumps(datas)


@blueprint.route("/seller#add", methods=['POST'])
def seller_http_add():
    codes = __code_generator__("items", "item_id")
    json_data = request.get_json()
    current_item = item.Item(codes, json_data["name"], json_data["description"], json_data["price"],
                             json_data["quantity"], json_data["img"], json_data["metadata"])
    items.__insert__(database, current_item)
    return json_data