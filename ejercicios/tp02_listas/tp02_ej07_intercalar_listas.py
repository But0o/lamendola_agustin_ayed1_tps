def intercalar(lista1: list, lista2: list) -> list:
    """
    contrato

    Mezcla los elementos de una segunda lista dentro de la primera,
    intercalando uno de cada lista, y modifica directamente la
    primera lista.

    pre: lista1 y lista2 son listas cualquiera, pueden tener distinta longitud
    post: modifica lista1 intercalando en ella los elementos de lista2 mediante rebanadas, sin crear una lista nueva, y devuelve lista1 modificada
    """
    i = 0

    while i < len(lista2):
        posicion = i * 2 + 1
        lista1[posicion:posicion] = [lista2[i]]
        i += 1
    return lista1


def main() -> None:

    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]

    lista = intercalar(lista1,lista2)

    print(lista)



if __name__ == "__main__":
    main()
