import os

from flask import Flask

from static.py.api.bucket.backblaze import backblaze
from env_files import env_load

from static.py.api.database import oracle
from static.py.api.blueprints.customer import blueprint as customer_blueprint
from static.py.api.blueprints.seller import blueprint as seller_blueprint

if __name__ == "__main__":
    environment = 0
    local = False
    cloud = False

    while True:
        try:
            environment = int(input("1: local, 2: cloud... "))
            if environment == 1 or environment == 2:
                break
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            print("Environment value must be either 1 or 2.")

    local = environment == 1
    cloud = environment == 2

    print("Initializing...")
    app = Flask(__name__, root_path=os.getcwd())
    app.register_blueprint(customer_blueprint)
    app.register_blueprint(seller_blueprint)

    if local:
        env_load.load()

    backblaze.__authenticate__()
    oracle.__run__(local)
    PORT = 8001
    host = None
    if cloud:
        host = '0.0.0.0'
    app.run(host=host, port=PORT, debug=local, use_reloader=False)
    oracle.__stop__()
