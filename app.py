#!flask/bin/python
from flask import Flask, jsonify
from lab1.lab1 import lab1
from lab4.lab4 import lab4
from lab5.lab5 import lab5
from lab6.lab6 import lab6

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
from lab2.lab2 import lab2
from lab6api.lab6api import lab6api

app.register_blueprint(lab1, url_prefix='/lab1')
app.register_blueprint(lab2, url_prefix='/lab2')
app.register_blueprint(lab4, url_prefix='/lab4')
app.register_blueprint(lab5, url_prefix='/lab5')
app.register_blueprint(lab6, url_prefix='/lab6')
app.register_blueprint(lab6api, url_prefix='/lab6/api')

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug="True")