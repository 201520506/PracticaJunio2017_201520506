class NodoCola:
    def __init__(self):
        self.operacion=None
        self.siguiente=None
class Cola:
    def __init__(self):
        self.cabeza=None
        self.fondo=None

    def add(self, operacion):
        actual=NodoCola()
        actual.operacion=operacion
        if self.colavacia()==True:
            self.cabeza=actual
            self.fondo=actual
        else:
            self.fondo.siguiente=actual
            self.fondo=actual
    def sacar(self):
        if self.colavacia()==False:
            operacion=self.cabeza.operacion
            if self.cabeza==self.fondo:
                self.cabeza=None
                self.fondo=None
            else:
                self.cabeza=self.cabeza.siguiente
            return operacion
        else:
            return "Cola Vacia"

    def mostrar(self):
        reco=self.cabeza
        print("Listado de los elementos")
        i=0
        while reco:
            print "indice    "+str(i)+":" + str(reco.operacion)
            reco=reco.siguiente
            i=i+1
    def colavacia(self):
        if self.cabeza==None:
            return True
        else:
            return False
class NodoPila:
    def __init__(self):
        self.info=None
        self.siguiente=None
class Pila:
    def __init__(self):
        self.cabeza=None
    def push(self, dato):
        nuevo=NodoPila()
        nuevo.info=dato
        if self.cabeza==None:
            nuevo.siguiente=None
            self.cabeza=nuevo
        else:
            nuevo.siguiente=self.cabeza
            self.cabeza=nuevo
    def pop(self):
        if self.cabeza!=None:
            informacion=self.cabeza.info
            self.cabeza=self.cabeza.siguiente
            return informacion
        else:
            return "Pila Vacia"
    def imprimir(self):
        reco=self.cabeza
        print("LISTADO DE TODOS LOS ELEMENTOS DE LA PILA")
        while reco:
            print str(reco.info)+"->",
            reco=reco.siguiente

