"""
Script para traducir automáticamente subtitulos en caso de que no se consiga
una versión en el idioa que se desea.
Para ello se aprovecha la google trasnlate. Una vez traducido se deberá hacer
una traducción propia dada la literalidad de la librería de Google, que se
presta a interpretaciónes erróneas.
"""
import os

banner = """
 _____      _     _                       _       _
/  ___|    | |   | |                     | |     | |
\ `--. _ __| |_  | |_ _ __ __ _ _ __  ___| | __ _| |_ ___  _ __
 `--. \ '__| __| | __| '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
/\__/ / |  | |_  | |_| | | (_| | | | \__ \ | (_| | || (_) | |
\____/|_|   \__|  \__|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|

"""



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
