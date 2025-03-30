from flask import Flask, render_template, jsonify, request
import json

from api.database import oracle
from api import items

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home/index.html")

@app.route("/content/<name>")
def home_content(name):
    template = f"home/{name}/index.html"
    print("Template:", template)
    return render_template(template)

@app.route("/item")
def item():
    template = f"item/index.html"
    return render_template(template)

@app.route("/api/database/<name>", methods=["POST"])
def database_content(name):
    data = {}
    if name == "items":
        data = items.api(request.json)

    json_data = json.dumps(data, indent=4)
    print(f"Data: {json_data}")
    return jsonify(data)

if __name__ == "__main__":
    oracle.__run__()
    PORT = 8001
    app.run(port=PORT, debug=True, use_reloader=False)
    oracle.__stop__()
