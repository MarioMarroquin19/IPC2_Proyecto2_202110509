import xml.etree.ElementTree as ET


#lectura del XML
ruta = input('Ruta del archivo:')
root = ruta.replace('"', "")

def cargarArchivo(root):
    try:
        tree = open(root)
        if tree.readable():
            print('Archivo cargado correctamente')
    except Exception as e:
        print('Erro:',e)
