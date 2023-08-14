import numpy as np 

class TorredeHanoi:
    __numero=0
    __tamaño=0
    __tope=0
    __arreglo=None


    def __init__(self, n, num):
        self.__numero=num
        self.__tamaño=n
        self.__tope=0
        self.__arreglo=np.empty(self.__tamaño, dtype=int)

    def getNumero(self):
        return self.__numero
    
    def llenar(self):
        i=self.__tamaño
        while not self.llena():
            self.insertar(i)
            i-=1

    def insertar(self, elemento):
        if not self.llena():
            self.__arreglo[self.__tope]=elemento
            self.__tope+=1

    def suprimir(self):
        if not self.vacia():
            self.__arreglo[self.__tope-1]=0
            self.__tope-=1

    def llena(self):
        if self.__tope == self.__tamaño:
            return True
        else:
            return False
        
    def vacia(self):
        if self.__tope == 0:
            return True
        else:
            return False
        
    def __gt__(self, otro):
        return self.__arreglo[self.__tope-1] > otro.__arreglo[otro.__tope-1]
    
    def sacar(self):
        disco=self.__arreglo[self.__tope-1]
        self.suprimir()
        return disco
    
    def 