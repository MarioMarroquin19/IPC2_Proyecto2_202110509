class EleCompuesto:
    def __init__(self, elemento, nombreCompuesto):
        self.elemento = elemento
        self.nombreCompuesto = nombreCompuesto

    
class nodo_EleCompuesto:
    def __init__(self,elemento,siguiente = None, anterior = None):
        self.elemento = elemento
        self.siguiente = siguiente
        self.anterior = anterior

class Lista_EleCompuesto:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, elemento):
        actual  = nodo_EleCompuesto(elemento = elemento)
        if self.primero is None:
            self.primero = actual
            self.ultimo = actual
        else:
            actual.anterior = self.ultimo
            self.ultimo.siguiente = actual
            self.ultimo = actual
        

    #buscar todos los elementos de un compuesto
    def buscarElementos(self, codigoCompuesto):
        elementos = ""
        actual = self.primero
        while actual:
            if actual.elemento.nombreCompuesto == codigoCompuesto:
                elementos += actual.elemento.elemento
            actual = actual.siguiente
        return elementos
    
    def devolverElementos(self, codigoCompuesto):
        actual = self.primero
        while actual:
            if actual.elemento.nombreCompuesto == codigoCompuesto:
                yield actual.elemento.elemento
            actual = actual.siguiente

    def vaciar(self):
        self.primero = None
        self.ultimo = None
