from tkinter import *
from tkinter import ttk
import tkinter as tk
from constante import style
from compuestos.EleCompuesto import Lista_EleCompuesto

elemento_Compuesto = Lista_EleCompuesto()

class Compuesto:
    def __init__(self, nombre, formula):
        self.nombre = nombre
        self.formula = formula

class nodoCompuesto:
    def __init__(self, compuesto, siguiente = None, anterior = None):
        self.compuesto = compuesto
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleCompuesto:
    def __init__(self):
        self.primero = None
    
    def insertar(self, compuesto):
        for elemento in compuesto.formula:
            elemento_Compuesto.insertar(elemento)
        if self.primero is None:
            self.primero = nodoCompuesto(compuesto = compuesto)
        else:
            actual = nodoCompuesto(compuesto = compuesto, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual        
    
    def verCompuesto_Formulas(self, ventana):
        self.ver = Text(ventana, width=50, height=10, **style.STYLE)
        self.ver.tag_config("orange", foreground="orange")
        self.ver.tag_config("white", foreground="white")
        if self.primero is None:
            return
        actual = self.primero
        self.ver.insert("1.0", "\n--COMPUESTO-- \n", "orange")
        self.ver.insert("end",'    '+str(actual.compuesto.nombre)+'\n',"white")
        self.ver.insert("end",'\n-Formulas:\n', "orange")
        self.ver.insert("end",'    '+str(elemento_Compuesto.buscarElementos(str(actual.compuesto.nombre)))+'\n', "white")
        while actual.siguiente:
            actual = actual.siguiente
            self.ver.insert("end", "\n--COMPUESTO-- \n", "orange")
            self.ver.insert("end",'    '+str(actual.compuesto.nombre)+'\n',"white")
            self.ver.insert("end",'\n-Formulas:\n', "orange")
            self.ver.insert("end",'    '+str(elemento_Compuesto.buscarElementos(str(actual.compuesto.nombre)))+'\n', "white")
        self.ver.configure(state="disabled")
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)

    def verFormula_Compuestos(self):
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)


    def vaciar(self):
        actual = self.primero
        while actual:
            siguiente = actual.siguiente
            del actual
            actual = siguiente
        self.primero = None
        elemento_Compuesto.vaciar()
        
