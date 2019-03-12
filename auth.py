from flask import jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    if username == 'dmitry':
        return '1234'
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 403