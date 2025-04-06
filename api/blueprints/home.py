from flask import Blueprint, render_template, request, jsonify
from api import items

import json

blueprint = Blueprint('home', __name__)

@blueprint.route("/")
def index():
    return render_template("home/index.html")

@blueprint.route("/content/<name>")
def home_content(name):
    template = f"home/{name}/index.html"
    print("Template:", template)
    return render_template(template)

@blueprint.route("/item")
def item():
    template = f"item/index.html"
    return render_template(template)

@blueprint.route("/api/database/<name>", methods=["POST"])
def database_content(name):
    data = {}
    if name == "items":
        data = items.api(request.json)

    json_data = json.dumps(data, indent=4)
    print(f"Data: {json_data}")
    return jsonify(data)