class Pines:
    def __init__(self, numero,simboloElemento, nombreMaquina, colorPin):
        self.numero = numero
        self.simboloElemento = simboloElemento
        self.nombreMaquina = nombreMaquina
        self.colorPin = colorPin
    
class nodoPines:
    def __init__(self, pines, siguiente = None, anterior = None):
        self.pines = pines
        self.siguiente = siguiente
        self.anterior = anterior
    
class listaDoblePines:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, pines):
        nuevo_nodo = nodoPines(pines = pines)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.primero
            self.primero.anterior = nuevo_nodo
            self.primero = nuevo_nodo
    
    #recorrer por medio del numero de pin
    def recorrer(self, numero_pin, nombreMaquina):
        sintaxis = ""
        sintaxis += "<tr>\n"
        sintaxis += f"<td>Pin:{numero_pin}</td>\n"
        sintaxis += "<td colspan=\'1\' rowspan=\'1\'>"
        sintaxis += "<table border=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
        sintaxis += "<tr>\n"
        actual = self.ultimo
        while actual:    
            if actual.pines.numero == numero_pin and actual.pines.nombreMaquina == nombreMaquina: 
                sintaxis += "<td><table border=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
                sintaxis += f"<tr><td align=\'center\' bgcolor=\"{actual.pines.colorPin}\" color=\"{actual.pines.colorPin}\" >{actual.pines.simboloElemento}</td></tr>\n"
                sintaxis += "</table>\n"
                sintaxis += "</td>\n"
            actual = actual.anterior
        sintaxis += "</tr>\n"
        sintaxis += "</table>\n"
        sintaxis += "</td>\n"
        sintaxis += "</tr>\n"
        return sintaxis


    def vaciar(self):
        self.primero = None
        self.ultimo = None

