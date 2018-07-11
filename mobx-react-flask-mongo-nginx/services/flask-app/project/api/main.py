from flask import current_app, Blueprint, jsonify
from pymongo import MongoClient
from bson import json_util
import json
import os

main_blueprint = Blueprint('main', __name__)
client = MongoClient(os.getenv('DATABASE_HOST'), 27017)


@main_blueprint.route('/flask/ping', methods=["GET"])
def ping():
    return jsonify({'status': 'success', 'data': 'Pong!!'})

