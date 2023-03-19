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

    def insertar(self, elemento):
        if self.primero is None:
            self.primero = nodo_EleCompuesto(elemento = elemento)
        else:
            actual = nodo_EleCompuesto(elemento = elemento, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual
    
    #buscar todos los elementos de un compuesto
    def buscarElementos(self, codigoCompuesto):
        elementos = ""
        if self.primero is None:
            return
        actual = self.primero
        if actual.elemento.nombreCompuesto == codigoCompuesto:
            elementos += actual.elemento.elemento

        while actual.siguiente:
            actual = actual.siguiente
            if actual.elemento.nombreCompuesto == codigoCompuesto:
                elementos += actual.elemento.elemento

        # Separar los elementos del compuesto
        pila_elementos = []
        elemento_actual = ""
        for c in elementos:
            if c.isupper():
                if elemento_actual != "":
                    pila_elementos.append(elemento_actual)
                    elemento_actual = ""
                elemento_actual += c
            else:
                elemento_actual += c
        pila_elementos.append(elemento_actual)  # Agregar el último elemento

        # Invertir el orden de los elementos
        compuesto_invertido = ""
        while pila_elementos:
            compuesto_invertido += pila_elementos.pop()

        return compuesto_invertido