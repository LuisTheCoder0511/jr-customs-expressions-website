from flask import Flask, render_template, request
import json

import database
from tables import items, profiles, carts
from objects import item, profile, cart
from codegen import CodeGenerator

from urls.base_urls import blueprint as base_blueprint
from urls.mcnav_urls import blueprint as mcnav_blueprint

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.register_blueprint(base_blueprint)
app.register_blueprint(mcnav_blueprint)


@app.route("/")
def home():



    if __is_mobile__():
        return json.dumps({'task': 'home'})
    return render_template("home/index.html")


@app.route("/item")
def http_item():
    return render_template("item/index.html")


@app.route("/profile#get", methods=['GET'])
def profile_http_get():
    account = request.get_json()
    name = account["name"]
    datas = profiles.__select_one__(database, "name", name)
    if __is_mobile__():
        return json.dumps({'task': 'json_get: ' + datas})
    return json.dumps(datas)


@app.route("/profile#add", methods=['POST'])
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


@app.route("/seller", methods=['GET'])
def seller_home():
    if __is_mobile__():
        return json.dumps({'task': 'seller_home'})
    return render_template("seller/home/index.html")


@app.route("/seller/add", methods=['GET'])
def seller_add():
    if __is_mobile__():
        return json.dumps({'task': 'seller_add'})
    return render_template("seller/add/index.html")


@app.route("/seller#get", methods=['GET'])
def seller_http_get():
    datas = database.__select_all__("items")
    if __is_mobile__():
        return json.dumps({'task': 'json_get: ' + datas})
    return json.dumps(datas)


@app.route("/seller#add", methods=['POST'])
def seller_http_add():
    codes = __code_generator__("items", "item_id")
    json_data = request.get_json()
    current_item = item.Item(codes, json_data["name"], json_data["description"], json_data["price"],
                             json_data["quantity"], json_data["img"], json_data["metadata"])
    items.__insert__(database, current_item)
    return json_data


def __is_mobile__():
    device = request.headers.get('User-Agent')
    return device.__contains__("Mobile")


if __name__ == '__main__':
    PORT = 8001

    database.__create_connection__()
    items.__create_table__(database)
    profiles.__create_table__(database)
    carts.__create_table__(database)
    database.__close_connection__()

    app.run(debug=True, host="0.0.0.0", port=PORT, use_reloader=False)
