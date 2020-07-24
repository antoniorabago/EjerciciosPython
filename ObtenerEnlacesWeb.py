###############################################
# Descarga de videos mp4 de una página web
###############################################

from bs4 import BeautifulSoup
# Python 3.x
import urllib.request, urllib.parse, urllib.error
import webbrowser

listavideos = []

url = input('Introduce la dirección de la página web:')
try:
    html = urllib.request.urlopen(url).read()
except:
    print('Se ha producido un error al leer la página')


soup = BeautifulSoup(html, "html.parser")

# Se seleccionan todos los enlaces de la página
for link in soup.select('a[href^="http://"]'):
       href = link.get('href')

       # Se seleccionan los enlaces con extensión mp4
       if not any(href.endswith(x) for x in ['.mp4']):
           continue

       listavideos.append(href)       
       
try:       
    for cadalinea in listavideos:       
        filename = cadalinea.rsplit('/', 1)[-1]
        print('Descargando el video...' + filename)
        webbrowser.open(cadalinea, new = 2)
        print("Descarga del video correcta.")
except:
    print('Se ha producido un error al descargar el video')

print('El proceso finalizado correctamente')

              

