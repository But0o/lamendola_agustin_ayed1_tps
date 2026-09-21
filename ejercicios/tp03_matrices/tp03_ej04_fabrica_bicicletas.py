import random as rn
from typing import List, Tuple

DIAS_SEMANA = 6

def matriz_fabrica(n: int) -> List[List[int]]:
    """
    Contrato: dado un entero n, construye y devuelve una matriz de n
    fábricas por 6 días de la semana, rellena con números enteros al azar
    que representan la cantidad de bicicletas producidas.

    Precondición: n > 0.
    Postcondición: el resultado es una lista de n listas, cada una con
    DIAS_SEMANA (6) elementos enteros, cada uno dentro del rango [0, 150].
    """
    matriz = []
    for i in range(n):
        fila = []
        for j in range(DIAS_SEMANA):
            cant_bici = rn.randint(0, 150)
            fila.append(cant_bici)
        matriz.append(fila)
    return matriz


def cant_total_x_fabrica(matriz: List[List[int]]) -> None:
    """
    Contrato: dada la matriz de producción, muestra por pantalla el total
    de bicicletas fabricadas por cada fábrica en la semana.

    Precondición: matriz es una lista de listas de enteros, no vacía.
    Postcondición: se imprime una línea por cada fábrica, con el número de
    fábrica (base 1) y la suma de los valores de su fila. No modifica
    matriz.
    """
    for fila in range(len(matriz)): print(f"La suma de la fabrica {fila+1} es de {sum(matriz[fila])}")


def maximo_facricado(matriz: List[List[int]]) -> Tuple[int, int, int]:
    """
    Contrato: dada la matriz de producción, determina cuál fue el valor
    más alto producido por una fábrica en un solo día, junto con la
    fábrica y el día donde ocurrió.

    Precondición: matriz es una lista de listas de enteros, no vacía, con
    DIAS_SEMANA columnas en cada fila.
    Postcondición: devuelve una tupla (i, j, maximo), donde maximo es el
    mayor valor de toda la matriz, e i, j son los índices de fila y
    columna (fábrica y día) de la primera aparición de ese valor. No
    modifica matriz.
    """
    lista = [numero for fila in matriz for numero in fila]
    maximo = max(lista)
    for i in range(len(matriz)):
            for j in range(DIAS_SEMANA):  
                if matriz[i][j] == maximo:
                    return i,j, maximo



def dia_mas_producido(matriz: List[List[int]]) -> Tuple[int, int]:
    """
    Contrato: dada la matriz de producción, determina qué día de la
    semana tuvo la mayor producción combinando todas las fábricas.

    Precondición: matriz es una lista de listas de enteros, no vacía, con
    DIAS_SEMANA columnas en cada fila.
    Postcondición: devuelve una tupla (mejor_dia, mejor_suma), donde
    mejor_dia es el índice de columna (0 a 5) cuya suma total (sumando
    todas las filas) es la más alta, y mejor_suma es esa suma. No
    modifica matriz.
    """
    mejor_suma = -1
    mejor_dia = 0
    for columna in range(DIAS_SEMANA):
        suma = 0
        for fila in range(len(matriz)):
            suma += matriz[fila][columna]
        if suma > mejor_suma:
            mejor_suma = suma
            mejor_dia = columna
    return mejor_dia,mejor_suma


def produccion_minima(matriz: List[List[int]]) -> List[int]:
    """
    Contrato: dada la matriz de producción, calcula la menor cantidad
    producida en un día por cada fábrica.

    Precondición: matriz es una lista de listas de enteros, cada fila con
    al menos un elemento.
    Postcondición: el resultado es una lista con la misma cantidad de
    elementos que filas tiene matriz, donde cada elemento es el valor
    mínimo de la fila correspondiente, en el mismo orden. No modifica
    matriz.
    """
    return [min(fila) for fila in matriz]
    

def mostar_matriz(matriz: List[List[int]]) -> None:
    """
    Contrato: dada una matriz, la muestra por pantalla, fila por fila.

    Precondición: matriz es una lista de listas.
    Postcondición: se imprime una línea por cada fila de matriz, en el
    orden en que aparecen. No modifica matriz.
    """
    for fila in matriz: print(fila)


def main():
    # Punto A
    print("Punto A")
    n = int(input("Ingrese el numero de fabricas para la matriz: "))
    matriz = matriz_fabrica(n)
    mostar_matriz(matriz)
    print("------------------------")
    # Punto B
    print("Punto B")
    cant_total_x_fabrica(matriz)
    print("------------------------")
    # Punto C
    print("Punto C")
    i,j, maximo = maximo_facricado(matriz)
    print(f"La fabrica que fabrico el maximo historico es la fabrica numero {i+1} fabricando un total de {maximo} bicis, el dia {j} de la semana ")
    print("------------------------")
    # Punto D
    print("Punto D")
    mejor_dia,mejor_suma = dia_mas_producido(matriz)
    print(f"El dia que mas bicis se fabricaron juntando todas las fabicras fue el dia {mejor_dia} fabricando un total de {mejor_suma} bicis")
    print("------------------------")
    # Punto F
    print("Punto F")
    minimo = produccion_minima(matriz)
    for i in range(len(minimo)):
        print(f"La fabrica {i+1} fabrico {minimo[i]} bicis")
    print("------------------------")  
    
if __name__ == "__main__":
    main()
