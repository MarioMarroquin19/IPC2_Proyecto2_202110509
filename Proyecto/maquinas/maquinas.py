import os
from tkinter import messagebox
from maquinas.pines import listaDoblePines
import random
from colour import Color
from graphviz import Digraph, Source
from constante import style
import tkinter as tk
from tkinter import *

nuevoPin = listaDoblePines()

class Maquina:
    def __init__(self, nombre, numeroPines, numeroElementos): #, pines
        self.nombre = nombre
        self.numeroPines = numeroPines
        self.numeroElementos = numeroElementos
        #self.pines = pines

class nodoMaquina:
    def __init__(self, maquina, siguiente = None, anterior = None):
        self.maquina = maquina
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleMaquina:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, maquina):
        nuevo_nodo = nodoMaquina(maquina = maquina)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
    
    def recorrer(self, nuevoPin, nombreElementos):
        sintaxisAntes = ""
        sintaxis = ""
        sintaxisFinal = ""
        sintaxisAntes += "digraph {"
        sintaxisAntes += "tbl ["
        sintaxisAntes += "shape=plaintext label=<"
        sintaxisAntes += "<table border=\'0\' cellborder=\'1\' color=\'black\' cellspacing=\'0\'>"
        if self.primero is None:
            return messagebox.showerror("Error", "No hay ninguna máquina registrada")
        actual = self.primero
        while actual:
            sintaxis += f'<tr><td colspan="2" align="center" bgcolor="yellow">{actual.maquina.nombre}</td></tr>'
            sintaxis += "<tr><td>PIN</td><td>Elementos</td></tr>"
            for i in range(1,actual.maquina.numeroPines+1):
                sintaxis += nuevoPin.recorrer(i, actual.maquina.nombre, nombreElementos)
            actual = actual.siguiente
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
        directorio = os.getcwd()
        with open(directorio+"\\maquinas\\grafica_graphviz\\Maquina_grafica.dot", "r") as archivo:
            contenido = archivo.read()
        # Renderizar archivo .dot a .svg
        grafo = Source(contenido, format="svg")
        grafo.render("maquinas/grafica_graphviz/maquina_grafica", format="svg", cleanup=True)
        messagebox.showinfo("Informacion", "Se ha generado la gráfica correctamente")

    def verImg(self):
        try:
            directorio = os.getcwd()
            os.startfile(directorio+"\\maquinas\\grafica_graphviz\\Maquina_grafica.png")
        except:
            messagebox.showerror("Error", "Aún no se ha generado alguna gráfica")
    
    def verSVG(self):
        try:
            directorio = os.getcwd()
            os.startfile(directorio+"\\maquinas\\grafica_graphviz\\maquina_grafica.svg")
        except:
            messagebox.showerror("Error", "Aún no se ha generado alguna gráfica")

    def vaciar(self):
        try:
            self.primero = None
            self.ultimo = None
            #borramos la imagen
            directorio = os.getcwd()
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\Maquina_grafica.png")
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\Maquina_grafica.dot")
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\maquina_grafica.svg")
        except:
            self.primero = None
            self.ultimo = None

    def codigo_colorPin(self):
        color = Color(rgb=(random.random(), random.random(), random.random()))
        color_name = color.get_hex_l()
        return str(color_name)       

    def devolverMaquinas(self, nombreMaquina):
        actual = self.primero
        while actual:
            if actual.maquina.nombre == nombreMaquina:
                return actual.maquina.numeroPines
            actual = actual.siguiente
                
    def devolverNombreMaquina(self):
        actual = self.primero
        while actual:
            yield actual.maquina.nombre
            actual = actual.siguiente      