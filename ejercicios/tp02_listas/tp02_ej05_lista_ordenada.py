def lista_ordenada(lista):
    return lista == sorted(lista)

def main():
    lista = []

    cantidad = int(input("Ingrese la cantidad de digitos para la lista: "))

    for i in range(cantidad):
        n = input("Inrgese numeros para agregar a la lista: ")
        lista.append(n)
        

    print(lista_ordenada(lista))


if __name__ == "__main__":
    main()