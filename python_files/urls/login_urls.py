from flask import Blueprint, render_template

blueprint = Blueprint('login', __name__, url_prefix='/login')


@blueprint.route("/")
def login():
    return navigate_url("login")


@blueprint.route("/register")
def register():
    return navigate_url("register")


def navigate_url(url):
    url = f"login_page/{url}/index.html"
    return render_template(url)
