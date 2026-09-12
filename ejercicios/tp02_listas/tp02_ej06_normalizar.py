def normalizar(lista: list[int]) -> list[float]:
    """
    contrato

    Transforma una lista de números para que cada valor represente
    la proporción que le corresponde respecto del total, de modo
    que todos los valores resultantes sumen 1.

    pre: lista es una lista de numeros enteros
    post: devuelve una nueva lista donde cada elemento representa la proporcion del original respecto a la suma total, de forma que la suma de la lista resultante sea 1.0
    """
    suma = sum(lista)
    lista_normal = []

    for i in range(len(lista)):
        lista_normal.append(lista[i] / suma)
    return lista_normal


def main() -> None:
    lista = []
    cantidad = []

    cantidad = int(input("Ingrese la cantidad de numeros de la lista: "))

    for i in range(cantidad):
            n = int(input("Inrgese numeros para agregar a la lista: "))
            lista.append(n)

    print(normalizar(lista))

if __name__ == "__main__":
     main()
