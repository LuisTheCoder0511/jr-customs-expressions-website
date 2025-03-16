from flask import Blueprint, request, render_template, jsonify

blueprint = Blueprint("reviews_route", __name__, url_prefix="/reviews")


@blueprint.route("/query")
def query():

    return jsonify()


@blueprint.route("/")
def reviews():
    url = "customer/home/content/reviews.html"
    return render_template(url)

