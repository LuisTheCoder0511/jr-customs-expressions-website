from flask import Blueprint, render_template, request, jsonify
import database

blueprint = Blueprint('login', __name__)


@blueprint.route("/login")
def login():
    return navigate_url("login")


@blueprint.route("/register")
def register():
    return navigate_url("register")


def navigate_url(url):
    url = f"login_page/{url}/index.html"
    return render_template(url)


@blueprint.route("/submit-data", methods=['POST', 'GET'])
def submit_data():
    json = request.get_json()
    data = json["data"]
    print(data)
    status = "Success"
    return jsonify({"data": data, "status": status})
