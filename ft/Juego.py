from TorredeHanoi import TorredeHanoi

discos=int(input("Ingrese cantidad de discos: "))
torre1 = TorredeHanoi(discos, 1)
torre1.llenar()
torre2 = TorredeHanoi(discos, 2)
torre3 = TorredeHanoi(discos, 3)

ban = True
while ban:
    torreA=int(input("De: "))
    torreB=int(input("A: "))
    if torreA == 1:
        if torre1.vacia:
            print("No hay discos en esta torre")
    elif torreA == 2:
        if torre2.vacia:
            print("No hay discos en esta torre")
    elif torreA == 3:
        if torre3.vacia:
            print("No hay discos en esta torre")
    else:
        print("Numero de torre invalido")

     