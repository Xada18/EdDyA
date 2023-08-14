from Pila import Pila

if __name__=='__main__':
    num = int(input("Ingrese un numero entero: "))
    if num > 0:
        pila=Pila(num)
        pila.factorial()
    else:
        print("Numero no valido")