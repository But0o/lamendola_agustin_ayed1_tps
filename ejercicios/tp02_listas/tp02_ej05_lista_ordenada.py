def lista_ordenada(lista: list) -> bool:
    """
    contrato

    Revisa si los elementos de una lista están ordenados de menor a
    mayor.

    pre: lista es una lista cualquiera
    post: devuelve True si la lista esta ordenada en forma ascendente, False en caso contrario
    """
    return lista == sorted(lista)

def main() -> None:
    lista = []

    cantidad = int(input("Ingrese la cantidad de digitos para la lista: "))

    for i in range(cantidad):
        n = input("Inrgese numeros para agregar a la lista: ")
        lista.append(n)
        

    print(lista_ordenada(lista))


if __name__ == "__main__":
    main()
