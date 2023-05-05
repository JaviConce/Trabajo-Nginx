import os
import subprocess

# Diccionario de rutas de archivos y comandos a ejecutar
FILE_COMMAND_DICT = {
    'backend1.log': "notify-send 'backend 1' 'Cliente: {client} Petición: {request}'",
    'backend2.log': "notify-send 'backend 2' 'Cliente: {client} Petición: {request}'",
    'backend3.log': "notify-send 'backend 3' 'Cliente: {client} Petición: {request}'"
}

# Últimas fechas de modificación de los archivos
last_modified = {file: os.path.getmtime(file) for file in FILE_COMMAND_DICT}

while True:
    # Esperar hasta que se detecte un cambio en alguno de los archivos
    while all(os.path.getmtime(file) == last_modified[file] for file in FILE_COMMAND_DICT):
        pass

    # Obtener la ruta del archivo modificado y el comando a ejecutar
    file_modified = [file for file in FILE_COMMAND_DICT if os.path.getmtime(file) != last_modified[file]][0]
    command = FILE_COMMAND_DICT[file_modified]

    # Leer la última línea del archivo modificado
    with open(file_modified) as f:
        last_line = f.readlines()[-1].strip()

    # Obtener la información del cliente y la petición
    client = last_line.split()[0]
    request = last_line.split('"')[1]

    # Formatear el comando y ejecutarlo
    command_formatted = command.format(client=client, request=request)
    subprocess.run(['bash', '-c', command_formatted])

    # Guardar la fecha y hora de la última modificación
    last_modified[file_modified] = os.path.getmtime(file_modified)

