import numpy as np

class Hash:
    __arreglo=None
    __dimension=None

    def __init__(self, dim):
        dimension=self.calculaPrimo(dim)
        self.__arreglo=np.empty(dimension, dtype=int)
        self.__dimension=int(dimension)

        for i in range(self.__dimension):
            self.__arreglo[i]=-1

    def calculaPrimo(self, dim):
        num=2
        while num < dim:
            mod=dim%num
            if mod == 0:
                num=2
                dim+=1
            else:
                num+=1
        return dim
            

    def mostrar(self):
        for i in range(self.__dimension):
            print(f"{self.__arreglo[i]}")

    def hashing(self, elemento):
        return elemento%self.__dimension


    def insertar(self, elemento):
        mod=self.hashing(elemento)
        aux=mod
        
        while mod < self.__dimension and self.__arreglo[mod] != -1 and elemento != self.__arreglo[mod]: 
            mod+=1

        if mod==self.__dimension:
            mod=0
            while mod < aux and self.__arreglo[mod] != -1 and elemento != self.__arreglo[mod]: 
                mod+=1
                
            if mod == aux:
                print("No hay lugar, elemento no insertado")
            elif elemento == self.__arreglo[mod]:
                print("Elemento existente")
            elif self.__arreglo[mod] == -1:
                self.__arreglo[mod]=elemento
                print("Se inserto el elemento")

        elif elemento == self.__arreglo[mod]:
            print("Elemento existente")
        elif self.__arreglo[mod] == -1:
            self.__arreglo[mod]=elemento
            print("Se inserto el elemento")
            


    def buscar(self, elemento):
        mod=self.hashing(elemento)
        aux=mod
        flag=False
        while not flag and mod < self.__dimension and self.__arreglo[mod] != -1 :
            if self.__arreglo[mod] == elemento:
                print("Elemento encontrado")
                flag=True
            else:
                mod+=1

        if mod == self.__dimension:
            mod = 0
            while not flag and mod < aux and self.__arreglo[mod] != -1:
                if self.__arreglo[mod] == elemento:
                    print("Elemento encontrado")
                    flag=True
                else:
                    mod+=1
        
        if not flag:
            print("Elemento no existente")



    def suprimir(self, elemento):#no se puede
        mod=self.hashing(elemento)
        aux=mod
        flag=False
        while not flag and mod < self.__dimension and self.__arreglo[mod] != -1 :
            if self.__arreglo[mod] == elemento:
                print("Elemento encontrado")
                flag=True
            else:
                mod+=1

        if mod == self.__dimension:
            mod = 0
            while not flag and mod < aux and self.__arreglo[mod] != -1:
                if self.__arreglo[mod] == elemento:
                    print("Elemento encontrado")
                    flag=True
                else:
                    mod+=1
        
        if not flag:
            print("Elemento no existente")
        
    

    def test(self):
        print(self.__dimension)
        print("43078713  " + str(43078713%self.__dimension))
        print("44665750  " + str(44665750%self.__dimension))
        print("44316666  " + str(44316666%self.__dimension))
        print("42432234  " + str(42432234%self.__dimension))
        print("46789234  " + str(46789234%self.__dimension))
        print("41121212  " + str(41121212%self.__dimension))
        print("41121212  " + str(41121212%self.__dimension))
        print("43078013  " + str(43078013%self.__dimension))
        self.mostrar()
        print("")
        self.insertar(43078713)
        self.insertar(44665750)
        self.insertar(44316666)
        self.insertar(42432234)
        self.insertar(46789234)
        self.insertar(41121212)
        self.insertar(41121212)
        self.insertar(43078013)
        print("")
        self.mostrar()
        print("")
        self.buscar(43078713)
        print("")
        self.buscar(44444444)
    
if __name__=='__main__':
    dim=14
    h=Hash(dim)
    h.test()
