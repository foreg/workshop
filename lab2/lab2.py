from flask import Blueprint, jsonify, request, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth import auth
from app import app
import sys

lab2 = Blueprint('lab2', __name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .models import Client, Service, Request

#region Clients CRUD
@lab2.route('/api/v1.0/clients', methods=['GET'])
@auth.login_required
def get_clients():
    clients = Client.query.all()
    clients_json = [{'id':c.id, 'FIO':c.FIO, 'email':c.email} for c in clients]
    return jsonify({'clients': clients_json})

@lab2.route('/api/v1.0/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client:
        return jsonify({
            'id': client.id,
            'FIO': client.FIO,
            'email': client.email,
            })
    else:
        abort(404)

@lab2.route('/api/v1.0/clients', methods=['POST'])
def create_client():
    if not request.json or not 'FIO' in request.json or not 'email' in request.json:
        return jsonify({'error': "Required json with 'FIO' and 'email' fields"})
    client = Client(FIO = request.json['FIO'], email = request.json['email'])
    db.session.add(client)
    try:
        db.session.flush()
        db.session.commit()
    except:
        if sys.exc_info()[1].orig.pgerror:
            return jsonify({'error': sys.exc_info()[1].orig.pgerror})
        else:
            return jsonify({'error': "Error during sql execution"})
    return jsonify({'client_id': client.id})

@lab2.route('/api/v1.0/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    if not request.json or not 'FIO' in request.json or not 'email' in request.json:
        return jsonify({'eroor': "Required json with 'FIO' and 'email' fields"})
    client = Client.query.get(client_id)
    if client:
        client.FIO = request.json['FIO']
        client.email = request.json['email']
        db.session.add(client)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({
                'id': client.id,
                'FIO': client.FIO,
                'email': client.email,
            })
        except:
            if sys.exc_info()[1].orig.pgerror:
                return jsonify({'error': sys.exc_info()[1].orig.pgerror})
            else:
                return jsonify({'error': "Error during sql execution"})
    else: 
        abort(404)

@lab2.route('/api/v1.0/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    try:
        Client.query.filter_by(id=client_id).delete()
        db.session.commit()
    except:
        if sys.exc_info()[1].orig.pgerror:
            return jsonify({'error': sys.exc_info()[1].orig.pgerror})
        else:
            return jsonify({'error': "Error during sql execution"})
    return jsonify({'result': True})
#endregion

#region Services CRUD
@lab2.route('/api/v1.0/services', methods=['GET'])
@auth.login_required
def get_services():
    services = Service.query.all()
    services_json = [{'id':c.id, 'name':c.name, 'price':c.price} for c in services]
    return jsonify({'services': services_json})

@lab2.route('/api/v1.0/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get(service_id)
    if service:
        return jsonify({
            'id': service.id,
            'name': service.name,
            'price': service.price,
            })
    else:
        abort(404)

@lab2.route('/api/v1.0/services', methods=['POST'])
def create_service():
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        return jsonify({'error': "Required json with 'name' and 'price' fields"})
    service = Service(name = request.json['name'], price = request.json['price'])
    db.session.add(service)
    try:
        db.session.flush()
        db.session.commit()
    except:
        if sys.exc_info()[1].orig.pgerror:
            return jsonify({'error': sys.exc_info()[1].orig.pgerror})
        else:
            return jsonify({'error': "Error during sql execution"})
    return jsonify({'service_id': service.id})

@lab2.route('/api/v1.0/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    if not request.json or not 'name' in request.json or not 'price' in request.json:
        return jsonify({'eroor': "Required json with 'name' and 'price' fields"})
    service = Service.query.get(service_id)
    if service:
        service.name = request.json['name']
        service.price = request.json['price']
        db.session.add(service)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({
                'id': service.id,
                'name': service.name,
                'price': service.price,
            })
        except:
            if sys.exc_info()[1].orig.pgerror:
                return jsonify({'error': sys.exc_info()[1].orig.pgerror})
            else:
                return jsonify({'error': "Error during sql execution"})
    else: 
        abort(404)

@lab2.route('/api/v1.0/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        Service.query.filter_by(id=service_id).delete()
        db.session.commit()
    except:
        if sys.exc_info()[1].orig.pgerror:
            return jsonify({'error': sys.exc_info()[1].orig.pgerror})
        else:
            return jsonify({'error': "Error during sql execution"})
#endregion

#region Requests CRUD
@lab2.route('/api/v1.0/requests', methods=['GET'])
@auth.login_required
def get_requests():
    requests = Request.query.all()
    requests_json = [{'id':c.id, 'client_id':c.client_id, 'service_id':c.service_id, 'date':c.date} for c in requests]
    return jsonify({'requests': requests_json})

@lab2.route('/api/v1.0/requests/<int:request_id>', methods=['GET'])
def get_request(request_id):
    my_request = Request.query.get(request_id)
    if my_request:
        return jsonify({
            'id': my_request.id,
            'client_id': my_request.client_id,
            'service_id': my_request.service_id,
            'date': my_request.date,
            })
    else:
        abort(404)

@lab2.route('/api/v1.0/requests', methods=['POST'])
def create_request():
    if not request.json or not 'client_id' in request.json or not 'service_id' in request.json:
        return jsonify({'error': "Required json with 'client_id' and 'service_id' and 'date' fields"})
    c = Client.query.get(request.json['client_id'])
    s = Service.query.get(request.json['service_id'])
    my_request = Request(client = c, service = s)
    db.session.add(my_request)
    try:
        db.session.flush()
        db.session.commit()
    except:
        if sys.exc_info()[1].orig.pgerror:
            return jsonify({'error': sys.exc_info()[1].orig.pgerror})
        else:
            return jsonify({'error': "Error during sql execution"})
    return jsonify({'request_id': my_request.id})

@lab2.route('/api/v1.0/requests/<int:request_id>', methods=['PUT'])
def update_request(request_id):
    if not request.json or not 'client_id' in request.json or not 'service_id' in request.json or not 'date' in request.json:
        return jsonify({'eroor': "Required json with 'client_id' and 'service_id' fields"})
    my_request = Request.query.get(request_id)
    if my_request:
        c = Client.query.get(request.json['client_id'])
        s = Service.query.get(request.json['service_id'])
        if c == None or s == None:
            return jsonify({'error': "Foreign key constraint"})
        my_request.client_id = c.id
        my_request.service_id = s.id
        my_request.date = request.json['date']
        db.session.add(my_request)
        try:
            db.session.flush()
            db.session.commit()
            return jsonify({
                'id': my_request.id,
                'client_id': my_request.client_id,
                'service_id': my_request.service_id,
                'date': my_request.date,
            })
        except:
            if sys.exc_info()[1].orig.pgerror:
                return jsonify({'error': sys.exc_info()[1].orig.pgerror})
            else:
                return jsonify({'error': "Error during sql execution"})
    else: 
        abort(404)

@lab2.route('/api/v1.0/requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    Request.query.filter_by(id=request_id).delete()
    db.session.commit()
    return jsonify({'result': True})
#endregion