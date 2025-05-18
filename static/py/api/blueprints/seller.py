from flask import Blueprint, render_template, request, jsonify, redirect
from static.py.api import items

import json

blueprint = Blueprint('seller', __name__, template_folder='templates', static_folder='static', url_prefix='/seller')

@blueprint.route("/")
def index():
    return redirect("dashboard")

@blueprint.route("/<name>", methods=['GET'])
def seller_content(name):
    header = render_template("seller/base.html")
    template = f"seller/{name}.html"
    body = render_template(template)
    return f"{header}{body}"


