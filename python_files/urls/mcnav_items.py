from flask import Blueprint, render_template, request

blueprint = Blueprint('mcnav_items', __name__, url_prefix='/mcnav/items')


@blueprint.route('/', methods=['POST'])
def mcnav_items():
    data = request.get_json()
    arg = data['arg']
    return render_template(f"seller/mcnav/items/{arg}/index.html")