from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from auth import auth
import requests

lab6 = Blueprint('lab6', __name__)
base_url = "http://localhost:5000/lab6/api/v1.0/"

@lab6.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@lab6.route('/tests', methods=['GET'])
def tests():
    url = base_url + "tests"
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    r = requests.get(url=url, headers=headers)
    r = r.json()['tests']
    for test in r:
        q_url = url + '/' + str(test['id']) + '/questions'
        qr = requests.get(url=q_url, headers=headers)
        qr = qr.json()['questions']
        for question in qr:
            a_url = q_url + '/' + str(question['id']) + '/answers'
            ar = requests.get(url=a_url, headers=headers)
            ar = ar.json()['answers']
            question.update({
                'answers': ar
            })
        test.update({
            'questions': qr
        })
    return render_template('tests.html',tests = r)

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
def add_question(test_id):
    url = base_url + 'tests/' + str(test_id) + '/questions'
    headers = {'Authorization': "Basic ZG1pdHJ5OjEyMzQ="}
    if (request.form.get("save")):
        payload = {
            'name': request.form.get("name"), 
        }
        r = requests.post(url=url, json=payload, headers=headers)
        q_id = r.json()['question_id']
        answers_url = url + '/' + str(q_id) + '/answers'
        answers = request.form.getlist('answer[]')
        isCorrect = request.form.getlist('isCorrect[]')
        offset = 0
        for i in range(len(answers)-1):
            correct = False
            x = isCorrect[offset]
            y = isCorrect[offset + 1]
            if y == '1':
                correct = True
                offset += 2
            else:
                offset += 1
            payload = {
                'name': answers[i],
                'isCorrect': correct
            }
            r = requests.post(url=answers_url, json=payload, headers=headers)

        
    return redirect('lab6/tests/' + str(test_id) + '/questions/add')