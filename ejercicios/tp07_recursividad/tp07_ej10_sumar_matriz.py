def sumar_fila(fila: list[int]) -> int:
    """
    contrato

    Suma recursivamente los elementos de una fila, sin usar sum().

    pre: fila es una lista de numeros
    post: devuelve la suma de los elementos de fila (0 si esta vacia)
    """
    if len(fila) == 0:
        return 0

    return fila[0] + sumar_fila(fila[1:])


def sumar_matriz(matriz: list[list[int]]) -> int:
    """
    contrato

    Suma todos los elementos de una matriz de M x N, sin usar sum().

    pre: matriz es una lista de M filas con N numeros cada una
    post: devuelve la suma de todos los elementos de matriz (0 si no tiene filas)
    """
    if len(matriz) == 0:
        return 0

    return sumar_fila(matriz[0]) + sumar_matriz(matriz[1:])


def main() -> None:
    matriz = [
        [1, 20, 3, 4],
        [50, 6, 7, 80],
        [9, 10, 111, 12],
    ]

    print(f"La suma de los elementos de la matriz es {sumar_matriz(matriz)}")


if __name__ == "__main__":
    main()
