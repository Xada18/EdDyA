from Nodo import Nodo

class ArbolBinario:
    __raiz=None
    

    def __init__(self):
        self.__raiz=None
        

    def insertar(self, elemento):
        nodo = Nodo(elemento)
        if self.__raiz==None:
            self.__raiz=nodo
        else:
            aux=self.__raiz
            if aux.getSiguiente() == None:
                aux.setSiguiente(nodo)
            elif aux.getAnterior() == None:
                aux.set


    def suprimir(self):
        pass

    def buscar(self, elemento):
        pass

    def nivel(self):
        pass

    def hoja(self):
        pass

    def hijo(self):
        pass
    
    def padre(self):
        pass
    
    def camino(self):
        pass

    def altura(self):
        pass

    def InOrden(self):
        pass

    def PreOrden(self):
        pass

    def PosOrden(self):
        pass
