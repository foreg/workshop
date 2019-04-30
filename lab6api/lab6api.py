from flask import Blueprint, jsonify, request, render_template, redirect, url_for, abort
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth import auth
from app import app
import requests

lab6api = Blueprint('lab6/api', __name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .models import Test, Question, Answer

#region Test
@lab6api.route('/v1.0/tests', methods=['GET'])
@auth.login_required
def get_tests():
    tests = Test.query.all()
    tests_json = [t.to_dict() for t in tests]
    return jsonify({'tests': tests_json}), 200

@lab6api.route('/v1.0/tests/<int:test_id>', methods=['GET'])
def get_test(test_id):
    test = Test.query.get(test_id)
    if test:
        return jsonify(test.to_dict()), 200
    else:
        abort(404)

@lab6api.route('/v1.0/tests', methods=['POST'])
def create_test():
    if not request.json:
        return jsonify({'error': "Required json"}), 400
    data = request.get_json() or {}
    test = Test()
    test.from_dict(data)
    db.session.add(test)
    db.session.commit()
    return jsonify({'test_id': test.id}), 201
#endregion

#region Question
@lab6api.route('/v1.0/tests/<int:test_id>/questions', methods=['GET'])
@auth.login_required
def get_questions(test_id):
    questions = Question.query.filter_by(test_id=test_id).all()
    questions_json = [t.to_dict() for t in questions]
    return jsonify({'questions': questions_json}), 200

@lab6api.route('/v1.0/tests/<int:test_id>/questions/<int:question_id>', methods=['GET'])
def get_question(test_id, question_id):
    question = Question.query.filter_by(id=question_id, test_id=test_id).first()
    if question:
        return jsonify(question.to_dict()), 200
    else:
        abort(404)

@lab6api.route('/v1.0/tests/<int:test_id>/questions', methods=['POST'])
def create_question(test_id):
    if not request.json:
        return jsonify({'error': "Required json"}), 400
    data = request.get_json() or {}
    question = Question()
    question.from_dict(data)
    question.test_id = test_id
    db.session.add(question)
    db.session.commit()
    return jsonify({'question_id': question.id}), 201
#endregion

#region Answer
@lab6api.route('/v1.0/tests/<int:test_id>/questions/<int:question_id>/answers', methods=['GET'])
@auth.login_required
def get_answers(test_id, question_id):
    answers = Answer.query.filter_by(question_id=question_id).all()
    answers_json = [t.to_dict() for t in answers]
    return jsonify({'answers': answers_json}), 200

@lab6api.route('/v1.0/tests/<int:test_id>/questions/<int:question_id>/answers/<int:answer_id>', methods=['GET'])
def get_answer(test_id, question_id, answer_id):
    answer = Answer.query.filter_by(id=answer_id, question_id=question_id).first()
    if answer:
        return jsonify(answer.to_dict()), 200
    else:
        abort(404)

@lab6api.route('/v1.0/tests/<int:test_id>/questions/<int:question_id>/answers', methods=['POST'])
def create_answer(test_id, question_id):
    if not request.json:
        return jsonify({'error': "Required json"}), 400
    data = request.get_json() or {}
    answer = Answer()
    answer.from_dict(data)
    answer.question_id = question_id
    db.session.add(answer)
    db.session.commit()
    return jsonify({'answer_id': answer.id}), 201
#endregion