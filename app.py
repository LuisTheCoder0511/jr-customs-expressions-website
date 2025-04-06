from flask import Flask

from api.database import oracle
from api.blueprints.home import blueprint as home_blueprint

app = Flask(__name__)
app.register_blueprint(home_blueprint)

if __name__ == "__main__":
    oracle.__run__()
    PORT = 8001
    app.run(host='0.0.0.0', port=PORT, debug=True, use_reloader=False)
    oracle.__stop__()
