from bs4 import BeautifulSoup
import requests

def Scrap(params):
    enlace_mes =  "https://www.soccerstats.com/results.asp?league=england&pmtype=month1" # TEMP URL FOR 2022 results
    enlace_anho = "https://www.soccerstats.com/results.asp?league=england_2021&pmtype=month12" # TEMP URL FOR 20xx results

    # enlace = "https://www.soccerstats.com/results.asp?league=england"
    enlace = "https://www.soccerstats.com/results.asp?league="

    # RETRIEVAL OF HTML USING REQUESTS
    html_text = requests.get(enlace+params).text

    # SCRAP OBJECT CREATION
    tabla = BeautifulSoup(html_text, 'lxml')

    # OBTAINS LIST OF HTML STRUCTURE OF MATCHES
    partidos = tabla.find('table', {'id': "btable"}).find_all('tr', class_="odd")

    # STRINGIFY RESULTS
    result = ""
    for partido in partidos:
        attr = partido.find_all("td")[:4]
        for a in attr:
            result += str(a.text) + ' '
        result += '\n'
    return result