from nodo import Nodo
class ListaEnlazada:
    __comienzo=None
    __cantidad=0

    def __init__(self):
        self.__comienzo=None
        self.__cantidad=0

    def vacia(self):
        return self.__comienzo==None

    def insertar(self, elemento, posicion):
        if posicion > 0 and posicion <= self.__cantidad:
            nodo=Nodo(elemento)
            if self.vacia():
                self.__comienzo=nodo
            else:
                if posicion == 1:
                    nodo.setSiguiente(self.__comienzo)
                    self.__comienzo=nodo
                else:
                    i=1
                    aux=self.__comienzo
                    while i < posicion-1 and aux:
                        aux=aux.getSiguiente()

                    nodo.setSiguiente(aux.getSiguiente)
                    aux.setSiguiente(nodo)
                    self.__cantidad+=1
        else: 
            print("Posicion no valida")

    def suprimir(self, posicion):
        if self.vacia():
            print("Lista vacia")

        elif not (posicion > 0 and posicion < self.__cantidad):
            print("Posicion no valida")

        else:
            if posicion==1:
                dato=self.__comienzo
                self.__comienzo=self.__comienzo.getSiguiente()
            else:
                i=1
                aux=self.__comienzo
                while i < posicion-1 and aux:
                    aux=aux.getSiguiente()
                
                dato=aux
                aux=aux.getSiguiente()
            del dato
        
    
    def recuperar(self, posicion):
        dato=None
        if not (posicion > 0 and posicion < self.__cantidad):
            print("Posicion no valida") 
        else:
            if posicion==1:
                dato=self.__comienzo
            else:
                i=1
                aux=self.__comienzo
                while i < posicion-1 and aux:
                    aux=aux.getSiguiente()
                
                dato=aux
            return dato

    def buscar(self, dato):
        aux=self.__comienzo
        while aux and aux.getDato() != dato:
            aux=aux.getSiguiente()
        
        return aux
    
    def primer_elemento(self):
        if self.vacia():
            return None
        else:
            return self.__comienzo.getDato()
    
    def ultimo_elemento(self):
        if self.vacia():
            return None
        else:
            aux=self.__comienzo
            while aux.getSiguiente():
                aux=aux.getSiguiente()
            return aux.getDato()
    
    def siguiente(self, posicion):
        dato=None
        if not (posicion > 0 and posicion < self.__cantidad-1):
            print("Posicion no valida")
        else:
            if posicion==1:
                dato=self.__comienzo.getSiguiente()
            else:
                i=1
                aux=self.__comienzo
                while i < posicion-1 and aux:
                    aux=aux.getSiguiente()
                
                dato=aux.getSiguiente()

        return dato
    
    def anterior(self, posicion):
        dato=None
        if not (posicion > 1 and posicion < self.__cantidad):
            print("Posicion no valida")
        else:
            i=1
            aux=self.__comienzo
            while i < posicion-1 and aux:
                aux=aux.getSiguiente()
            
            dato=aux

        return dato
    
    def recorrer(self): #Mostrar
        if self.vacia():
            print("Lista vacia")
        else:
            aux=self.__comienzo
            while aux:
                print(aux.getDato())
                aux=aux.getSiguiente()


import numpy as np

class ListaSecuencial:
    __dimension=0
    __cantidad=0
    __arreglo=None

    def __init__(self, dim):
        self.__dimension=dim
        self.__cantidad=0
        self.__arreglo=np.empty(dim, dtype=int)

    def vacia(self):
        return self.__cantidad==0          
        
    def insertar(self):
        