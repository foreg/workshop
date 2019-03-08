from flask import Blueprint, jsonify, request
from auth import auth
from num2words import num2words
from .codes import get_codes
import datetime
import math



lab1 = Blueprint('lab1', __name__)

@lab1.route('/api/v1.0/inwords/<float:n>', methods=['GET'])
@lab1.route('/api/v1.0/inwords/<int:n>', methods=['GET'])
@auth.login_required
def numberInWords(n):
    words = num2words(n, lang='ru')
    return jsonify({'words': words})

@lab1.route('/api/v1.0/quadraticEquations/', methods=['GET'])
@auth.login_required
def solveQuadraticEquation():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = float(request.args.get('c'))
    except (ValueError, TypeError) as e:
        return jsonify({'success': False, 'error': 'Not all of parameters were numbers'})
    d = b**2-4*a*c
    if d < 0:
        return jsonify({
            'success': False,
            'error': "discriminant < 0"
            })
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return jsonify({
            'success': True,
            'results': [x]
            })
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        return jsonify({
            'success': True,
            'results': [x1,x2]
            })

@lab1.route('/api/v1.0/daysofweek/', methods=['GET'])
@auth.login_required
def dayOfWeek():
    try:        
        date = datetime.datetime.strptime(request.args.get('date'), '%d.%m.%Y')
    except ValueError:
        return jsonify({'success': False, 'error': 'Not valid date input. Please, use dd.mm.yyyy'})
    week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return jsonify({
        'success': True, 
        'dayOfWeek': week[date.weekday()]
        })

@lab1.route('/api/v1.0/fibs/<int:n>', methods=['GET'])
@auth.login_required
def fibs(n):
    nth_number = ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)//(2**n*math.sqrt(5))
    return jsonify({'number': nth_number})

@lab1.route('/api/v1.0/codes/<int:n>', methods=['GET'])
@auth.login_required
def codes(n):
    codes = get_codes()
    if codes.get(n):
        return jsonify({'name': codes[n]})
    else:
        return jsonify({'error': "No such region"})