import numpy as np
from ClaseNodo import Nodo
class Cola:
    __primero=None
    __ultimo=None

    def __init__(self):
        self.__primero=None
        self.__ultimo=None

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.vacia():
            self.__primero=nodo
        else:
            aux=self.__primero
            while aux.getSiguiente():
                aux=aux.getSiguiente()
            aux.setSiguiente(nodo)
        
        self.__ultimo=nodo
            

    def suprimir(self):
        if not self.vacia():
            primero=self.__primero
            self.__primero=self.__primero.getSiguiente()
            del primero

    def vacia(self):
        if self.__primero is None:
            return True
        else:
            return False
        
    def recorrer(self):
        nodo = self.__primero
        while nodo.getSiguiente():
            nodo = nodo.getSiguiente()