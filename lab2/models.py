from .lab2 import db
from datetime import datetime

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FIO = db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    requests = db.relationship('Request', backref='client', lazy='dynamic')
    def __repr__(self):
        return '<Client {}>'.format(self.FIO) 

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    requests = db.relationship('Request', backref='service', lazy='dynamic')
    def __repr__(self):
        return '<Service {}>'.format(self.name) 

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id', ondelete='RESTRICT'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id', ondelete='RESTRICT'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Request {}>'.format(self.id)