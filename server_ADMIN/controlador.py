dummy_db = "../server_SEARCH/file.txt"
success = "EXITOSO"

def main(prompt):
    with open(dummy_db, "a") as f:
        f.write('\n'+str(prompt))
        f.close()
    return success