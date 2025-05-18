from flask import Blueprint, render_template, request, jsonify
from static.py.api import items

import json

blueprint = Blueprint('customer', __name__, template_folder='templates', static_folder='static')

@blueprint.route("/")
def index():
    return render_template("customer/base.html")

@blueprint.route("/customer/<name>", methods=['GET'])
def customer_content(name):
    header = index()
    template = f"customer/{name}.html"
    print("Template:", template)
    body = render_template(template)
    return f"{header}{body}"

@blueprint.route("/customer/divs/item")
def item_div():
    template = "customer/item_div.html"
    return render_template(template)

@blueprint.route("/customer/api/<name>", methods=["POST"])
def database_content(name):
    data = {}
    if name == "items":
        data = items.api(request.json)

    json_data = json.dumps(data, indent=4)
    print(f"Data: {json_data}")
    return jsonify(data)
