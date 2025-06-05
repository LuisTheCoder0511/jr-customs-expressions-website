from flask import render_template, Blueprint, request, jsonify

from static.py.api import webpage, items

blueprint = Blueprint("home", __name__)

@blueprint.route("/")
def index():
    return render_template("home.html")

@blueprint.route("/api/<name>", methods=["GET", "POST"])
def api(name):
    data = {}
    if name == "items":
        data = items.api(request.form, None)
    elif name == "webpage":
        data = webpage.api(request.form)

    return jsonify(data)