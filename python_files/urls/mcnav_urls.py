from flask import Blueprint, render_template

blueprint = Blueprint('mcnav', __name__, url_prefix='/mcnav')


@blueprint.route("/items")
def seller_items():
    return navigate_url("items")


@blueprint.route("/stats")
def seller_stats():
    return navigate_url("stats")


@blueprint.route("/orders")
def seller_orders():
    return navigate_url("orders")


@blueprint.route("/messages")
def seller_messages():
    return navigate_url("messages")


@blueprint.route("/finance")
def seller_finance():
    return navigate_url("finance")


@blueprint.route("/settings")
def seller_settings():
    return navigate_url("settings")


def navigate_url(url):
    url = f"seller/mcnav/{url}/index.html"
    return render_template(url)
