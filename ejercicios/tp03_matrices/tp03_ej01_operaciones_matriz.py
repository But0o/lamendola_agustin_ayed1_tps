from typing import List


def cargar_matriz(n: int) -> List[List[int]]:
    """
    Contrato: dado un entero n, construye y devuelve una matriz cuadrada de
    n x n cargada con enteros ingresados por teclado.

    Precondición: n > 0.
    Postcondición: el resultado es una lista de n listas, cada una con n
    elementos enteros.
    """
    matriz = []
    for i in range(n):
        fila = []
        for columna in range(n):
            numero = int(input("Ingrese un numero: "))
            fila.append(numero)
        matriz.append(fila)
    return matriz


def ordenar_matriz(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz, ordena de forma ascendente los elementos de
    cada fila, de forma independiente entre sí.

    Precondición: matriz es una lista de listas de enteros, no vacía.
    Postcondición: cada fila de matriz queda ordenada de menor a mayor.
    La cantidad de filas y columnas no cambia. Modifica matriz in-place.
    """
    for fila in matriz: fila.sort()


def interalar_fila(matriz: List[List[int]], fila1: int, fila2: int) -> None:
    """
    Contrato: dada una matriz y dos índices de fila, intercambia el
    contenido completo de ambas filas.

    Precondición: 0 <= fila1 < len(matriz) y 0 <= fila2 < len(matriz).
    Postcondición: lo que antes estaba en matriz[fila1] ahora está en
    matriz[fila2], y viceversa. Modifica matriz in-place.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercalar_columna(matriz: List[List[int]], col1: int, col2: int) -> None:
    """
    Contrato: dada una matriz y dos índices de columna, intercambia el
    contenido de ambas columnas en todas las filas.

    Precondición: 0 <= col1 < len(matriz) y 0 <= col2 < len(matriz)
    (columnas válidas para todas las filas).
    Postcondición: para cada fila, el valor que estaba en la posición col1
    ahora está en col2, y viceversa. Modifica matriz in-place.
    """
    for fila in matriz: fila[col1], fila[col2] = fila[col2], fila[col1]


def trasponer_matriz(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz cuadrada, la convierte en su transpuesta
    (intercambia filas por columnas).

    Precondición: matriz es cuadrada (n x n).
    Postcondición: para todo i, j, el nuevo matriz[i][j] es igual al
    matriz[j][i] original. Modifica matriz in-place.
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):  matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]


def promedio_matriz(matriz: List[List[int]], num: int) -> float:
    """
    Contrato: dada una matriz y un número de fila, calcula el promedio
    aritmético de los elementos de esa fila.

    Precondición: 0 <= num < len(matriz), y la fila num tiene al menos
    un elemento.
    Postcondición: el resultado devuelto es igual a la suma de los
    elementos de matriz[num] dividida por su cantidad. No modifica matriz.
    """
    cant = len(matriz[num])
    suma = sum(matriz[num])
    promedio = suma / cant
    return promedio


def procentaje_impares(matriz: List[List[int]], num: int) -> float:
    """
    Contrato: dada una matriz y un número de columna, calcula qué
    porcentaje de los elementos de esa columna son impares.

    Precondición: 0 <= num < len(matriz), matriz es cuadrada.
    Postcondición: el resultado es un valor entre 0 y 100, igual a
    (cantidad de impares en la columna num / cantidad total de filas) * 100.
    No modifica matriz.
    """
    contador_impares = 0
    for i in range(len(matriz)):
        if matriz[i][num] % 2 == 1:
            contador_impares += 1
    cant_total = len(matriz)
    porcentaje = (contador_impares / cant_total) * 100
    return porcentaje


def matriz_simetrica(matriz: List[List[int]]) -> bool:
    """
    Contrato: dada una matriz cuadrada, determina si es simétrica respecto
    a su diagonal principal.

    Precondición: matriz es cuadrada (n x n).
    Postcondición: devuelve True si y solo si matriz[i][j] == matriz[j][i]
    para todo par de índices válidos i, j. No modifica matriz.
    """
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if not matriz[i][j] == matriz[j][i]:
                return False
    return True


def matriz_simetrica_secundaria(matriz: List[List[int]]) -> bool:
    """
    Contrato: dada una matriz cuadrada, determina si es simétrica respecto
    a su diagonal secundaria.

    Precondición: matriz es cuadrada (n x n).
    Postcondición: devuelve True si y solo si
    matriz[i][j] == matriz[n-1-j][n-1-i] para todo par de índices válidos
    i, j, con n = len(matriz). No modifica matriz.
    """
    n = len(matriz)
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if not matriz[i][j] == matriz[n - 1 - j][n - 1 - i]:
                return False
    return True


def columna_capicua(matriz: List[List[int]]) -> List[int]:
    """
    Contrato: dada una matriz cuadrada, identifica qué columnas son
    palíndromas (se leen igual de arriba hacia abajo que de abajo hacia
    arriba).

    Precondición: matriz es cuadrada (n x n).
    Postcondición: el resultado es una lista con los índices i tales que
    la columna i, leída de arriba a abajo, es igual a sí misma leída de
    abajo a arriba. No modifica matriz.
    """
    capicuas = []
    for i in range(len(matriz)):
        columna = [fila[i] for fila in matriz]
        invertida = columna[::-1]
        if columna == invertida:
            capicuas.append(i)
    return capicuas


def mostar_matriz(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz, la muestra por pantalla, fila por fila.

    Precondición: matriz es una lista de listas.
    Postcondición: se imprime una línea por cada fila de matriz, en el
    orden en que aparecen. No modifica matriz.
    """
    for fila in matriz: print(fila)


def main() -> None:
    # Punto A
    n = int(input("Ingrese el numero para la dimension de la matriz: "))
    matriz = cargar_matriz(n)
    mostar_matriz(matriz)

    # Punto B
    ordenar_matriz(matriz)
    mostar_matriz(matriz)

    # Punto C
    fila1 = int(input("Ingrese la primer fila para intercambiar: "))
    fila2 = int(input("Ingrese la segunda fila para intercambiar: "))
    interalar_fila(matriz, fila1, fila2)
    mostar_matriz(matriz)

    # Punto D
    col1 = int(input("Ingrese la primer columna para intercambiar: "))
    col2 = int(input("Ingrese la segunda columna para intercambiar: "))
    intercalar_columna(matriz, col1, col2)
    mostar_matriz(matriz)

    # Punto E
    trasponer_matriz(matriz)
    mostar_matriz(matriz)

    # Punto F
    num = int(input("Ingrese el numero de la fila para saber el promedio: "))
    print(promedio_matriz(matriz, num))

    # Punto G
    num = int(input("Ingrese el numero de columna para calcular el porcentaje: "))
    print(procentaje_impares(matriz, num))

    # Punto H
    if matriz_simetrica(matriz):
        print("Es simetrica")
    else:
        print("No es simetrica")

    # Punto I
    if matriz_simetrica_secundaria(matriz):
        print("Es simetrica")
    else:
        print("No es simetrica")

    # Punto J
    print(columna_capicua(matriz))


if __name__ == "__main__":
    main()