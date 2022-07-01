from flask import Flask
import controlador
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

conn = psycopg2.connect(
        host="localhost",
        database="ginyu",
        user="Grove",
        password=os.getenv("db_password"))
cur = conn.cursor()

@app.route("/<query>")
def main(query):
    print(query)
    return controlador.main(query, cur)

app.run(port=5002, debug=True)