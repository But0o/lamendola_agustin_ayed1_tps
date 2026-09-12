from typing import Callable

OBLONGO: Callable[[int], bool] = lambda n: (4 * n + 1) ** 0.5 == int((4 * n + 1) ** 0.5)
"""
contrato

Indica si un número se puede formar multiplicando dos números
naturales consecutivos, por ejemplo 2 y 3.

pre: n es un numero entero
post: devuelve True si n es oblongo (producto de dos naturales consecutivos), False en caso contrario
"""

TRIANGULAR: Callable[[int], bool] = lambda n: (8 * n + 1) ** 0.5 == int((8 * n + 1) ** 0.5)
"""
contrato

Indica si un número se puede formar sumando una serie de números
naturales consecutivos que empieza en 1.

pre: n es un numero entero
post: devuelve True si n es triangular (suma de naturales consecutivos desde 1), False en caso contrario
"""

def main() -> None:
    numero = int(input("Ingrese un número entero: "))

    resultado_oblongo = OBLONGO(numero)
    resultado_triangular = TRIANGULAR(numero)

    print(f"El numero ingresado es Oblongo? {resultado_oblongo}")
    print(f"El numero ingresado es Triangular? {resultado_triangular}")

if __name__ == "__main__":
    main()
