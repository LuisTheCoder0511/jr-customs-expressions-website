from flask import Flask, render_template, request
import json

from python_files.database import Database
from python_files.tables import item, profile
from python_files.codegen import CodeGenerator

app = Flask(__name__)
# app.config["SECRET_KEY"] = "!LuromA!5847"


@app.route("/")
def home():
    if __is_mobile__():
        return json.dumps({'task': 'home'})
    return render_template("home/index.html")


@app.route("/profile#get", methods=['GET'])
def profile_http_get():
    account = request.get_json()
    name = account["name"]
    datas = database.__select_one__("profiles", "name", name)
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
        json_data["phone"]
    )
    database.__insert__("profiles", profile.__keys__(), current_profile.__values__())
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
    codes = __code_generator__("items", "code")
    json_data = request.get_json()
    current_item = item.Item(
        codes,
        json_data["name"],
        json_data["description"],
        json_data["price"],
        json_data["quantity"],
        json_data["item_type"]
    )
    database.__insert__("items", item.__keys__(), current_item.__values__())
    return json_data


def __is_mobile__():
    device = request.headers.get('User-Agent')
    return device.__contains__("Mobile")


def __code_generator__(table_name: str, column_name: str):
    ids = database.__select_all__(table_name, column_name)
    code_gen = CodeGenerator(ids)
    return code_gen.__generate__()


if __name__ == '__main__':
    PORT = 8001
    database = Database("database/test")
    database.__create_table__("items", item.__blueprint__())
    database.__create_table__("profiles", profile.__blueprint__())
    code = __code_generator__("profiles", "code")
    user = profile.Profile(
        code,
        "luroma0511",
        "This is my description",
        "luroma0511@email.com",
        "1234567890"
    )
    database.__insert__("profiles", profile.__keys__(), user.__values__())
    app.run(debug=True, host="0.0.0.0", port=PORT)
