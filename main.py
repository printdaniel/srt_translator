"""
Este script permite la traducción automática de subtítulos en caso de no
disponerse de una versión en el idioma deseado. Para ello, se utiliza la
herramienta Google Translate. No obstante, debido a las limitaciones de esta
herramienta, que pueden generar traducciones imprecisas o ambiguas, se recomienda
realizar una revisión posterior del texto traducido para asegurar su correcta
interpretación.
"""
import os
from assets.banner import banner
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
    Opciones:

    1) - Scanear directorios en busca de archivos .srt
    2) - Ver si hay subtitulos en el directorio
    3) - Convertir  subtutulos
    4) - Salir
    """)

def main_control():
    menu()
    while True:
        opcion = input("Ingrese una opción del menú: ")
        if opcion == "1":
            scan_directory_for_subtitle()
        elif opcion == "2":
            print(scan_directory_for_subtitle())
        elif opcion == "3":
            translate_sub()
        elif opcion == "4":
            break
        else:
            print("Esa opción no está en el menú de opciones")

if __name__ == '__main__':
    main_control()
