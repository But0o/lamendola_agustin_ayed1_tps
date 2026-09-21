import random as rn
from typing import List



def matriz_random(n: int) -> List[List[int]]:
    """
    Contrato: dado un entero n, construye y devuelve una matriz cuadrada de
    n x n rellena con números enteros al azar dentro del intervalo [0, n**2],
    sin que ningún número se repita en toda la matriz.

    Precondición: n > 0. El intervalo [0, n**2] tiene n**2 + 1 valores
    posibles, uno más que la cantidad de celdas (n**2), por lo que siempre
    hay suficientes números distintos disponibles.
    Postcondición: el resultado es una lista de n listas, cada una con n
    elementos enteros; todos los elementos de la matriz son distintos entre
    sí, y cada uno está dentro del rango [0, n**2].
    """
    matriz = []
    numeros_sin_repetir = set()

    for i in range(n):
        fila = []
        for columna in range(n):
            numero = rn.randint(0, n**2)
            while numero in numeros_sin_repetir:
                numero = rn.randint(0, n**2)
            numeros_sin_repetir.add(numero)
            fila.append(numero)
        matriz.append(fila)
    return matriz

def mostar_matriz(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz, la muestra por pantalla, fila por fila.

    Precondición: matriz es una lista de listas.
    Postcondición: se imprime una línea por cada fila de matriz, en el
    orden en que aparecen. No modifica matriz.
    """
    for fila in matriz: print(fila)



def main():
    n = int(input("Ingrese un numero para la dimencion de la matriz: "))
    matriz = matriz_random(n)
    mostar_matriz(matriz)


if __name__ == "__main__":
    main()