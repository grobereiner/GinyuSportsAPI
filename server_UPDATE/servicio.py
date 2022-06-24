import requests
import psycopg2
from time import sleep

bmq_addr = "http://127.0.0.1:5009/enviar"
# CAMBIAR PARA UN DIRECTORIO MEJOR
temp_file_path = "C:/Users/Public/Documents/TEMP/temp.csv"

queryUpdate = "COPY resultados(fecha, team_one, team_two, resultado) FROM '"
queryUpdate += temp_file_path
queryUpdate += "' DELIMITER ',' CSV HEADER;"

while True:
    conn = psycopg2.connect(
        host="localhost",
        database="ginyu",
        user="Grove",
        password="root")
    cur = conn.cursor()

    try:
        r = requests.get(url=bmq_addr)
    
        if len(r.text) == 0:
            print("No hay recibos en la cola")
        else:
            print(r.text)
            with open(temp_file_path, "w") as f:
                f.write(r.text)
                f.close()
            try:
                cur.execute(query=queryUpdate)
                conn.commit()
                pass
            except:
                print("Fallo en la subida")

    except:
        print("NO HAY CONEXION AL BMQ")
    
    cur.close()
    conn.close()
    sleep(5)
