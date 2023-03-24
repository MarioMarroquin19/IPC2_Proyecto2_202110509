import os
from tkinter import messagebox
from maquinas.pines import listaDoblePines
import random
from colour import Color

nuevoPin = listaDoblePines()

class Maquina:
    def __init__(self, nombre, numeroPines, numeroElementos, pines):
        self.nombre = nombre
        self.numeroPines = numeroPines
        self.numeroElementos = numeroElementos
        self.pines = pines

class nodoMaquina:
    def __init__(self, maquina, siguiente = None, anterior = None):
        self.maquina = maquina
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleMaquina:
    def __init__(self):
        self.primero = None

    def insertar(self, maquina):
        for pin in maquina.pines:
            nuevoPin.insertar(pin)
        if self.primero is None:
            self.primero = nodoMaquina(maquina = maquina)
        else:
            actual = nodoMaquina(maquina = maquina, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual
    
    def recorrer(self):
        sintaxisAntes = ""
        sintaxis = ""
        sintaxisFinal = ""
        sintaxisAntes += "digraph {"
        sintaxisAntes += "tbl ["
        sintaxisAntes += "shape=plaintext label=<"
        sintaxisAntes += "<table border=\'0\' cellborder=\'1\' color=\'blue\' cellspacing=\'0\'>"
        if self.primero is None:
            return
        actual = self.primero
        sintaxis += "<tr><td colspan=\'2\' align=\'center\' bgcolor=\'yellow\'>"+actual.maquina.nombre+"</td></tr>"
        sintaxis += "<tr><td>PIN</td><td>Elementos</td></tr>"
        for i in range(1,actual.maquina.numeroPines+1):
            sintaxis += nuevoPin.recorrer(i, actual.maquina.nombre)
        while actual.siguiente:
            actual = actual.siguiente
            sintaxis += "<tr><td colspan=\'2\' align=\'center\' bgcolor=\'yellow\'>"+actual.maquina.nombre+"</td></tr>"
            sintaxis += "<tr><td>PIN</td><td>Elementos</td></tr>"
            for i in range(1,actual.maquina.numeroPines+1):
                sintaxis += nuevoPin.recorrer(i, actual.maquina.nombre)
        
        sintaxisFinal = "</table>>];\n"
        sintaxisFinal += "}"
        #Generar imagen y archivo dot
        cadena1=os.path.dirname(os.path.abspath(__file__))
        ruta=cadena1
        ruta+="\\grafica_graphviz\\Maquina_"
        ruta+="grafica"
        ruta+=".dot"
        imagen=cadena1
        imagen+="\\grafica_graphviz\\Maquina_"
        imagen+="grafica"
        imagen+=".png"
        nodo=cadena1
        nodo+="\\grafica_graphviz\\Maquina_"
        nodo+="grafica"
        nodo+=".dot"
        nodo_final="dot -Tpng "+nodo+" -o "+imagen
        file = open(ruta, "w+")
        file.write(sintaxisAntes+sintaxis+sintaxisFinal)
        file.close()
        os.system(nodo_final)
        messagebox.showinfo("Informacion", "Se ha generado la gráfica correctamente")

    def verImg(self):
        try:
            directorio = os.getcwd()
            os.startfile(directorio+"\\Proyecto\\maquinas\\grafica_graphviz\\Maquina_grafica.png")
        except:
            messagebox.showerror("Error", "Aún no se ha generado alguna gráfica")

    def vaciar(self):
        try:
            actual = self.primero
            while actual:
                siguiente = actual.siguiente
                del actual
                actual = siguiente
            self.primero = None
            nuevoPin.vaciar()
            directorio = os.getcwd()
            os.remove(directorio+"\\Proyecto\\maquinas\\grafica_graphviz\\Maquina_grafica.png")
        except:
            actual = self.primero
            while actual:
                siguiente = actual.siguiente
                del actual
                actual = siguiente
            self.primero = None
            nuevoPin.vaciar()


    def codigo_colorPin(self):
        color = Color(rgb=(random.random(), random.random(), random.random()))
        color_name = color.get_hex_l()
        return str(color_name)
