##################################################################
# Descarga archivos de las extensiones indicadas de una página web
##################################################################

from bs4 import BeautifulSoup
# Python 3.x
import urllib.request, urllib.parse, urllib.error
import webbrowser

listaficheros = []

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
       #if not any(href.endswith(x) for x in ['.mp4']):
       #    continue
       
       if not "CDIMPRESO" in href:
            continue

       listaficheros.append(href)       
       
try:       
    for cadalinea in listaficheros:       
        filename = cadalinea.rsplit('/', 1)[-1]
        print('Descargando el fichero...' + filename)
        webbrowser.open(cadalinea, new = 2)
        print("Descarga del fichero correcta.")
except:
    print('Se ha producido un error al descargar el fichero')

print('El proceso finalizado correctamente')
             
