class TiempoMaquina:
    def __init__(self, nombreMaquina, tiempo, nombreCompuesto):
        self.nombreMaquina = nombreMaquina
        self.tiempo = tiempo
        self.nombreCompuesto = nombreCompuesto

class NodoTiempoMaquina:
    def __init__(self, TiempoMaquina, siguiente = None, anterior = None):
        self.TiempoMaquina = TiempoMaquina
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleTiempoMaquina:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def insertar(self, TiempoMaquina):
        nuevo_nodo = NodoTiempoMaquina(TiempoMaquina = TiempoMaquina)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
    
    def devolverTiempo(self, nombreMaquina, nombreCompuesto):
        tiempo = 0
        actual = self.primero
        while actual:
            if actual.TiempoMaquina.nombreMaquina == nombreMaquina and actual.TiempoMaquina.nombreCompuesto == nombreCompuesto:
                tiempo = actual.TiempoMaquina.tiempo
            actual = actual.siguiente
        return tiempo
    
    def vaciar(self):
        self.primero = None
        self.ultimo = None

class NodoTiempoMaquina1:
    def __init__(self, TiempoMaquina, siguiente = None, anterior = None):
        self.TiempoMaquina = TiempoMaquina
        self.siguiente = siguiente
        self.anterior = anterior

class listaDobleTiempoMaquina1:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def insertar(self, TiempoMaquina):
        nuevo_nodo = NodoTiempoMaquina(TiempoMaquina = TiempoMaquina)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
    
    def devolverTiempo(self, nombreMaquina, nombreCompuesto):
        tiempo = 0
        actual = self.primero
        while actual:
            if actual.TiempoMaquina.nombreMaquina == nombreMaquina and actual.TiempoMaquina.nombreCompuesto == nombreCompuesto:
                tiempo = actual.TiempoMaquina.tiempo
            actual = actual.siguiente
        return tiempo
    
    def vaciar(self):
        self.primero = None
        self.ultimo = None