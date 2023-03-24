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

    def insertar(self, pines):
        if self.primero is None:
            self.primero = nodoPines(pines = pines)
        else:
            actual = nodoPines(pines = pines, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual
    
    #recorrer por medio del numero de pin
    def recorrer(self, numero_pin, nombreMaquina):
        sintaxis = ""
        sintaxis += "<tr>\n"
        sintaxis += "<td>Pin:"+str(numero_pin)+"</td>\n"
        sintaxis += "<td colspan=\'1\' rowspan=\'1\'>"
        sintaxis += "<table border=\'1\' cellpadding=\'0\' cellspacing=\'0\'>\n"
        sintaxis += "<tr>\n"
        if self.primero is None:
            return
        actual = self.primero
        elementos = []
        coloresPin = []
        if actual.pines.numero == numero_pin and actual.pines.nombreMaquina == nombreMaquina:
            elementos.append(actual.pines.simboloElemento)
            coloresPin.append(actual.pines.colorPin)
            '''sintaxis += "<td><table border=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
            sintaxis += "<tr><td align=\'center\'>"+actual.pines.simboloElemento+"</td></tr>\n"
            sintaxis += "</table>\n"
            sintaxis += "</td>\n"'''
            actual = actual.siguiente
        while actual:    
            if actual.pines.numero == numero_pin and actual.pines.nombreMaquina == nombreMaquina: 
                elementos.append(actual.pines.simboloElemento)
                coloresPin.append(actual.pines.colorPin)
                '''sintaxis += "<td><table border=\'0\' cellpadding=\'0\' cellspacing=\'0\'>\n"
                sintaxis += "<tr><td align=\'center\'>"+actual.pines.simboloElemento+"</td></tr>\n"
                sintaxis += "</table>\n"
                sintaxis += "</td>\n"'''
            actual = actual.siguiente
        elementos.reverse()
        for i in range(len(elementos)):
        #for elemento in elementos:
            sintaxis += "<td><table border=\'0\' cellpadding=\'10\' cellspacing=\'0\'>\n"
            sintaxis += "<tr><td align=\'center\' bgcolor=\""+coloresPin[i]+"\" color=\""+coloresPin[i]+"\" >"+elementos[i]+"</td></tr>\n"
            sintaxis += "</table>\n"
            sintaxis += "</td>\n"
        sintaxis += "</tr>\n"
        sintaxis += "</table>\n"
        sintaxis += "</td>\n"
        sintaxis += "</tr>\n"
        return sintaxis


    def vaciar(self):
        actual = self.primero
        while actual:
            siguiente = actual.siguiente
            del actual
            actual = siguiente
        self.primero = None

