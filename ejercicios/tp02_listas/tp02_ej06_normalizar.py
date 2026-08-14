def normalizar(lista):
    suma = sum(lista)
    lista_normal = []

    for i in range(len(lista)):
        lista_normal.append(lista[i] / suma)
    return lista_normal


def main():
    lista = []
    cantidad = []

    cantidad = int(input("Ingrese la cantidad de numeros de la lista: "))

    for i in range(cantidad):
            n = int(input("Inrgese numeros para agregar a la lista: "))
            lista.append(n)

    print(normalizar(lista))

if __name__ == "__main__":
     main()