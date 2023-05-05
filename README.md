# Comandos básicos

## Instalación:
- sudo apt update
- sudo apt install nginx


## Para reiniciar nginx después de modificar o añadir algún archivo:
- sudo service nginx restart
(Si da error es probable que sea por algún error de los archivos)

## Para ver el estado de nginx:
- sudo systemctl status nginx


## Resetear ngrinx sin interrupciones (sin parar el servicio ngrinx): 
- sudo nginx -s reload

# Para la Demo

## Archivos para logs (no es necesario para el funcionamiento)
- copiar contenido de la carpeta nginx en /var/log/nginx


## Archivos para servidores backend y frontend:
- copiar contenido de sites-enabled en /etc/nginx/sites-enabled


## Archivos html que se mostrarán en el navegador:
- copiar contenido de www en /var/www
- Cada backend tendrá un directorio, con un index.html dentro de cada uno.

## Archivos .sh:
Hay algunos archivos .sh en la carpeta de logs, es para mandar peticiones de distintas formas y mostrar a qué servidor backend ha ido cada una.


## Tutorial demo:
Simplemente buscar en el navegador localhost:80, y ver en cada búsqueda a qué backend nos ha mandado el balanceador de carga.


El modo de balanceo por defecto es round robin. Para cambiarlo, modificar en el frontend la función upstream, descomentando el método que se desea utilizar.

- En vez del navegador, puedes usar el sh enviar_x_peticiones.sh (num_peticiones) para enviar peticiones por terminal.
- Con mostrar_peticiones.sh se imprime el número de peticiones que ha recibido cada backend.
- Con limpiar_peticiones.sh reinicias el contador de peticiones de todos los backends.



## Puertos:
Frontend en el puerto 80. 3 backends en los 8081, 8082 y 8083.


## Archivos HTML: Para modificar los archivos html que muestra cada backend, modificar la parte

root /var/www/backend1;

    index index.html;
    
    
Indicando el directorio y el archivo, respectivamente.

También puedes cambiar los html existentes.

# Notificaciónes:
Junto a los logs, en la carpeta "nginx" se encuentra un script de python llamado listener_notify.py.

Durante su ejecución, aprovecha los archivos backend1.log, backend2.log y backend3.log. Estos archivos se usaban en la demo para ver cómo se habían balanceado las peticiones en cada búsqueda.

Consisten en que cada vez que llega una petición a un backend, este añade una línea a su respectivo log como la siguiente:


- 127.0.0.1 - - [04/May/2023:08:14:25 +0200] "GET / HTTP/1.0" 200 197 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"


Esto es la información de la petición. Lo más importante es el usuario que la ha realizado (127.0.0.1 en este caso), y la línea de solicitud ("GET / HTTP/1.0", donde GET es el método HTTP utilizado, / es el recurso que se solicita, en este caso es la página de inicio o raíz del sitio web, y HTTP/1.0 es la versión del protocolo).

El script de python consiste en esperar a que estos archivos se modifiquen, es decir, a que un backend haya recibido una petición. Cuando ocurra, leerá la nueva línea (la nueva petición), y obtendrá los datos necesarios de ella. Después, hará el respectivo notify-send.
