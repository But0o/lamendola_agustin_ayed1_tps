import random as rn
from typing import List, Tuple


def cargar_sala(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz existente (todos ceros), la llena con
    valores al azar (0 o 1) simulando butacas ya reservadas.

    Precondición: matriz es una lista de listas, no vacía, con al menos
    una fila y una columna.
    Postcondición: cada posición de matriz queda con 0 o 1, elegido al
    azar. Modifica matriz in-place.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = rn.randint(0, 1)


def mostrar_butacas(matriz: List[List[int]]) -> None:
    """
    Contrato: dada la matriz de la sala, muestra por pantalla el estado
    de cada butaca usando símbolos (🟩 libre, 🟥 ocupada).

    Precondición: matriz contiene únicamente los valores 0 o 1 en cada
    posición.
    Postcondición: se imprime una línea por fila, con un símbolo por
    butaca (🟩 si el valor es 0, 🟥 si es 1). No modifica matriz.
    """
    for fila in matriz:
        for disponibilidad in fila:
            if disponibilidad == 0:
                print("🟩", end=" ")
            else:
                print("🟥", end=" ")
        print()


def butacas_libres(matriz: List[List[int]]) -> int:
    """
    Contrato: dada la matriz de la sala, cuenta cuántas butacas están
    libres en total.

    Precondición: matriz contiene únicamente los valores 0 o 1.
    Postcondición: devuelve la cantidad total de posiciones con valor 0
    en toda la matriz. No modifica matriz.
    """
    butacas = [numero for fila in matriz for numero in fila]
    libres = butacas.count(0)
    return libres


def reservar(matriz: List[List[int]], fila: int, columna: int) -> bool:
    """
    Contrato: dada la matriz, una fila y una columna, intenta reservar
    esa butaca puntual si está disponible.

    Precondición: 0 <= fila < len(matriz) y 0 <= columna < len(matriz[fila]).
    Postcondición: si matriz[fila][columna] era 0, pasa a valer 1 y
    devuelve True. Si ya era 1, no modifica nada y devuelve False.
    """
    if matriz[fila][columna] == 0:
        matriz[fila][columna] = 1
        return True
    else:
        return False


def buscar_contiguas(matriz: List[List[int]]) -> Tuple[int, int]:
    """
    Contrato: dada la matriz de la sala, busca la secuencia más larga de
    butacas libres consecutivas dentro de una misma fila, y devuelve
    dónde empieza.

    Precondición: matriz contiene únicamente los valores 0 o 1, con al
    menos una fila y una columna.
    Postcondición: devuelve una tupla (i_mejor, j_mejor) con la fila y
    columna donde empieza la racha de ceros consecutivos más larga de
    toda la matriz (comparando solo dentro de cada fila, nunca cruzando
    entre filas distintas). No modifica matriz.
    """
    racha_mas_alta = 0
    i_mejor = 0
    j_mejor = 0

    for i in range(len(matriz)):
        racha_actual = 0
        inicio = 0
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                if racha_actual == 0:
                    inicio = j
                racha_actual += 1
                if racha_actual > racha_mas_alta:
                    racha_mas_alta = racha_actual
                    i_mejor = i
                    j_mejor = inicio
            else:
                racha_actual = 0
    return racha_mas_alta, i_mejor, j_mejor


def main():
    M = int(input("Ingrese un numero de butacas x fila: "))
    N = int(input("Ingrese un numero de filas: "))
    matriz = [[0 for _ in range(M)] for _ in range(N)]

    # Punto A
    print("PUNTO A")
    cargar_sala(matriz)
    print("Se cargo la matriz")
    print("------------------")
    # Punto B
    print("Punto B")
    print("🟩 -> Butaca Libre", "🟥 -> Butaca Ocupada")
    mostrar_butacas(matriz)
    print("------------------")
    # Punto C
    print("Punto C")
    fila = int(input("Ingrese numero de fila: "))
    columna = int(input("ingrese numero de butaca: "))
    print(reservar(matriz, fila, columna))
    mostrar_butacas(matriz)
    print("------------------")
    # Punto D
    print("Punto D")
    mejor_racha, i_mejor, j_mejor = buscar_contiguas(matriz)
    print(
        f"La mejor racha se butacas libre es de {mejor_racha} butacas, y emepzo en el indice {i_mejor},{j_mejor} de la matriz"
    )


if __name__ == "__main__":
    main()
