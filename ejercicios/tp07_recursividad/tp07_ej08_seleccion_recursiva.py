def posicion_minimo(lista: list[int], desde: int, minimo: int) -> int:
    """
    contrato

    Busca recursivamente la posicion del menor elemento de la lista a
    partir de una posicion dada, sin usar min().

    pre: lista es una lista de enteros; desde es una posicion de la lista y minimo es la posicion del menor elemento encontrado hasta ahora
    post: devuelve la posicion del menor elemento de lista[desde:] o minimo si ninguno es menor
    """
    if desde == len(lista):
        return minimo

    if lista[desde] < lista[minimo]:
        minimo = desde

    return posicion_minimo(lista, desde + 1, minimo)


def ordenar_seleccion(lista: list[int], inicio: int = 0) -> None:
    """
    contrato

    Ordena una lista de menor a mayor con el metodo de seleccion: coloca el
    elemento mas pequeno en la primera posicion y ordena el resto con una
    llamada recursiva.

    pre: lista es una lista de enteros; inicio es la primera posicion a ordenar
    post: lista[inicio:] queda ordenada de menor a mayor (se modifica la lista recibida)
    """
    if inicio >= len(lista) - 1:
        return

    menor = posicion_minimo(lista, inicio + 1, inicio)
    lista[inicio], lista[menor] = lista[menor], lista[inicio]

    ordenar_seleccion(lista, inicio + 1)


def main() -> None:
    lista = list(map(int, input("Ingrese los numeros separados por espacios: ").split()))

    ordenar_seleccion(lista)

    print(f"Lista ordenada: {lista}")


if __name__ == "__main__":
    main()
