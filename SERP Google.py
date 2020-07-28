from bs4 import BeautifulSoup
import requests
import json
import pandas


# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

#Parametros de la consulta
query = input('Introduzca el término a buscar:')
query = query.replace(' ', '+')
numero_resultados = input ('Introduzca el número de resultados que quiere recuperar:')
codigo_lenguaje = "es"

#Construimos la consulta
url_google = 'https://www.google.com/search?q={}&num={}&hl={}'.format(query, numero_resultados, codigo_lenguaje)
headers = {"user-agent": USER_AGENT}

#Realizamos la consulta a google
respuesta = requests.get(url_google, headers=headers)

#Si se recuperan los datos correctamente
if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.content, "html.parser")
    
    resultados = []

    #Extraemos la información y la añadimos en una lista de diccionarios
    for g in soup.find_all('div', class_='r'):
        enlace = g.find_all('a')     
        if enlace:
            titulo = g.find('h3').text
            link = enlace[0]['href']

            item = {
                "Pagina": titulo,
                "Enlace": link
            }
            
            resultados.append(item)              
   
    #Guardamos la información en un fichero CSV a través de un DataFrame
    data = pandas.DataFrame(resultados)
    data.to_csv (r'C:\Users\anrab\source\repos\PageRank\datos_busqueda.csv', index = False, header= True)


    #Guardamos la información en un fichero formato Json
    with open('datos_biblioteca.json', 'w', newline='') as write_obj:  #si esta en python 2 en python 3 use 'w'
        json.dump(resultados, write_obj)










