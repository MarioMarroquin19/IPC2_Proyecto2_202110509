import os
from tkinter import messagebox
from graphviz import Source
import tkinter as tk
from tkinter import *
from constante import style
from maquinas.TiempoMaquina import TiempoMaquina,listaDobleTiempoMaquina, listaDobleTiempoMaquina1
import xml.etree.ElementTree as ET
from lxml import etree

tiempoMaquina = listaDobleTiempoMaquina()
tiempoMaquina1 = listaDobleTiempoMaquina1()

class Pines:
    def __init__(self, numero,simboloElemento, nombreMaquina, colorPin):
        self.numero = numero
        self.simboloElemento = simboloElemento
        self.nombreMaquina = nombreMaquina
        self.colorPin = colorPin
    
class nodoPines:
    def __init__(self, pines, siguiente = None, anterior = None):
        self.pines = pines
        self.siguiente = siguiente
        self.anterior = anterior
    
class nodoPines1:
    def __init__(self, pines, siguiente = None, anterior = None):
        self.pines = pines
        self.siguiente = siguiente
        self.anterior = anterior    

class listaDoblePines:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.primero1 = None
        self.ultimo1 = None

    def insertar(self, pines):
        nuevo_nodo = nodoPines(pines = pines)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.insertar1(pines)

    #para que no se modifiquen los nodos al hacer la grafica con graphviz
    def insertar1(self, pines):
        nuevo_nodo = nodoPines1(pines = pines)
        if self.primero1 is None:
            self.primero1 = nuevo_nodo
            self.ultimo1 = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo1
            self.ultimo1.siguiente = nuevo_nodo
            self.ultimo1 = nuevo_nodo
    
    #recorrer por medio del numero de pin
    def recorrer(self, numero_pin, nombreMaquina, nombreElemento):
        sintaxis = ""
        sintaxis += "<tr>\n"
        sintaxis += f"<td>Pin:{numero_pin}</td>\n"
        sintaxis += "<td colspan=\'1\' rowspan=\'1\'>"
        sintaxis += "<table border=\'0\' cellborder=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
        sintaxis += "<tr>\n"
        actual = self.primero1
        while actual:    
            if actual.pines.numero == numero_pin and actual.pines.nombreMaquina == nombreMaquina: 
                sintaxis += "<td><table border=\'0\'  cellborder=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
                sintaxis += f"<tr><td align=\'left\' bgcolor=\"{actual.pines.colorPin}\" color=\"{actual.pines.colorPin}\" >{nombreElemento.retornarNumeroAtomicoSimbolo(actual.pines.simboloElemento)}</td></tr>\n"
                sintaxis += f"<tr><td align=\'center\' bgcolor=\"{actual.pines.colorPin}\" color=\"{actual.pines.colorPin}\" >{actual.pines.simboloElemento}</td></tr>\n"
                sintaxis += f"<tr><td align=\'center\' bgcolor=\"{actual.pines.colorPin}\" color=\"{actual.pines.colorPin}\" >{nombreElemento.retornarNombreElementoSimbolo(actual.pines.simboloElemento)}</td></tr>\n"
                sintaxis += "</table>\n"
                sintaxis += "</td>\n"
            actual = actual.siguiente
        sintaxis += "</tr>\n"
        sintaxis += "</table>\n"
        sintaxis += "</td>\n"
        sintaxis += "</tr>\n"
        return sintaxis
            
    #funcion para verificar en que pin esta el elemento
    def existe(self, nombreCompuesto, eleCompuesto, maquina):
        # for maquina in maquinas.devolverMaquinas():
        #     tiempo = 1
            for i in range(1,maquina+1):
                for elemento in eleCompuesto.devolverElementos(nombreCompuesto):
                    actual = self.primero
                    columna = 0
                    while actual:
                        if actual.pines.numero == i and actual.pines.simboloElemento != elemento:
                            columna += 1 
                        if actual.pines.numero == i and actual.pines.simboloElemento == elemento:
                            #mensaje = (f'FUSIÓN EN: \nEstá en el pin:{i}, el elemento es:{elemento}, su columna:{columna}')
                            #print(mensaje)
                            yield i, elemento, columna
                        actual = actual.siguiente
    
    def crearTabla(self, nombreCompuesto, eleCompuesto, maquinas):
        for maq in maquinas.devolverNombreMaquina():
            tiempo1 = 0
            #for maquina in maquinas.devolverMaquinas():
            for num, elemento, columna in self.existe(nombreCompuesto, eleCompuesto, maquinas.devolverMaquinas(maq)):
                for c in range(columna):
                    tiempo1 += 1
                tiempo1 += 1
            tiempoMa = TiempoMaquina(maq, tiempo1)
            tiempoMaquina.insertar(tiempoMa)

        sintaxis = ""
        sintaxisFinal = ""
        sintaxisAntes = ""
        sintaxisAntes += "digraph {tbl [shape=plaintext label=<<table border=\'0\' cellborder=\'1\' color=\'black\' cellspacing=\'0\'>"
        for maq in maquinas.devolverNombreMaquina():
            tiempo = 0
            #for maquina in maquinas.devolverMaquinas():
            sintaxis +=f"<tr><td colspan=\"1000\" align=\"center\" bgcolor=\"yellow\">Instrucciones para construir el compuesto: {nombreCompuesto}, MAQUINA: {maq}, TIEMPO: {tiempoMaquina.devolverTiempo(maq)} segundos</td></tr>"
            for num, elemento, columna in self.existe(nombreCompuesto, eleCompuesto, maquinas.devolverMaquinas(maq)):
                sintaxis += "<tr>\n"
                sintaxis += f"<td>Pin:{num}</td>\n"
                for c in range(columna):
                    sintaxis += "<td>Mover adelante</td>\n"
                    tiempo += 1
                sintaxis += f"<td bgcolor=\'red\'>FUSIONAR {elemento}</td>\n"
                tiempo += 1
                sintaxis += "</tr>\n"
            sintaxisFinal += "</table>>];}"
        cadena1=os.path.dirname(os.path.abspath(__file__))
        ruta=cadena1
        ruta+="\\grafica_graphviz\\Instrucciones_"
        ruta+="grafica"
        ruta+=".dot"
        imagen=cadena1
        imagen+="\\grafica_graphviz\\Instrucciones_"
        imagen+="grafica"
        imagen+=".png"
        nodo=cadena1
        nodo+="\\grafica_graphviz\\Instrucciones_"
        nodo+="grafica"
        nodo+=".dot"
        nodo_final="dot -Tpng "+nodo+" -o "+imagen
        file = open(ruta, "w+")
        file.write(sintaxisAntes+sintaxis+sintaxisFinal)
        file.close()
        os.system(nodo_final)
        directorio = os.getcwd()
        with open(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.dot", "r") as archivo:
            contenido = archivo.read()
        # Renderizar archivo .dot a .svg
        grafo = Source(contenido, format="svg")
        grafo.render("maquinas/grafica_graphviz/Instrucciones_grafica", format="svg", cleanup=True)
        messagebox.showinfo("Informacion", "Se ha generado la gráfica correctamente")
                 
    #funcionamiento de la maquina
    def funcionamiento(self, ventana,maquinas):
        #listar maquinas
        self.ver = Text(ventana, width=50, height=10, **style.STYLE)
        self.ver.tag_config("orange", foreground="orange")
        self.ver.tag_config("white", foreground="white")
        for maquina in maquinas.devolverNombreMaquina():
            self.ver.insert("end", "\n--MAQUINA-- \n", "orange")
            self.ver.insert("end", "    "+maquina+"\n", "white")
            self.ver.insert("end", "\n-Tiempo necesario para producir el compuesto: \n", "orange")
            self.ver.insert('end', f"Tiempo (segundos): {tiempoMaquina.devolverTiempo(maquina)}\n", "white")
        self.ver.configure(state="disabled")
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
    
    def verMaquinas(self):
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)  
    
    def todos(self, nomCompuesto,eleCompuesto ,maquina):
            for i in range(1,maquina+1):
                for elemento in eleCompuesto.devolverElementos(nomCompuesto):
                    actual = self.primero
                    columna = 0
                    while actual:
                        if actual.pines.numero == i and actual.pines.simboloElemento != elemento:
                            columna += 1 
                        if actual.pines.numero == i and actual.pines.simboloElemento == elemento:
                            #mensaje = (f'FUSIÓN EN: \nEstá en el pin:{i}, el elemento es:{elemento}, su columna:{columna}')
                            #print(mensaje)
                            yield i, elemento, columna
                        actual = actual.siguiente

    def generarXmlSalida(self,Compuesto, eleCompuesto, maquinas):
        #self.crearTablaTODOS(eleCompuesto, maquinas)
        for nombreCompuesto in Compuesto.devolverCompuestos():
            for maq in maquinas.devolverNombreMaquina():
                tiempo1 = 0
                #for maquina in maquinas.devolverMaquinas():
                for num, elemento, columna in self.todos(nombreCompuesto,eleCompuesto ,maquinas.devolverMaquinas(maq)):
                    for c in range(columna):
                        tiempo1 += 1
                    tiempo1 += 1
                tiempoMa = TiempoMaquina(maq, tiempo1)
                tiempoMaquina1.insertar(tiempoMa)
        root = ET.Element('RESPUESTA')
        hijo = ET.SubElement(root, 'listaCompuestos')
        hijo1 = ET.SubElement(hijo, 'compuesto')
        hijo3 = ET.SubElement(hijo1, 'nombre')
        for nombre in Compuesto.devolverCompuestos():
            hijo3.text = nombre
            for maq in maquinas.devolverNombreMaquina():
                hijo4 = ET.SubElement(hijo1, 'maquina')
                hijo4.text = maq
                hijo5 = ET.SubElement(hijo1, 'tiempoOptimo')
                hijo5.text = str(tiempoMaquina1.devolverTiempo(maq))
                hijo6 = ET.SubElement(hijo1, 'instrucciones')
                hijo7 = ET.SubElement(hijo6, 'tiempo')
                hijo8 = ET.SubElement(hijo7, 'numeroSegundos')
                hijo8.text = str(tiempoMaquina1.devolverTiempo(maq))
                hijo9 = ET.SubElement(hijo7, 'acciones')
                hijo10 = ET.SubElement(hijo9, 'accionPin')
                #for maquina in maquinas.devolverMaquinas():
                for num, elemento, columna in self.todos(nombre,eleCompuesto ,maquinas.devolverMaquinas(maq)):
                    hijo11 = ET.SubElement(hijo10, 'numeroPin')
                    hijo11.text = str(num)
                    for c in range(columna+1):
                        hijo12 = ET.SubElement(hijo10, 'accion')
                        hijo12.text = "Mover adelante"
                    hijo12.text = f"Fusionar {elemento}"

        tree = ET.ElementTree(root)
        root_elem = tree.getroot()
        xmlstr = ET.tostring(root_elem, encoding='unicode')
        lxml_root = etree.fromstring(xmlstr)
        directorio = os.getcwd()
        with open(directorio+"/Salida.xml", "wb") as f:
            f.write(etree.tostring(lxml_root, xml_declaration=True, pretty_print=True))
        messagebox.showinfo("Informacion", "Se ha generado el archivo de salida correctamente")

    def verImg(self):
        try:
            directorio = os.getcwd()
            os.startfile(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.png")
        except:
            messagebox.showerror("Error", "Aún no se ha generado alguna gráfica")
    
    def verSVG(self):
        try:
            directorio = os.getcwd()
            os.startfile(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.svg")
        except:
            messagebox.showerror("Error", "Aún no se ha generado alguna gráfica")

    def vaciar(self):
        try:
            self.primero = None
            self.ultimo = None
            self.primero1 = None
            self.ultimo1 = None
            tiempoMaquina.vaciar()
            tiempoMaquina1.vaciar()
            directorio = os.getcwd()
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.png")
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.dot")
            os.remove(directorio+"\\maquinas\\grafica_graphviz\\Instrucciones_grafica.svg")
        except:
            self.primero = None
            self.ultimo = None
            self.primero1 = None
            self.ultimo1 = None
            tiempoMaquina.vaciar()
            tiempoMaquina1.vaciar()         