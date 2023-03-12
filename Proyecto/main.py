import xml.etree.ElementTree as ET


#lectura del XML
ruta = input('Ruta del archivo:')
root = ruta.replace('"', "")

def cargarArchivo(root):
    try:
        tree = open(root)
        if tree.readable():
            nueva_configuracion = ET.fromstring(tree.read())
            print('Archivo cargado correctamente')

            #leemos los elementos del XML
            for elemento in nueva_configuracion.findall('listaElementos/elemento'):
                numeroAtomico_elemento = elemento.find('numeroAtomico').text
                simbolo_elemento = elemento.find('simbolo').text
                nombre_elemento = elemento.find('nombreElemento').text

                print('Numero atomico:',numeroAtomico_elemento)
                print('Simbolo:',simbolo_elemento)
                print('Nombre:',nombre_elemento)

            #leemos las máquinas del XML
            for maquina in nueva_configuracion.findall('listaMaquinas/Maquina'):
                nombre_maquina = maquina.find('nombre').text
                numeroPines_maquina = maquina.find('numeroPines').text
                numeroElementos = maquina.find('numeroElementos').text

                for elementos in maquina.findall('pin/elementos'):
                    elemento_maquina = elementos.find('elemento').text

                print('------------------------------------------------')
                print('Nombre:',nombre_maquina)
                print('Numero de pines:',numeroPines_maquina)
                print('Numero de elementos:',numeroElementos)
                print('Elemento:',elemento_maquina)
            
            #leemos los compuestos del XML
            for compuesto in nueva_configuracion.findall('listaCompuestos/compuesto'):
                nombre_compuesto = compuesto.find('nombre').text

                for elementos_compuesto in compuesto.findall('elementos'):
                    elemento_compuesto = elementos_compuesto.find('elemento').text

                print('------------------------------------------------')
                print('Nombre:',nombre_compuesto)
                print('Elemento:',elemento_compuesto)
                print('------------------------------------------------')

             
    except Exception as e:
        print('Erro:',e)

if __name__ == '__main__':
    cargarArchivo(root)
