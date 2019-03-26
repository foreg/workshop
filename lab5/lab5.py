from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from auth import auth
import requests

lab5 = Blueprint('lab5', __name__)
base_url = "http://localhost:5000/lab2/api/v1.0/"

@lab5.route('/clients', methods=['GET'])
def getClients():
    url = base_url + "clients"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    r = requests.get(url=url, headers=headers)
    r = r.json()
    return render_template('clients.html', clients=r['clients'])

@lab5.route('/clients', methods=['POST'])
def saveClient():
    id = request.form.get("id")
    if id:
        url = base_url + "clients/" + str(id)
    else:
        url = base_url + "clients"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    if (request.form.get("save")):
        payload = {
            'FIO': request.form.get("FIO"), 
            'email': request.form.get("email")
        }
        r = requests.put(url=url, json=payload, headers=headers)
    elif (request.form.get("delete")):
        r = requests.delete(url=url, headers=headers)
    else:
        payload = {
            'FIO': request.form.get("FIO"), 
            'email': request.form.get("email")
        }
        r = requests.post(url=url, json=payload, headers=headers)
    return redirect(url_for('lab5.getClients'))

@lab5.route('/services', methods=['GET'])
def getServices():
    url = base_url + "services"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    r = requests.get(url=url, headers=headers)
    r = r.json()
    return render_template('services.html', services=r['services'])

@lab5.route('/services', methods=['POST'])
def saveService():
    id = request.form.get("id")
    if id:
        url = base_url + "services/" + str(id)
    else:
        url = base_url + "services"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    if (request.form.get("save")):
        payload = {
            'name': request.form.get("name"), 
            'price': request.form.get("price")
        }
        r = requests.put(url=url, json=payload, headers=headers)
    elif (request.form.get("delete")):
        r = requests.delete(url=url, headers=headers)
    else:
        payload = {
            'name': request.form.get("name"), 
            'price': request.form.get("price")
        }
        r = requests.post(url=url, json=payload, headers=headers)
    return redirect(url_for('lab5.getServices'))

@lab5.route('/requests', methods=['GET'])
def getRequests():
    url = base_url + "requests"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    r = requests.get(url=url, headers=headers)
    r = r.json()
    return render_template('requests.html', requests=r['requests'])

@lab5.route('/requests', methods=['POST'])
def saveRequest():
    id = request.form.get("id")
    if id:
        url = base_url + "requests/" + str(id)
    else:
        url = base_url + "requests"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    if (request.form.get("save")):
        payload = {
            'client_id': request.form.get("client_id"), 
            'service_id': request.form.get("service_id"),
            'date': request.form.get("date")
        }
        r = requests.put(url=url, json=payload, headers=headers)
    elif (request.form.get("delete")):
        r = requests.delete(url=url, headers=headers)
    else:
        payload = {
            'client_id': request.form.get("client_id"), 
            'service_id': request.form.get("service_id"),
            'date': request.form.get("date")
        }
        r = requests.post(url=url, json=payload, headers=headers)
    return redirect(url_for('lab5.getRequests'))