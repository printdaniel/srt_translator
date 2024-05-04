"""
Script para traducir automáticamente subnombre_subtitulos en caso de que no se consiga
una versión en el idioa que se desea.
Para ello se aprovecha la google trasnlate. Una vez traducido se deberá hacer
una traducción propia dada la literalidad de la librería de Google, que se
presta a interpretaciónes erróneas.
"""
import os
from re import sub
from banner import banner
import pysrt
from googletrans import Translator


def scan_dir():
    directorio_actual = os.getcwd()
    contenido = os.listdir(directorio_actual)
    global nombre_subtitulo
    for elemento in contenido:
        if elemento.endswith(".srt"):
            print(elemento)
            nombre_subtitulo = elemento

def read_file():
    scan_dir()
    global subs
    global subtitulo_original

    subs = pysrt.open(nombre_subtitulo)
    subtitulo_original = subs

def translate_sub( ):
    t = Translator()
    count = 0
    subs_nuevos = pysrt.open("Whiplash.srt")
    for linea in range(len(subtitulo_original)):
        linea_actual = subtitulo_original[linea].text

        try:
            subs_nuevos[linea].text = t.translate(linea_actual, dest='es')
            count += 1
            print(count)
        except:
            pass

    subs_nuevos.save("nuevo_subtitulo.srt")

def menu():
    print(f"""
          {banner}
    opciones:

    1) - Scanear directorios en busca de archivos .srt
    """)


if __name__ == '__main__':
    #menu()
    scan_dir()
    read_file()
    translate_sub()
