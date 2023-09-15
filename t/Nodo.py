
class Nodo:
    __dato=None
    __siguiente=None
    __anterior=None

    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
        self.__anterior=None

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self,sig):
        self.__siguiente=sig

    def getSiguiente(self):
        return self.__siguiente
    
    def setAnterior(self, ant):
        self.__anterior=ant

    def getAnterior(self):
        return self.__anterior



