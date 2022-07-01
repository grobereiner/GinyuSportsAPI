from http.client import HTTPException
from urllib.error import HTTPError
from flask import Flask, abort, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import requests


app = Flask(__name__)


@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)


@app.route("/admin/<prompt>")
def scrap(prompt):
	try:
		resp = requests.get(url="http://127.0.0.1:5001/"+prompt)
		return resp.text, 201
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route("/search/<query>")
def search(query):
	try:
		resp = requests.get(url="http://127.0.0.1:5002/"+query)
		return resp.text, 200
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route('/validation/login', methods=["POST"])
def login_post():
	try:
		resp = requests.get(url="http://127.0.0.1:5000/login")
		return resp.text, 201
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route('/validation/login', methosd=["GET"])
def login_get():
	try:
		resp = requests.get(url="http://127.0.0.1:5000/login")
		return resp.text, 200
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route("/validation/signup", methods=["POST"])
def signup_post():
	try:
		resp = requests.get(url="http://127.0.0.1:5000/signup")
		return resp.text, 201
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route("/validation/signup", methods=["GET"])
def signup_get():
	try:
		resp = requests.get(url="http://127.0.0.1:5000/signup")
		return resp.text, 200
	except requests.exceptions.ConnectionError:
		abort(405)


@app.route('/validation/signout')
def signout():
	try:
		resp = requests.get(url="http://127.0.0.1:5000/signout")
		return resp.text, 200
	except requests.exceptions.ConnectionError:
		abort(405)



SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
	SWAGGER_URL,
	API_URL,
	config={
		'app_name': 'Ginyu Sports API Documentation'
	}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


app.run(port=5010, debug=True)
