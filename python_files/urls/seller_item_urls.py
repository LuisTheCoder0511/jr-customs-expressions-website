from flask import Blueprint, request, jsonify
from python_files.api import item_api

blueprint = Blueprint('seller-item', __name__, url_prefix="/seller-item")


@blueprint.route('/', methods=['POST', 'GET'])
def seller_item():
    data = request.get_json()
    get_data = {
        "data": data,
        "status": "success"
    }

    item_api.execute(get_data)

    return jsonify({"response": "ok", "status": get_data['status'], "get": get_data['data']})
