import socket
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect(('congreso.es', 80))
cmd = 'GET http://www.congreso.es/wc/wc/audiovisualdetalledisponible?codSesion=7&codOrgano=380&fechaSesion=23/07/2020&mp4=mp4&idLegislaturaElegida=14 HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(),end='')
misock.close()