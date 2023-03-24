from tkinter import *
from tkinter import ttk
import tkinter as tk

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
    
    def insertar(self, elemento):
        if self.primero is None:
            self.primero = nodoElemento(elemento = elemento)
        else:
            actual = nodoElemento(elemento = elemento, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual
        
    def recorrer(self):
        if self.primero is None:
            print("aun no hay elementos en la lista")
            return
        actual = self.primero
        print("Elemento: ", actual.elemento.nombreElemento +'\n',
              "Simbolo: ", actual.elemento.simbolo +'\n',
              "Numero Atomico: ", actual.elemento.numeroAtomico +'\n')
        while actual.siguiente:
            actual = actual.siguiente
            print("Elemento: ", actual.elemento.nombreElemento +'\n',
                  "Simbolo: ", actual.elemento.simbolo +'\n',
                  "Numero Atomico: ", actual.elemento.numeroAtomico +'\n') 

    #verificar que no se repita elemento, numero atomico ni simbolo
    def verificarElemento(self, elemento):
        if self.primero is None:
            return True
        actual = self.primero
        if actual.elemento.nombreElemento == elemento.nombreElemento or actual.elemento.numeroAtomico == elemento.numeroAtomico or actual.elemento.simbolo == elemento.simbolo:
            return False
        while actual.siguiente:
            actual = actual.siguiente
            if actual.elemento.nombreElemento == elemento.nombreElemento or actual.elemento.numeroAtomico == elemento.numeroAtomico or actual.elemento.simbolo == elemento.simbolo:
                return False
        return True

    #vaciamos la lista doblemente enlazada        
    def vaciar(self):
        actual = self.primero
        while actual:
            siguiente = actual.siguiente
            del actual
            actual = siguiente
        self.primero = None

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
                if actual.elemento.numeroAtomico > actual.siguiente.elemento.numeroAtomico:
                    # Intercambiar elementos
                    actual.elemento, actual.siguiente.elemento = actual.siguiente.elemento, actual.elemento
                    cambiado = True
                else:
                    actual = actual.siguiente
    
    #creamos la tabal donde se visualizaran los elementos
    def crearTabla(self, ventana):
        self.ordenar()

        self.tabla = ttk.Treeview(ventana, columns=("#1",'#2','#3'))
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

        self.tabla.pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)

    def mostrarTabla(self):
        self.tabla.pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
       



