from flask import Blueprint, render_template, request, jsonify, redirect
from static.py.api import products, webpage

import json

blueprint = Blueprint('customer', __name__, template_folder='templates', static_folder='static')

@blueprint.route("/")
def index():
    return redirect("/customer/content/items")

@blueprint.route("/customer/content/<name>", methods=['GET'])
def customer_content(name):
    header = render_template("customer/base.html")
    template = f"customer/{name}.html"
    print(template)
    body = render_template(template)
    return f"{header}{body}"

@blueprint.route("/customer/template/<name>")
def customer_template(name):
    template = f"customer/{name}.html"
    print(template)
    return render_template(template)

@blueprint.route("/customer/api/<name>", methods=["POST"])
def customer_api(name):
    data = {}
    if name == "items":
        data = items.api(request.form, None)

    elif name == "webpage":
        data = webpage.api(request.form)

    json_data = json.dumps(data, indent=4)
    print(f"Data: {json_data}")
    return jsonify(data)
