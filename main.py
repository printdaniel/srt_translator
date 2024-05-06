"""
Script para traducir automáticamente subnombre_subtitulos en caso de que no se consiga
una versión en el idioa que se desea.
Para ello se aprovecha la google trasnlate. Una vez traducido se deberá hacer
una traducción propia dada la literalidad de la librería de Google, que se
presta a interpretaciónes erróneas.
"""
import os
from assets.banner import banner
from assets.lenguages import LANGUAGES
import pysrt
from googletrans import Translator


def scan_dir():
    contenido = os.listdir(os.getcwd())
    global nombre_subtitulo
    for elemento in contenido:
        if elemento.endswith(".srt"):
            nombre_subtitulo = elemento
            return nombre_subtitulo
    return None

def read_file():
    scan_dir()
    global subs_originales

    subs = pysrt.open(nombre_subtitulo, encoding='latin-1')
    subs_originales = subs

def translate_sub():
    translator = Translator()
    subs_nuevos = pysrt.SubRipFile()

    for subtitulo in subs_originales:
        try:
            texto_traducido = translator.translate(subtitulo.text, dest="es").text
            subs_nuevos.append(pysrt.SubRipItem(start=subtitulo.start, end=subtitulo.end, text=texto_traducido))
        except Exception as e:
            print(f"Error al traducir subtítulo: {e}")

    subs_nuevos.save("subtitulo_traducido.srt")
    print("Traducción completada. Se ha guardado el archivo 'subtitulo_traducido.srt'.")

def menu():
    print(f"""
          {banner}
    opciones:

    1) - Scanear directorios en busca de archivos .srt
    """)


# Ejemplo de uso
if __name__ == '__main__':
    menu()
    read_file()
