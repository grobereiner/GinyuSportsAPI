from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import requests


app = Flask(__name__)


@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)


@app.route("/<query>")
def search(query):
	return requests.get(url='http://127.0.0.1:5002/'+query).text


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


app.run(port=5005)
