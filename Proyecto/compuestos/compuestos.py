from tkinter import *
from tkinter import ttk
import tkinter as tk
from constante import style
from compuestos.EleCompuesto import Lista_EleCompuesto

elemento_Compuesto = Lista_EleCompuesto()

class Compuesto:
    def __init__(self, nombre):#, formula
        self.nombre = nombre
        #self.formula = formula

class nodoCompuesto:
    def __init__(self, compuesto, siguiente = None, anterior = None):
        self.compuesto = compuesto
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleCompuesto:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, compuesto):
        '''for elemento in compuesto.formula:
            elemento_Compuesto.insertar(elemento)'''
        nuevo_nodo = nodoCompuesto(compuesto = compuesto)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
     
    def verCompuesto_Formulas(self, ventana, elemento_Compuesto):
        self.ver = Text(ventana, width=50, height=10, **style.STYLE)
        self.ver.tag_config("orange", foreground="orange")
        self.ver.tag_config("white", foreground="white")
        actual = self.ultimo
        while actual:
            self.ver.insert("end", "\n--COMPUESTO-- \n", "orange")
            self.ver.insert("end",'    '+str(actual.compuesto.nombre)+'\n',"white")
            self.ver.insert("end",'\n-Formulas:\n', "orange")
            self.ver.insert("end",'    '+str(elemento_Compuesto.buscarElementos(str(actual.compuesto.nombre)))+'\n', "white")
            actual = actual.anterior
        self.ver.configure(state="disabled")
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)
        
    def verFormula_Compuestos(self):
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)

    def vaciar(self):
        self.primero = None
        self.ultimo = None

