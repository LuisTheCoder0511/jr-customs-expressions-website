import json

from flask import render_template, Blueprint, request, jsonify, send_file, redirect

from static.py.api import webpage, products, accounts, passwords, carts, orders
from static.py.api.others import session

blueprint = Blueprint("routes", __name__)

@blueprint.route("/")
def customer_index():
    return redirect("/customer_page/home")

@blueprint.route("/seller_page")
def seller_index():
    return redirect("/seller_page/customize")

@blueprint.route("/customer_page/<name>")
def customer_page(name):
    print("Redirecting to /customer_page/" + name)
    return render_template("customer/" + name + ".html")

@blueprint.route("/seller_page/<name>")
def seller_page(name):
    return render_template("seller/" + name + ".html")

@blueprint.route("/customer_base/<name>")
def customer_base(name):
    return send_file("templates/customer/base/" + name + ".html", mimetype="text/html")

@blueprint.route("/seller_base/<name>")
def seller_base(name):
    return send_file("templates/seller/base/" + name + ".html", mimetype="text/html")

@blueprint.route("/api/<name>/<method>", methods=["GET", "POST"])
def api(name, method):
    data = {}
    form_data = request.form.to_dict()
    print(f"Name: {name}")
    print(f"Method: {method}")
    if name == "login":
        login(data, form_data, method)
    elif name == "products":
        data = products.api(form_data, request.files, method)
    elif name == "webpage":
        data = webpage.api(form_data, method)

    return jsonify(data)


def login(data, form_data, method):
    if method == "register":
        result = accounts.api(form_data, None, "select_username")
        print("Account checked!")
        print(result)

        result = passwords.api(form_data, "insert")
        print("Password checked!")
        print(result)
        password_id = result["password_id"]

        result = carts.api(form_data, "insert")
        print("Cart created!")
        print(result)
        cart_id = result["cart_id"]

        temp_data = form_data.get("data")
        json_data = json.loads(temp_data)
        json_data["data"]["password_id"] = password_id
        json_data["data"]["cart_id"] = cart_id
        temp_data = json.dumps(json_data)
        form_data["data"] = temp_data

        result = accounts.api(form_data, None, "insert")
        print("Account created!")
        print(result)

        session.write_file(json_data["data"])
        data["redirect"] = True

    if method == "login":
        result = accounts.api(form_data, None, "select_username")
        if not result:
            data["error"] = "Password not valid"
            return jsonify(data)

        print("Account found!")
        print(result)
        password_id = result[1]

        temp_data = form_data.get("data")
        json_data = json.loads(temp_data)
        json_data["data"]["password_id"] = password_id
        temp_data = json.dumps(json_data)
        form_data["data"] = temp_data

        result = passwords.api(form_data, "authenticate")
        if not result:
            data["error"] = "Password not valid"
            return jsonify(data)

        print("Password authenticated!")
        print(result)
        data["redirect"] = True

        json_data = json.loads(form_data.get("data"))

        session.write_file(json_data["data"])