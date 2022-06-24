import difflib
import json

f = open("countries.json")
paises = json.load(f)
f.close()

query_resultados = lambda nat: "select team_one, team_two, resultado, fecha from resultados where pais = '"+nat+"';"

def procesar(query: str):
    palabras = query.split()
    similarity = ['', 0]
    for pais in paises:
        for p in palabras:
            ratio = difflib.SequenceMatcher(a=p, b=pais).ratio()
            if ratio>similarity[1]:
                similarity[0] = pais
                similarity[1] = ratio
    return similarity[0]

def resultados_formato(resultados):
    formato = ''
    for i in resultados:
        for j in i:
            formato += str(j)
            formato += '\t'
        formato+='\n'
    return formato
    

def main(query, cur):    
    proximo = procesar(query)
    resultados = None
    try:
        cur.execute(query_resultados(proximo))
        resultados = resultados_formato(cur.fetchall())
    except:
        return "No hay similitudes"
    return resultados
    