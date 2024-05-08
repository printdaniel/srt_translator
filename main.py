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

def scan_directory_for_subtitle():
    """
    Escanea el directorio especificado en busca de archivos .srt y devuelve el
    nombre del primer archivo encontrado.

    Parameters:
    - directory: El directorio a escanear.

    Returns:
    - El nombre del archivo de subtítulo encontrado, o None si no se
    encontraron archivos de subtítulos.
    """
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".srt"):
            return filename
    return None

def read_file():
    filename = scan_directory_for_subtitle()

    if filename:
        subs = pysrt.open(filename, encoding='latin-1')
        subs_originales = subs
        return subs_originales
    else:
        print("No se encontró ningún archivo de subtitulo en el directorio")
        return None

def translate_sub():
    translator = Translator()
    subs_originales = read_file()
    subs_nuevos = pysrt.SubRipFile()

    if subs_originales:
        for subtitulo in subs_originales:
            try:
                texto_traducido = translator.translate(subtitulo.text, dest="es").text
                subs_nuevos.append(pysrt.SubRipItem(start=subtitulo.start, end=subtitulo.end, text=texto_traducido))
            except Exception as e:
                print(f"Error al traducir subtítulo: {e}")

        subs_nuevos.save("subtitulo_traducido.srt")
        print("Traducción completada. Se ha guardado el archivo 'subtitulo_traducido.srt'.")
    else:
        ("No se pudo cargar el archivo de subtitulos para la traducción")

def menu():
    print(f"""
          {banner}
    opciones:

    1) - Scanear directorios en busca de archivos .srt
    """)


if __name__ == '__main__':
    translate_sub()

