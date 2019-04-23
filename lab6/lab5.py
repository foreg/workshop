from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from auth import auth
import requests

lab6 = Blueprint('lab6', __name__)
base_url = "http://localhost:5000/lab6/api/v1.0/"
