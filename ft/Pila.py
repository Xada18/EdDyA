import numpy as np 

class Pila:
    __tamaño=0
    __tope=0
    __arreglo=None


    def __init__(self, n):
        self.__tamaño=n
        self.__tope=0
        self.__arreglo=np.empty(self.__tamaño, dtype=int)
        
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
        
    def mostrar(self):
        for i in range(self.__tamaño-1,-1,-1):
            print(self.__arreglo[i])
            
    def cadena(self):
        cadena=""
        for i in range(self.__tamaño-1,-1,-1):
            cadena+=str(self.__arreglo[i])
        return 
    
    def factorial(self):
        i=1
        while not self.llena():
            self.insertar(i)
            i+=1
        
        factor=1
        for elem in self.__arreglo:
            factor*=elem
        print(factor)        
    
        
        
    def test(self):
        self.insertar(1)
        self.insertar(2)
        self.insertar(3)
        self.insertar(4)
        self.mostrar()
        self.suprimir()
        self.suprimir()
        self.mostrar()
        self.suprimir()
        self.mostrar()

if __name__=='__main__':
    pila=Pila(3)
    pila.test()