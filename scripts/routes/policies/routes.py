from flask import Blueprint, request, render_template, jsonify

blueprint = Blueprint("policies_route", __name__, url_prefix="/policies")


@blueprint.route("/query")
def query():

    return jsonify()


@blueprint.route("/")
def policies():
    url = "customer/home/content/policies.html"
    return render_template(url)

