class NodoDisperso:
    def __init__(self, info):
        self.info = info
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

    def getInfo(self):
        return str(self.info)

    def setInfo(self, info):
        self.info = str(info)

    def getDerecha(self):
        return self.derecha

    def setDerecha(self, derecha):
        self.derecha = derecha

    def getIzquierda(self):
        return self.izquierda

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda

    def getArriba(self):
        return self.arriba

    def setArriba(self, arriba):
        self.arriba = arriba

    def getAbajo(self):
        return self.abajo

    def setAbajo(self, abajo):
        self.abajo = abajo



class MatrizOrto:
    def __init__(self):
        nuevo = NodoDisperso("Cabeza")
        self.cabeza = nuevo

    def filas(self, auxiliar, letra):
        while auxiliar:
            if auxiliar.getAbajo() != None:
                if auxiliar.getAbajo().getInfo() > letra:
                    return auxiliar
                else:
                    auxiliar = auxiliar.getAbajo()
            else:
                return auxiliar

    def columnas(self, auxiliar, letra):
        while auxiliar:
            if auxiliar.getDerecha() != None:
                if auxiliar.getDerecha().getInfo() > letra:
                    return auxiliar
                else:
                    auxiliar = auxiliar.getDerecha()
            else:
                return auxiliar

    def compararfila(self, letra):
        auxiliar = self.cabeza.getAbajo()
        while auxiliar:
            if auxiliar.getInfo() == letra:
                return True
            auxiliar = auxiliar.getAbajo()
        return False

    def compararcolumna(self, letra):
        auxiliar = self.cabeza.getDerecha()
        while auxiliar:
            if auxiliar.getInfo() == letra:
                return True
            auxiliar = auxiliar.getDerecha()
        return False

    def imprimir(self):
        auxiliar = self.cabeza
        while auxiliar:
            print str(auxiliar.getInfo() + " "),
            auxiliar = auxiliar.getDerecha()
        print "\n"
        auxiliar = self.cabeza.getAbajo()
        while auxiliar:
            print str(auxiliar.getInfo() + " ")
            auxiliar = auxiliar.getAbajo()

    def buscarletra(self, letra):
        respuesta = ""
        auxiliar = self.cabeza.getAbajo()
        fila = None
        while auxiliar:
            if auxiliar.getInfo() == letra:
                fila = auxiliar
                auxiliar = None
            else:
                auxiliar = auxiliar.getAbajo()
        while fila:
            respuesta = respuesta + fila.getInfo() + "-"
            if fila.getProfundidabajo() != None:
                auxiliar2 = fila.getProfundidabajo()
                while auxiliar2 != None:
                    respuesta = respuesta + auxiliar2.getInfo() + "-"
                    auxiliar2 = auxiliar2.getProfundidabajo()
            fila = fila.getDerecha()
        return respuesta

    def buscarCorreo(self, correo):
        respuesta = ""
        auxiliar = self.cabeza.getDerecha()
        columna = None
        while auxiliar:
            if auxiliar.getInfo() == correo:
                columna = auxiliar
                auxiliar = None
            else:
                auxiliar = auxiliar.getDerecha()
        while columna:
            respuesta = respuesta + columna.getInfo() + "-"
            if columna.getProfundidabajo() != None:
                auxiliar2 = columna.getProfundidabajo()
                while auxiliar2 != None:
                    respuesta = respuesta + auxiliar2.getInfo() + "-"
                    auxiliar2 = auxiliar2.getProfundidabajo()
            columna = columna.getAbajo()
        return respuesta

    def insertar(self, dato, dato2):
        letra = str(dato[0])
        fila = self.cabeza
        columna = self.cabeza
        nuevo = NodoDisperso(dato)
        if self.cabeza.getDerecha() == None:
            fila = NodoDisperso(letra)
            columna = NodoDisperso(dato2)
            self.cabeza.setDerecha(columna)
            columna.setIzquierda(self.cabeza)
            self.cabeza.setAbajo(fila)
            fila.setArriba(self.cabeza)
            nuevo.setIzquierda(fila)
            fila.setDerecha(nuevo)
            nuevo.setArriba(columna)
            columna.setAbajo(nuevo)
        else:
            existefila = self.compararfila(letra)
            existecolumna = self.compararcolumna(dato2)
            if existecolumna == False and existefila == False:
                auxiliar = self.cabeza
                # PARA VER EN QUE FILA DEBE DE IR
                fila = self.filas(auxiliar, letra)
                # PARA VER EN QUE COLUMNA DEBE DE IR
                columna = self.columnas(auxiliar, dato2)
                # SE CREAN LOS ENCABEZADOS DE LA FILA Y COLUMNA
                auxiliarfila = NodoDisperso(letra)
                auxiliarcolumna = NodoDisperso(dato2)
                # ENLACES DE LAS FILAS
                if fila.getAbajo() != None:
                    auxiliarfila.setAbajo(fila.getAbajo())
                    fila.getAbajo().setArriba(auxiliarfila)
                fila.setAbajo(auxiliarfila)
                auxiliarfila.setArriba(fila)
                # ENLACES DE LAS COLUMNAS
                if columna.getDerecha() != None:
                    auxiliarcolumna.setDerecha(columna.getDerecha())
                    columna.getDerecha().setIzquierda(auxiliarcolumna)
                columna.setDerecha(auxiliarcolumna)
                auxiliarcolumna.setIzquierda(columna)
                # ENLACES AL NODO NUEVO
                auxiliarfila.setDerecha(nuevo)
                nuevo.setIzquierda(auxiliarfila)
                auxiliarcolumna.setAbajo(nuevo)
                nuevo.setArriba(auxiliarcolumna)
            if existefila == True and existecolumna == False:
                columna = self.columnas(self.cabeza, dato2)
                # METEMOS EL INDICE DE LA COLUMNA
                auxiliarcolumna = NodoDisperso(dato2)
                auxiliarcolumna.setDerecha(columna.getDerecha())
                if columna.getDerecha() != None:
                    columna.getDerecha().setIzquierda(auxiliarcolumna)
                auxiliarcolumna.setIzquierda(columna)
                columna.setDerecha(auxiliarcolumna)
                # METEMOS EL DATO EN LA MATRIZ
                auxiliar = self.cabeza.getAbajo()
                while not (auxiliar.getInfo() == letra):
                    auxiliar = auxiliar.getAbajo()

                fila = auxiliar
                prueba = auxiliar
                while prueba.getDerecha() != None:
                    prueba = prueba.getDerecha()
                    auxiliar2 = prueba
                    while auxiliar2.getArriba() != None:
                        auxiliar2 = auxiliar2.getArriba()
                    if auxiliar2.getInfo() < dato2:
                        fila = prueba
                    auxiliar = auxiliar.getDerecha()

                nuevo.setArriba(auxiliarcolumna)
                auxiliarcolumna.setAbajo(nuevo)
                nuevo.setDerecha(fila.getDerecha())
                if fila.getDerecha() != None:
                    fila.getDerecha().setIzquierda(nuevo)
                fila.setDerecha(nuevo)
                nuevo.setIzquierda(fila)
            if existefila == False and existecolumna == True:
                fila = self.filas(self.cabeza, letra)
                # METEMOS EL NUEVO INDICE DE LA FIAL
                auxiliarfila = NodoDisperso(letra)
                auxiliarfila.setAbajo(fila.getAbajo())
                if fila.getAbajo() != None:
                    fila.getAbajo().setArriba(auxiliarfila)
                fila.setAbajo(auxiliarfila)
                auxiliarfila.setArriba(fila)
                # METEMOS EL DATO EN LA MATRIZ
                auxiliar = self.cabeza.getDerecha()
                while not (auxiliar.getInfo() == dato2):
                    auxiliar = auxiliar.getDerecha()
                columna = self.filas(auxiliar, letra)
                nuevo.setAbajo(columna.getAbajo())
                if columna.getAbajo() != None:
                    columna.getAbajo().setArriba(nuevo)
                columna.setAbajo(nuevo)
                nuevo.setArriba(columna)
                nuevo.setIzquierda(auxiliarfila)
                auxiliarfila.setDerecha(nuevo)
            if existefila == True and existecolumna == True:
                auxiliar = self.cabeza.getDerecha()
                while not (auxiliar.getInfo() == dato2):
                    auxiliar = auxiliar.getDerecha()
                columna = self.filas(auxiliar, letra)
                if columna.getAbajo() != None:
                    if columna.getAbajo().getInfo()[0] == letra[0]:
                        actual = columna.getAbajo()
                        while actual.getProfundidabajo():
                            actual = actual.getProfundidabajo()
                        actual.setProfundidabajo(nuevo)
                        nuevo.setProfundidadarriba(actual)
                else:
                    auxiliar = self.cabeza.getAbajo()
                    while not (auxiliar.getInfo() == letra):
                        auxiliar = auxiliar.getAbajo()
                    prueba = auxiliar
                    fila = auxiliar
                    while prueba.getDerecha():
                        prueba = prueba.getDerecha()
                        auxiliar2 = prueba
                        while auxiliar2.getArriba():
                            auxiliar2 = auxiliar2.getArriba()
                        if auxiliar2.getInfo() < dato2:
                            fila = prueba
                        auxiliar = auxiliar.getDerecha()
                    nuevo.setDerecha(fila.getDerecha())
                    if fila.getDerecha() != None:
                        fila.getDerecha().setIzquierda(nuevo)
                    fila.setDerecha(nuevo)
                    nuevo.setIzquierda(fila)
                    nuevo.setAbajo(columna.getAbajo())
                    if columna.getAbajo() != None:
                        columna.getAbajo.setArriba(nuevo)
                    nuevo.setArriba(columna)
                    columna.setAbajo(nuevo)

    def buscarNodo(self, valor):
        letra = str(valor[0])
        auxiliar = self.cabeza.getAbajo()
        fila = None
        while auxiliar:
            if auxiliar.getInfo() == letra:
                fila = auxiliar
                auxiliar = None
            else:
                auxiliar = auxiliar.getAbajo()
        while fila:
            if fila.getInfo() == valor:
                return fila
            if fila.getProfundidabajo() != None:
                auxiliar = fila.getProfundidabajo()
                while auxiliar:
                    if auxiliar.getInfo() == valor:
                        return auxiliar
                    auxiliar = auxiliar.getProfundidabajo()
            fila = fila.getDerecha()
        print("NO envia nada")
        return None

