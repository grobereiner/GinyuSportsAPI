from flask import Flask

app = Flask(__name__)

dummy_db = "file.txt"

@app.route("/<query>")
def main(query):
    with open(dummy_db, "r") as f:
        lines = f.readlines()
        f.close()
        return str(lines)

app.run(port=5002)