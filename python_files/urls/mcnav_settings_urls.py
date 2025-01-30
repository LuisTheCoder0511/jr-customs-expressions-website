from flask import Blueprint, render_template

blueprint = Blueprint('mcnav_settings', __name__, url_prefix='/mcnav/settings')


@blueprint.route("/account")
def seller_items():
    return navigate_url("account")


@blueprint.route("/security")
def seller_stats():
    return navigate_url("security")


@blueprint.route("/privacy")
def seller_orders():
    return navigate_url("privacy")


@blueprint.route("/address")
def seller_messages():
    return navigate_url("address")


@blueprint.route("/credit")
def seller_finance():
    return navigate_url("credit")


@blueprint.route("/email")
def seller_settings():
    return navigate_url("email")


def navigate_url(url):
    url = f"seller/mcnav/settings/{url}/index.html"
    return render_template(url)
