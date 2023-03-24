import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from constante import style
from tkinter import *
from tkinter import ttk
import os
import sys
from webbrowser import get
import xml.etree.ElementTree as ET
from elementos.elementos import Elemento
from elementos.elementos import listaDobleElemento
from compuestos.compuestos import Compuesto
from compuestos.compuestos import listaDobleCompuesto
from compuestos.EleCompuesto import EleCompuesto
from maquinas.maquinas import Maquina
from maquinas.maquinas import listaDobleMaquina
from maquinas.pines import Pines



nuevoElementoIngreso = listaDobleElemento()
nuevoCompuestoIngreso = listaDobleCompuesto()
nuevaMaquinaIngreso = listaDobleMaquina()

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()
    
    def salir(self):
        sys.exit()

    def movetoAyuda(self):
        self.controller.show_frame(Ayuda)
    
    def movertoGestionarElementosQuimicos(self):
        self.controller.show_frame(GestionarElementosQuimicos)
    
    def movertoGestionCompuestos(self):
        self.controller.show_frame(GestionCompuestos)
    
    def movertoGestionMaquinas(self):
        self.controller.show_frame(GestionMaquinas)

    def reiniciar(self):
        nuevoElementoIngreso.vaciar()
        nuevoCompuestoIngreso.vaciar()
        nuevaMaquinaIngreso.vaciar()
        messagebox.showinfo("Reiniciar", "Se ha reiniciado el programa")
    
    def abrirXML(self):
        self.abrirXML_archivo = filedialog.askopenfile(title = 'Abrir Archivo', filetypes = [('XML files', '*.xml'), 
        ('All Files', '*.*')])
        cargarArchivo(self.abrirXML_archivo)

    def init_widgets(self):
        tk.Label(self, 
            text = "MENÚ PRINCIPAL",
            justify= tk.CENTER,
            **style.STYLE2).pack(side = tk.TOP,fill = tk.BOTH,expand = True,padx = 22,pady = 11)
        tk.Label(self,
            text = "Elija una opción",
            justify= tk.CENTER,
            **style.STYLE3).pack(side = tk.TOP,fill = tk.BOTH,expand = True,padx=22,pady=11)
        tk.Button(self,
            text = "Cargar Archivo XML",
            command= self.abrirXML,
            **style.STYLE,relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Generar un XML de Salida",
            #command=self.salir,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Gestionar Elementos Químicos",
            command=self.movertoGestionarElementosQuimicos,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Gestión de Compuestos",
            command=self.movertoGestionCompuestos,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Gestión de Máquinas",
            command=self.movertoGestionMaquinas,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Reiniciar el Sistema",
            command=self.reiniciar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Ayuda",
            command=self.movetoAyuda,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Salir",
            command=self.salir,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)

#---------------------Leer XML---------------------
def cargarArchivo(root):
    try:
        tree = open(root.name)
        messagebox.showinfo("Información", "Archivo XML cargado correctamente")
        if tree.readable():
            nueva_configuracion = ET.fromstring(tree.read())

            #leemos los elementos del XML
            for elemento in nueva_configuracion.findall('listaElementos/elemento'):
                numeroAtomico_elemento = elemento.find('numeroAtomico').text
                simbolo_elemento = elemento.find('simbolo').text
                nombre_elemento = elemento.find('nombreElemento').text
                #numero atomico es un entero
                numeroAtomico = int(numeroAtomico_elemento)
                
                #verificamos que no existan elementos repetidos
                elementoNuevo = Elemento(numeroAtomico, simbolo_elemento, nombre_elemento)
                repetidos = nuevoElementoIngreso.verificarElemento(elementoNuevo)

                if repetidos == False:
                    messagebox.showerror("Error", "Existen Elementos repetidos")
                    nuevoElementoIngreso.vaciar()
                    break
                else:
                    nuevoElementoIngreso.insertar(elementoNuevo)
 
            #leemos las máquinas del XML          
            for maquina in nueva_configuracion.findall('listaMaquinas/Maquina'):
                nombre_maquina = maquina.find('nombre').text
                numeroPines_maquina = maquina.find('numeroPines').text
                numeroElementos = maquina.find('numeroElementos').text
                if maquina.findall('pin'):
                    numeroPin = 1
                    pinesPin = []
                    for pin in maquina.findall('pin'):
                        for elementos in pin.findall('elementos/elemento'):
                            elemento_maquina = elementos.text
                            nuevoPin = Pines(numeroPin,elemento_maquina,nombre_maquina,nuevaMaquinaIngreso.codigo_colorPin())
                            pinesPin.append(nuevoPin)
                        numeroPin += 1
                numeroPines = int(numeroPines_maquina)
                numeroElementosMaquina = int(numeroElementos)
                nuevaMaquina = Maquina(nombre_maquina, numeroPines, numeroElementosMaquina, pinesPin)
                nuevaMaquinaIngreso.insertar(nuevaMaquina)

            #leemos los compuestos del XML
            for compuesto in nueva_configuracion.findall('listaCompuestos/compuesto'):
                nombre_compuesto = compuesto.find('nombre').text
                elementosCompuesto = []
                for elementos_compuesto in compuesto.findall('elementos/elemento'):
                    elementosInCompuesto = EleCompuesto(elementos_compuesto.text, nombre_compuesto)
                    elementosCompuesto.append(elementosInCompuesto)
                nuevoCompuesto = Compuesto(nombre_compuesto, elementosCompuesto)
                nuevoCompuestoIngreso.insertar(nuevoCompuesto)  

    except Exception as e:
        print('Error:',e)

