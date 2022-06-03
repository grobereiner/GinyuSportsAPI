from bs4 import BeautifulSoup
import requests

def Scrap(params):
    enlace = "https://www.soccerstats.com/results.asp?league="
    mes = "&pmtype=month3"

    # RETRIEVAL OF HTML USING REQUESTS
    html_text = requests.get(enlace+params+mes).text

    # SCRAP OBJECT CREATION
    tabla = BeautifulSoup(html_text, 'lxml')

    # OBTAINS LIST OF HTML STRUCTURE OF MATCHES
    partidos = tabla.find('table', {'id': "btable"}).find_all('tr', class_="odd")

    # STRINGIFY RESULTS
    result = ""
    for partido in partidos:
        attr = partido.find_all("td")[:4]
        for a in attr:
            result += str(a.text[:-1]) + ' '
        result += '\n'
    return result