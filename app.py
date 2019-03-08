#!flask/bin/python
from flask import Flask, jsonify
from lab1.lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1, url_prefix='/lab1')

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(debug="True")