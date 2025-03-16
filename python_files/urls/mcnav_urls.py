from flask import Blueprint, render_template, request

blueprint = Blueprint('mcnav', __name__, url_prefix="/mcnav")


@blueprint.route('/', methods=['POST'])
def mcnav():
    data = request.get_json()
    client = data['client']
    arg = data['arg']
    arg_extra = data['arg_extra']

    url = f"{client}/mcnav/{arg}{arg_extra}/index.html"

    print(f"URL: {url}")

    return render_template(url)

