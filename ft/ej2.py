from Pila import Pila

if __name__=='__main__':
    pila = Pila(8)

    numero = int(input("Ingrese un numero: "))
    
    for _ in range(8):
        modulo = numero%2
        numero = numero/2
        pila.insertar(modulo)
    
    print(pila.cadena())

    

