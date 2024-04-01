import os
import re
def buscar_secreto(ruta_directorio, patron):
    for root, _, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            if archivo.endswith('.js'):
                ruta_archivo = os.path.join(root, archivo)
                with open(ruta_archivo, 'r') as f:
                    lineas = f.readlines()
                    for linea_numero, linea in enumerate(lineas, start=1):
                        if re.search(patron, linea):
                            print(f'Secreto encontrado en {ruta_archivo}, línea {linea_numero}: {linea.strip()}')
ruta_repositorio = "C:/Users/LuuuJ/Documents/Challenge técnico/vulnerable-java-application/src/main/resources/static/js"
patron = r'apikey1234abcdefghij01234567890'
buscar_secreto(ruta_repositorio, patron)