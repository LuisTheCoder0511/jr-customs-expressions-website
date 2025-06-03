from flask import Blueprint, render_template, request, jsonify, redirect
from static.py.api import items

import json

blueprint = Blueprint('seller', __name__, template_folder='templates', static_folder='static', url_prefix='/seller')

@blueprint.route("/")
def index():
    return redirect("content/dashboard")

@blueprint.route("/content/<name>", methods=['GET'])
def seller_content(name):
    header = render_template("seller/base.html")
    template = f"seller/{name}.html"
    body = render_template(template)
    return f"{header}{body}"

@blueprint.route("/template/<name>")
def seller_template(name):
    template = f"seller/{name}.html"
    print(template)
    return render_template(template)

@blueprint.route("/api/<name>", methods=["POST"])
def seller_api(name):
    data = {}
    if name == "items":
        data = items.api(request.form, request.files)

    json_data = json.dumps(data, indent=4)
    print(f"Data: {json_data}")
    return jsonify(data)
