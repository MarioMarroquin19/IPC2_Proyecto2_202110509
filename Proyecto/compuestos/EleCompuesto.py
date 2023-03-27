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

    def insertar(self, maquina):
        actual  = nodo_EleCompuesto(elemento = maquina)
        if self.primero is None:
            self.primero = actual
            self.ultimo = actual
        else:
            actual.siguiente = self.primero
            self.primero.anterior = actual
            self.primero = actual

    #buscar todos los elementos de un compuesto
    def buscarElementos(self, codigoCompuesto):
        elementos = ""
        actual = self.ultimo
        while actual:
            if actual.elemento.nombreCompuesto == codigoCompuesto:
                elementos += actual.elemento.elemento
            actual = actual.anterior
        return elementos

    def vaciar(self):
        self.primero = None
        self.ultimo = None
