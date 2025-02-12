from flask import Flask, render_template, redirect, url_for
import json

import database
import login

from urls.base_urls import blueprint as base_blueprint
from urls.mcnav_urls import blueprint as mcnav_blueprint
from urls.mcnav_settings_urls import blueprint as mcnav_settings_blueprint
from urls.login_urls import blueprint as login_blueprint

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.register_blueprint(base_blueprint)
app.register_blueprint(mcnav_blueprint)
app.register_blueprint(mcnav_settings_blueprint)
app.register_blueprint(login_blueprint)


@app.route("/")
def home():
    # if __is_mobile__():
    #     return json.dumps({'task': 'home'})

    if login.check_file():
        return render_template("customer/home/index.html")

    return redirect(url_for('login.login'))


@app.route("/item")
def http_item():
    return render_template("customer/mcnav/items/index.html")


@app.route("/seller", methods=['GET'])
def seller_home():
    return render_template("seller/home/index.html")


@app.route("/seller/add", methods=['GET'])
def seller_add():
    return render_template("seller/add/index.html")


@app.route("/seller#get", methods=['GET'])
def seller_http_get():
    datas = database.__select_all__("items")
    return json.dumps(datas)


# @app.route("/seller#add", methods=['POST'])
# def seller_http_add():
#     codes = __code_generator__("items", "item_id")
#     json_data = request.get_json()
#     current_item = item.Item(codes, json_data["name"], json_data["description"], json_data["price"],
#                              json_data["quantity"], json_data["img"], json_data["metadata"])
#     items.__insert__(database, current_item)
#     return json_data


if __name__ == '__main__':
    PORT = 8001

    print("Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"URL: {rule}, Endpoint: {rule.endpoint}")

    app.run(debug=True, host="0.0.0.0", port=PORT, use_reloader=False)
