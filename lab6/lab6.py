from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from auth import auth
import requests

lab6 = Blueprint('lab6', __name__)
base_url = "http://localhost:5000/lab6/api/v1.0/"

@lab6.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@lab6.route('/tests/add', methods=['GET'])
def add_test_form():
    return render_template('addTest.html')

@lab6.route('/tests/add', methods=['POST'])
def add_test():
    url = base_url + 'tests'
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    payload = {
        'name': request.form.get("name"), 
    }
    r = requests.post(url=url, json=payload, headers=headers)
    return redirect('lab6/tests/' + str(r.json()['test_id']) + '/questions/add')

@lab6.route('/tests/<int:test_id>/questions/add', methods=['GET'])
def add_question_form(test_id):
    return render_template('addQuestion.html')

@lab6.route('/tests/<int:test_id>/questions/add', methods=['POST'])
def add_test():
    url = base_url + 'tests/questions/add'
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    payload = {
        'name': request.form.get("name"), 
    }
    r = requests.post(url=url, json=payload, headers=headers)
    return redirect('lab6/tests/' + str(r.json()['test_id']) + '/questions/add')

# @lab5.route('/clients', methods=['GET'])
# def getClients():
#     url = base_url + "clients"
#     headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
#     r = requests.get(url=url, headers=headers)
#     r = r.json()
#     return render_template('clients.html', clients=r['clients'])

# @lab5.route('/clients', methods=['POST'])
# def saveClient():
#     id = request.form.get("id")
#     if id:
#         url = base_url + "clients/" + str(id)
#     else:
#         url = base_url + "clients"
#     headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
#     if (request.form.get("save")):
#         payload = {
#             'FIO': request.form.get("FIO"), 
#             'email': request.form.get("email")
#         }
#         r = requests.put(url=url, json=payload, headers=headers)
#     elif (request.form.get("delete")):
#         r = requests.delete(url=url, headers=headers)
#     else:
#         payload = {
#             'FIO': request.form.get("FIO"), 
#             'email': request.form.get("email")
#         }
#         r = requests.post(url=url, json=payload, headers=headers)
#     return redirect(url_for('lab5.getClients'))