"""
Script para traducir automáticamente subnombre_subtitulos en caso de que no se consiga
una versión en el idioa que se desea.
Para ello se aprovecha la google trasnlate. Una vez traducido se deberá hacer
una traducción propia dada la literalidad de la librería de Google, que se
presta a interpretaciónes erróneas.
"""
import os
from banner import banner
import pysrt


def menu():
    print(f"""
          {banner}
    opciones:

    1) - Scanear directorios en busca de archivos .srt
    """)

def scan_dir():
    directorio_actual = os.getcwd()
    contenido = os.listdir(directorio_actual)
    global nombre_subtitulo
    for elemento in contenido:
        if elemento.endswith(".srt"):
            print(elemento)
            nombre_subtitulo = elemento

def read_file():
    subs = pysrt.open(nombre_subtitulo)
    subtitulo = subs[2]
    print(subtitulo)




if __name__ == '__main__':
    menu()
    scan_dir()
    read_file()
