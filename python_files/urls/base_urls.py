from flask import Blueprint, render_template

blueprint = Blueprint('base', __name__, url_prefix='/base')

@blueprint.route("/header")
def base_header():
    print(blueprint.url_prefix)
    return render_template("base/header/index.html")

@blueprint.route("/items")
def base_item():
    return render_template("base/item/index.html")

@blueprint.route("/reviews")
def base_review():
    return render_template("base/review/index.html")
