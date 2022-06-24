dummy_db = "file.txt"

def main(query):    
    with open(dummy_db, "r") as f:
        lines = f.readlines()
        f.close()
        return str(lines)