#--------------------Gestion de elementos químicos--------------------
class GestionarElementosQuimicos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def salir(self):
        sys.exit()
    
    def regresar(self):
        self.controller.show_frame(Menu)
    
    def listarElementosQuimicos(self):
        ventana = tk.Tk()
        ventana.geometry("400x320") #ancho y alto
        ventana.title("Elementos Químicos")
        ventana.resizable(False,False)
        ventana.configure(background=style.BACKGROUND)

        def volver():
            ventana.destroy()

        tabla = ttk.Treeview(ventana, columns=("#1",'#2','#3'))
        tabla.column("#0", width=100)
        tabla.column("#1", width=100)
        tabla.column("#2", width=100)

        tabla.heading("#0", text="Número Atómico")
        tabla.heading("#1", text="Simbolo")
        tabla.heading("#2", text="Elemento")
        
        nuevoElementoIngreso.crearTabla(ventana)
        nuevoElementoIngreso.mostrarTabla()

        tk.Button(
            ventana,
            text = "Regresar",
            command=volver,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
    
    def agregarNuevoElemento(self):
        ventana = tk.Tk()
        ventana.geometry("400x380") #ancho y alto
        ventana.title("Elementos Químicos")
        ventana.resizable(False,False)
        ventana.configure(background=style.BACKGROUND)

        def volver():
            ventana.destroy()

        agregarNumeroAtomico = tk.Label(ventana, text="Inserte el número atómico",justify=tk.CENTER, **style.STYLE1)
        agregarNumeroAtomico.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        insertarNumeroAtomico = tk.Entry(ventana, **style.STYLE5)
        insertarNumeroAtomico.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        agregarSimbolo = tk.Label(ventana, text="Inserte el símbolo",justify=tk.CENTER, **style.STYLE1)
        agregarSimbolo.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        insertarSimbolo = tk.Entry(ventana, **style.STYLE5)
        insertarSimbolo.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        agregarNombreElemento = tk.Label(ventana, text="Inserte el nombre del elemento",justify=tk.CENTER, **style.STYLE1)
        agregarNombreElemento.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        insertarNombreElemento = tk.Entry(ventana, **style.STYLE5)
        insertarNombreElemento.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
       
        def agregar():
            try:
                nombreElemento = insertarNombreElemento.get()
                simboloElemento = insertarSimbolo.get()
                numeroAtomico = int(insertarNumeroAtomico.get())

                elementoNuevo = Elemento(numeroAtomico,simboloElemento,nombreElemento)
                elementoRepetido = nuevoElementoIngreso.verificarElemento(elementoNuevo)

                if elementoRepetido == False:
                    messagebox.showerror("Error", "El elemento ya existe")
                else:
                    nuevoElementoIngreso.insertar(elementoNuevo)
                    messagebox.showinfo("Felicidades", "Se ha agregado el nuevo elemento")
                    ventana.destroy()
                    
            except Exception as e:
                messagebox.showerror("Error",str(e)+"\nRellene los campos correctamente")
                

        tk.Button(ventana, text = "Agregar Elemento", command=agregar, **style.STYLE, relief=tk.FLAT, activebackground=style.BACKGROUND, activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)        
        tk.Button(ventana, text = "Regresar", command=volver, **style.STYLE, relief=tk.FLAT, activebackground=style.BACKGROUND, activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)

    def init_widgets(self):
        tk.Button(
            self,
            text = "Ver Listado de Elementos Químicos",
            command=self.listarElementosQuimicos,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Agregar Elemento Químico",
            command=self.agregarNuevoElemento,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)


#---------------------Gestion de compuestos---------------------
class GestionCompuestos(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def salir(self):
        sys.exit()
    
    def regresar(self):
        self.controller.show_frame(Menu)
    
    def ver_listado(self):
        ventana = tk.Tk()
        ventana.geometry("380x500") #ancho y alto
        ventana.title("Compuestos y Formulas")
        ventana.resizable(False,False)
        ventana.configure(background=style.BACKGROUND)

        def volver():
            ventana.destroy()
        
        nuevoCompuestoIngreso.verCompuesto_Formulas(ventana)
        nuevoCompuestoIngreso.verFormula_Compuestos()

        tk.Button(
            ventana,
            text = "Regresar",
            command=volver,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)

    def seleccionarCompuesto(self):
        ventana = tk.Tk()
        ventana.geometry("380x200")
        ventana.title("Seleccionar Compuesto")
        ventana.resizable(False,False)
        ventana.configure(background=style.BACKGROUND)

        def volver():
            ventana.destroy()
        
        seleccionar = tk.Label(ventana, text="Ingrese el nombre del compuesto:",justify=tk.CENTER, **style.STYLE1)
        seleccionar.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)
        insertarCompuesto = tk.Entry(ventana, **style.STYLE5)
        insertarCompuesto.pack(side = tk.TOP,fill = tk.BOTH,padx=22,pady=11)

        def obtenerNombreCompuesto():
            nombreCompuesto = insertarCompuesto.get()
            print(nombreCompuesto)

        tk.Button(ventana, text = "Aceptar", command=obtenerNombreCompuesto, **style.STYLE, relief=tk.FLAT, activebackground=style.BACKGROUND, activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)        
        tk.Button(ventana, text = "Regresar", command=volver, **style.STYLE, relief=tk.FLAT, activebackground=style.BACKGROUND, activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)


    def init_widgets(self):
        tk.Button(
            self,
            text = "Ver Listado de Compuestos y sus Fórmulas",
            command=self.ver_listado,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Analizar Compuesto",
            command=self.seleccionarCompuesto,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)


#---------------------Gestion de maquinas---------------------
class GestionMaquinas(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def salir(self):
        sys.exit()
    
    def regresar(self):
        self.controller.show_frame(Menu)

    def verPrueba(self):
        nuevaMaquinaIngreso.recorrer()

    def verImagen(self):
        nuevaMaquinaIngreso.verImg()

    def init_widgets(self):
        tk.Button(
            self,
            text = "Ver Gráficamente Listado de Máquinas",	
            command=self.verPrueba,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Visualizar imagen de la máquina",
            command=self.verImagen,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)



#----------------------Ayuda----------------------#
class Ayuda(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.init_widgets()

    def salir(self):
        sys.exit()
    
    def regresar(self):
        self.controller.show_frame(Menu)
    
    def doc_oficial(self):
        directorio = os.getcwd()
        os.startfile(directorio+"\Documentacion\DocumentacionOficial_202110509.pdf")
    
    def init_widgets(self):
        tk.Label(self,
            text = "Desarrollado por:",
            justify= tk.LEFT,
            **style.STYLE3).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Label(self,
            text = "Mario Ernesto Marroquín Pérez",
            justify= tk.LEFT,
            **style.STYLE4).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Label(self,
            text = "Carné:",
            justify= tk.LEFT,
            **style.STYLE3).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Label(self,
            text = "202110509",
            justify= tk.LEFT,
            **style.STYLE4).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Label(self,
            text = "Contacto:",
            justify= tk.LEFT,
            **style.STYLE3).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Label(self,
            text = "2815806340401@ingenieria.usac.edu.gt",
            justify= tk.LEFT,
            **style.STYLE4).pack(side = tk.TOP,fill = tk.BOTH,expand = False,padx=22,pady=11)
        tk.Button(
            self,
            text = "Manual de Usuario",
            #command=self.salir,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Documentación Oficial",
            command=self.doc_oficial,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)
        tk.Button(
            self,
            text = "Regresar",
            command=self.regresar,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT).pack(side = tk.TOP,fill = tk.X,padx=22,pady=11)