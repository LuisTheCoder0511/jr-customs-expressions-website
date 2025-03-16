import logging

from flask import Flask, render_template, redirect, url_for
from python_files.oracle import oracle
from python_files import login

from python_files.urls.base_urls import blueprint as base_blueprint
from python_files.urls.mcnav_settings_urls import blueprint as mcnav_settings_blueprint
from python_files.urls.login_urls import blueprint as login_blueprint
from python_files.urls.mcnav_urls import blueprint as mcnav_blueprint
from python_files.urls.mcnav_items import blueprint as mcnav_items_blueprint
from python_files.urls.seller_item_urls import blueprint as seller_item_blueprint
from python_files.urls.customer_item_urls import blueprint as customer_item_blueprint

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.register_blueprint(base_blueprint)
app.register_blueprint(login_blueprint)
app.register_blueprint(mcnav_blueprint)
app.register_blueprint(mcnav_settings_blueprint)
app.register_blueprint(mcnav_items_blueprint)
app.register_blueprint(seller_item_blueprint)
app.register_blueprint(customer_item_blueprint)


@app.route("/")
def home():
    return render_template("customer/home/index.html")


@app.route("/seller", methods=['GET'])
def seller_home():
    return render_template("seller/home/index.html")


if __name__ == '__main__':
    oracle.__run__()

    PORT = 8001
    print("Available routes:")
    for rule in app.url_map.iter_rules():
        print(f"URL: {rule}, Endpoint: {rule.endpoint}")

    app.logger.setLevel(logging.ERROR)
    app.run(debug=True, host="0.0.0.0", port=PORT, use_reloader=False)
    oracle.__stop__()
