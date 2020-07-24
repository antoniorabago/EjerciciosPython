import urllib.request, urllib.parse, urllib.error

#Se importa la librería de expresiones regulares
import re
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Introduce la dirección de la página web:')
datos = urllib.request.urlopen(url).read()

#Obtenemos los ficheros de video mp4 de la página
videos = re.findall(b'href="(http[s]?://.*?mp4)"', datos)
for video in videos:
    print(video.decode())

#Obtenemos todos los enlaces
#enlaces = re.findall(b'href="(http[s]?://.*?)"', datos)
#for enlace in enlaces:
#    print(enlace.decode())


#Obtenemos todos los enlaces usando BeautifulSoup
#from bs4 import BeautifulSoup
#soup =  BeautifulSoup(datos)

##Convertir a UTF-8
##if soup.original_encoding=='utf-8':
##    content=str(webpage.content, 'utf-8')
#if soup.original_encoding=='cp1252':
#    content=str(webpage.content, 'cp1252')
#    content.encode('utf-8','ignore')
#if soup.original_encoding=='windows-1252':
#    content=str(datos, 'windows-1252')
#    content.encode('utf-8','ignore')
#if soup.original_encoding=='ISO-8859-1':
#    content=str(webpage.content, 'ISO-8859-1')

#tags = soup('a')
#for tag in tags:    
#		print(tag.get('href'))





