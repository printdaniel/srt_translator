"""
Script para traducir automáticamente subtitulos en caso de que no se consiga
una versión en el idioa que se desea.
Para ello se aprovecha la google trasnlate. Una vez traducido se deberá hacer
una traducción propia dada la literalidad de la librería de Google, que se
presta a interpretaciónes erróneas.
"""
import os
from banner import banner



def menu():
    print(f"""
          {banner}
    opciones:

    1) - Scanear directorios en busca de archivos .srt
    """)

def scan_dir():
    directorio_actual = os.getcwd()
    contenido = os.listdir(directorio_actual)
    for elemento in contenido:
        if elemento.endswith(".srt"):
            print(elemento)


if __name__ == '__main__':
    menu()
    scan_dir()
