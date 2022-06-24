from scrap import Scrap
import requests

dummy_db = "../server_SEARCH/file.txt"
success = "EXITOSO, ELEMENTOS SCRAPEADOS:\n"

def send_to_bmq(csv_format):
    requests.post(url="http://127.0.0.1:5009/recibir", data=csv_format)


def main(prompt):
    send_to_bmq(Scrap(prompt))
    return success