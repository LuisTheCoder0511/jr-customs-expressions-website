from flask import render_template, Blueprint, request, jsonify, send_file

from static.py.api import webpage, items

blueprint = Blueprint("routes", __name__)

@blueprint.route("/")
def index():
    return render_template("home.html")

@blueprint.route("/page/<name>")
def page(name):
    return render_template(name + ".html")

@blueprint.route("/base/<name>")
def template(name):
    return send_file("templates/base/" + name + ".html", mimetype="text/html")

@blueprint.route("/api/<name>", methods=["GET", "POST"])
def api(name):
    data = {}
    if name == "items":
        data = items.api(request.form, None)
    elif name == "webpage":
        data = webpage.api(request.form)

    return jsonify(data)