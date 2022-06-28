import requests
import psycopg2
from time import sleep
import json

bmq_addr = "http://127.0.0.1:5003/enviar"
# CAMBIAR PARA UN DIRECTORIO MEJOR
temp_file_path = "C:/Users/Public/Documents/TEMP/temp.csv"

queryUpdate = "COPY resultados(fecha, team_one, team_two, resultado, pais) FROM '"
queryUpdate += temp_file_path
queryUpdate += "' DELIMITER ',' CSV HEADER;"

queryCountries = "select distinct pais from resultados;"

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
                # ACTUALIZAR DATOS
                cur.execute(query=queryUpdate)
                conn.commit()
                
                # ACTUALIZAR PAISES
                cur.execute(query=queryCountries)
                pais_filas = cur.fetchall()
                paises = [pais[0]  for pais in pais_filas]

                f = open("countries.json", "w")
                json.dump(paises, f)
                f.close()
            except:
                print("Fallo en la subida")

    except:
        print("NO HAY CONEXION AL BMQ")
    
    cur.close()
    conn.close()
    sleep(5)
