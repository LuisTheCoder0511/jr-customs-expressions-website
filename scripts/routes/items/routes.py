from flask import Blueprint, render_template, jsonify
from scripts.backend import item

blueprint = Blueprint("items_route", __name__, url_prefix="/items")


@blueprint.route("/query/<limit>/<offset>/<filter>")
def query(limit, offset, filter):
    data = {
        "arg": "select_all",
        "limit": limit,
        "offset": offset,
        "filter": filter
    }
    item.api(data)
    return jsonify(data["get_data"])


@blueprint.route("/")
def item_home():
    url = "customer/home/content/items.html"
    return render_template(url)


# @blueprint.route("/<item>")
# def item_page():
#     url = "customer/"
#     return render_template(url)


@blueprint.route("/seller/<item>")
def item_seller_page():
    url = "seller"
    return render_template(url)
