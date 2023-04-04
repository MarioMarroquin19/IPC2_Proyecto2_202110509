from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

class Elemento:
    def __init__(self, numeroAtomico, simbolo, nombreElemento):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.nombreElemento = nombreElemento
    
class nodoElemento:
    def __init__(self, elemento, siguiente = None, anterior = None):
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior
        
class listaDobleElemento:
    def __init__(self):
        self.primero = None    
        self.ultimo = None  
        self.elementos_repetidos = 0 # contador de elementos repetidos
        self.mostrar_error = True # bandera para mostrar el mensaje de error una sola vez       
    
    def insertar(self, elemento):

        if not self.verificarElemento(elemento):
            self.elementos_repetidos += 1  # aumentar contador de elementos repetidos
            if self.mostrar_error:
                self.mostrar_error = False
                messagebox.showerror("Error", "Existen Elementos repetidos, verifique el XML de entrada y los elementos ingresados. SE HAN OMITIDO LOS ELEMENTOS REPETIDOS.")
            return
        nuevo_nodo = nodoElemento(elemento = elemento)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
    
    def retornarNombreElementoSimbolo(self, simboloElemento):
        if self.primero is None:
            return None
        actual = self.primero
        while actual is not None:
            if actual.elemento.simbolo == simboloElemento:
                return actual.elemento.nombreElemento
            actual = actual.siguiente
        return None

    def retornarNumeroAtomicoSimbolo(self, simboloElemento):
        if self.primero is None:
            return None
        actual = self.primero
        while actual is not None:
            if actual.elemento.simbolo == simboloElemento:
                return actual.elemento.numeroAtomico
            actual = actual.siguiente
        return None
        
        
    #verificar que no se repita elemento, numero atomico ni simbolo
    def verificarElemento(self, elemento):   
        if self.primero is None:
            return True
        actual = self.primero
        while actual is not None:
            if actual.elemento.nombreElemento == elemento.nombreElemento or actual.elemento.numeroAtomico == elemento.numeroAtomico or actual.elemento.simbolo == elemento.simbolo:
                return False
            actual = actual.siguiente
        return True

    #vaciamos la lista doblemente enlazada        
    def vaciar(self):
        self.primero = None
        self.ultimo = None
    
    def resetear(self):
        self.elementos_repetidos = 0
        self.mostrar_error = True

    def ordenar(self):
        if self.primero is None:
            return
        # Definir variables para el algoritmo bubble sort
        cambiado = True
        while cambiado:
            actual = self.primero
            cambiado = False
            # Recorrer la lista
            while actual.siguiente:
                # Comparar número atómico con siguiente elemento
                if actual.elemento.numeroAtomico < actual.siguiente.elemento.numeroAtomico:
                    # Intercambiar elementos
                    actual.elemento, actual.siguiente.elemento = actual.siguiente.elemento, actual.elemento
                    cambiado = True
                else:
                    actual = actual.siguiente
    
    #creamos la tabal donde se visualizaran los elementos
    def crearTabla(self, ventana):
        self.ordenar()

        self.tabla = ttk.Treeview(ventana, columns=("#1",'#2','#3'))
        scrollbar = ttk.Scrollbar(ventana, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.column("#0", width=100)
        self.tabla.column("#1", width=100)
        self.tabla.column("#2", width=100)
        self.tabla.heading("#0", text="Número Atómico")
        self.tabla.heading("#1", text="Simbolo")
        self.tabla.heading("#2", text="Elemento")


        if self.primero is None:
            return
        actual = self.primero
        self.tabla.insert('', 0, text=str(actual.elemento.numeroAtomico),values=(actual.elemento.simbolo,actual.elemento.nombreElemento))
        while actual.siguiente:
            actual = actual.siguiente
            self.tabla.insert('', 0, text=str(actual.elemento.numeroAtomico),values=(actual.elemento.simbolo,actual.elemento.nombreElemento))        

        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tabla.pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)

    def mostrarTabla(self):
        self.tabla.pack(side = tk.TOP,fill = tk.X,padx=22,pady=11) 
       



