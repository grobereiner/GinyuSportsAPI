from cgi import test
from flask import Flask

import sys
sys.path.append('../')

import Service.service as serv

app = Flask(__name__)

@app.route("/")
def home():
    return serv.test()


app.run()
