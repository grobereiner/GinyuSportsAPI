from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from requests import request


app = Flask(__name__)


@app.route('/static/<path:path>')
def send_static(path):
	return send_from_directory('static', path)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
	SWAGGER_URL,
	API_URL,
	config={
		'app_name': 'Ginyu Sports API'
	}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


app.run(port=5005)
