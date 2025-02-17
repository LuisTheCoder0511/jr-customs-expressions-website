from flask import Blueprint, render_template, request

blueprint = Blueprint('mcnav', __name__, url_prefix="/mcnav")


@blueprint.route('/', methods=['POST'])
def mcnav():
    data = request.get_json()
    arg = data['arg']
    return render_template(f"seller/mcnav/{arg}/index.html")

