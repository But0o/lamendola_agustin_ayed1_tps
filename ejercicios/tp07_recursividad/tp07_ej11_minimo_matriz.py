def minimo_fila(fila: list[int]) -> int:
    """
    contrato

    Busca recursivamente el menor elemento de una fila.

    pre: fila es una lista no vacia de numeros
    post: devuelve el menor elemento de fila
    """
    if len(fila) == 1:
        return fila[0]

    minimo_resto = minimo_fila(fila[1:])

    if fila[0] < minimo_resto:
        return fila[0]

    return minimo_resto


def minimo_matriz(matriz: list[list[int]]) -> int:
    """
    contrato

    Busca el menor elemento de una matriz de M x N.

    pre: matriz es una lista no vacia de filas no vacias de numeros
    post: devuelve el menor elemento de matriz
    """
    if len(matriz) == 1:
        return minimo_fila(matriz[0])

    minimo_fila_actual = minimo_fila(matriz[0])
    minimo_resto = minimo_matriz(matriz[1:])

    if minimo_fila_actual < minimo_resto:
        return minimo_fila_actual

    return minimo_resto


def main() -> None:
    matriz = [
        [41, 20, 33, 14],
        [50, 6, 7, 80],
        [9, 10, 111, 12],
    ]

    print(f"El minimo elemento de la matriz es {minimo_matriz(matriz)}")


if __name__ == "__main__":
    main()
