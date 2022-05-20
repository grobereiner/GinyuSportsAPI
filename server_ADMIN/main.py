from flask import Flask

app = Flask(__name__)

dummy_db = "../server_SEARCH/file.txt"
success = "EXITOSO"

@app.route("/<prompt>")
def main(prompt):
    with open(dummy_db, "a") as f:
        f.write('\n'+str(prompt))
        f.close()
    return success

app.run(port=5001)