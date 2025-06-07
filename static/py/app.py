import os

from flask import Flask

from static.py.api.bucket.backblaze import backblaze
from env_files import env_load

from static.py.api.database import oracle

from static.py.blueprints.routes import blueprint

if __name__ == "__main__":
    environment = 0
    local = False
    cloud = False
    public = False

    while True:
        try:
            environment = int(input("1: local, 2: cloud, 3: public... "))
            if environment == 1 or environment == 2 or environment == 3:
                break
        except ValueError:
            print("Invalid input. Please try again.")
        else:
            print("Environment value must be either 1, 2, or 3.")

    local = environment == 1 or environment == 3
    cloud = environment == 2
    public = environment == 3

    print("Initializing...")
    app = Flask(__name__, root_path=os.getcwd())
    app.register_blueprint(blueprint)

    if local:
        env_load.load()

    backblaze.__authenticate__()
    oracle.__run__(local)
    PORT = 8001
    if public:
        host = '127.0.0.1'
    else:
        host = '0.0.0.0'

    app.run(host=host, port=PORT, debug=local, use_reloader=False)
    oracle.__stop__()
