import time

from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from scripts.backend import customer, password

blueprint = Blueprint("customer_route", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def home():
    print("Redirecting home page")
    url = "customer/home/index.html"
    return render_template(url)


@blueprint.route("/customer/signout")
def signout():
    customer.write_user()
    return jsonify({"status": "ok"})


@blueprint.route("/account/<arg>")
def account(arg):
    url = f"customer/home/templates/{arg}.html"
    return render_template(url)


@blueprint.route("/login_label/<arg>")
def login_label(arg):
    url = f"customer/login/templates/{arg}.html"
    return render_template(url)


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    url = "customer/login/index.html"
    return render_template(url)


@blueprint.route("/login/submit", methods=["POST"])
def submit_login():
    username = request.form.get("username")
    name = request.form.get("name")
    raw_password = request.form.get("password")
    register = request.form.get("register")

    if register == "true":
        hashed_password = password.encrypt_password(raw_password)
        data = {
            "username": username,
            "name": name,
            "hashed_password": hashed_password,
            "arg": "insert"
        }

        customer.api(data)

        if data["exists"]:
            return redirect(url_for("customer_route.login", cause="accountExists"))
    else:
        data = {
            "username": username,
            "name": name,
            "password": raw_password,
            "arg": "select"
        }

        customer.api(data)

        if not data["exists"]:
            return redirect(url_for("customer_route.login", cause="accountMissing"))
        elif data["invalid"]:
            return redirect(url_for("customer_route.login", cause="passwordInvalid"))

    remember = request.form.get("remember") == "visible"

    print(username, password, remember)
    if not username or not password:
        return redirect(url_for("customer_route.login", cause="accountRequired"))

    data = {
        "account": {
            "username": username,
            "timestamp": int(time.time()),
            "remember": remember
        }
    }

    customer.write_user(data)
    return redirect(url_for("customer_route.home"))


@blueprint.route("/read-account")
def read_account():
    result = customer.read_user()
    return jsonify(result)


@blueprint.route("/read-user/<username>")
def read_user(username):
    data = {
        "username": username,
        "arg": "select"
    }

    customer.api(data, False)

    return jsonify(data)
