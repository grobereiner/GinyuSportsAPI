from scrap import Scrap

dummy_db = "../server_SEARCH/file.txt"
success = "EXITOSO, ELEMENTOS SCRAPEADOS:\n"

def main(prompt):
    global success
    result = success
    with open(dummy_db, "a") as f:
        f.write(Scrap(prompt))
        f.close()
    result += Scrap(prompt)
    return result