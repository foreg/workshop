from .lab6api import db
from datetime import datetime

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

    questions = db.relationship('Question', backref='test', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data

    def from_dict(self, data):
        for field in ['name']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Test {}>'.format(self.name) 

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    answers = db.relationship('Answer', backref='question', lazy='dynamic')

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
        }
        return data

    def from_dict(self, data):
        for field in ['name']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Question {}>'.format(self.name) 

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    isCorrect = db.Column(db.Boolean, default=False)

    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'isCorrect': self.isCorrect,
        }
        return data

    def from_dict(self, data):
        for field in ['name', 'isCorrect']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self):
        return '<Answer {}>'.format(self.name)