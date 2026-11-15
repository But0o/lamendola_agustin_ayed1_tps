def imprimir_fila(fila: list[int]) -> None:
    """
    contrato

    Imprime recursivamente los elementos de una fila en una misma linea,
    alineados a la derecha.

    pre: fila es una lista de numeros
    post: muestra por pantalla los elementos de fila sin salto de linea final
    """
    if len(fila) == 0:
        return

    print(f"{fila[0]:5}", end="")
    imprimir_fila(fila[1:])


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    contrato

    Imprime recursivamente una matriz de M x N, una fila por linea.

    pre: matriz es una lista de M filas con N numeros cada una
    post: muestra por pantalla la matriz con sus filas y columnas alineadas
    """
    if len(matriz) == 0:
        return

    imprimir_fila(matriz[0])
    print()
    imprimir_matriz(matriz[1:])


def main() -> None:
    matriz = [
        [1, 20, 3, 4],
        [50, 6, 7, 80],
        [9, 10, 111, 12],
    ]

    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
