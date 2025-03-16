from flask import Blueprint, request, render_template, jsonify

blueprint = Blueprint("about_route", __name__, url_prefix="/about")


@blueprint.route("/query")
def query():

    return jsonify()


@blueprint.route("/")
def about():
    url = "customer/home/content/about.html"
    return render_template(url)

