from flask import Blueprint, render_template

blueprint = Blueprint('base', __name__, url_prefix='/base')


@blueprint.route("/header")
def base_header():
    return navigate_url("header")


@blueprint.route("/items")
def base_item():
    return navigate_url("items")


@blueprint.route("/reviews")
def base_review():
    return navigate_url("reviews")


def navigate_url(url):
    url = f"customer/mcnav/{url}/index.html"
    return render_template(url)
