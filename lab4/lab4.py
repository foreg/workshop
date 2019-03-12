from flask import Blueprint, jsonify, request
from auth import auth
import requests

lab4 = Blueprint('lab4', __name__)

@lab4.route('/api/v1.0/otherapis', methods=['GET'])
@auth.login_required
def getResponseFromOtherApi():
    r = requests.get('http://www.mocky.io/v2/5c7db5e13100005a00375fda')
    r = r.json()['result'].replace(' ', '_')
    return jsonify({'response': r}), 200