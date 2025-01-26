from flask import Blueprint, render_template

blueprint = Blueprint('mcnav', __name__, url_prefix='/mcnav')

@blueprint.route("/items")
def seller_items():
    return render_template("seller/mcnav/items/index.html")

