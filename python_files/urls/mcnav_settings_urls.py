from flask import Blueprint, render_template

blueprint = Blueprint('mcnav_settings', __name__, url_prefix='/mcnav/settings')


@blueprint.route("/account")
def settings_account():
    return navigate_url("account")


@blueprint.route("/security")
def settings_security():
    return navigate_url("security")


@blueprint.route("/privacy")
def settings_privacy():
    return navigate_url("privacy")


@blueprint.route("/address")
def settings_address():
    return navigate_url("address")


@blueprint.route("/credit")
def settings_credit():
    return navigate_url("credit")


@blueprint.route("/email")
def settings_email():
    return navigate_url("email")


def navigate_url(url):
    url = f"seller/mcnav/settings/{url}/index.html"
    return render_template(url)
