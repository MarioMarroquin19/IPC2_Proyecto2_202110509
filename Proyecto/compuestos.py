from tkinter import *
from tkinter import ttk
import tkinter as tk
from constante import style
from EleCompuesto import Lista_EleCompuesto

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
        if self.primero is None:
            return
        actual = self.primero
        self.ver.insert("1.0", "\n--COMPUESTO-- \n" +'    '+str(actual.compuesto.nombre) +'\n-FORMULAS-\n'+'    '+str(elemento_Compuesto.buscarElementos(str(actual.compuesto.nombre)))+'\n')
        while actual.siguiente:
            actual = actual.siguiente
            self.ver.insert("1.0", "\n--COMPUESTO-- \n"+'    '+str(actual.compuesto.nombre) +'\n-FORMULAS-\n'+'    '+str(elemento_Compuesto.buscarElementos(str(actual.compuesto.nombre)))+'\n')
        self.ver.configure(state="disabled")
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)

    def verFormula_Compuestos(self):
        self.ver.pack(side=tk.TOP,fill=tk.BOTH,expand=True,padx=22,pady=11)

        



    


