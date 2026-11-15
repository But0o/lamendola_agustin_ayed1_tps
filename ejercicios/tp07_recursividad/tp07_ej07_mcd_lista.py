def mcd(x: int, y: int) -> int:
    """
    contrato

    Calcula el maximo comun divisor de dos numeros usando las propiedades
    MCD(X, X) = X, MCD(X, Y) = MCD(Y, X) y MCD(X, Y) = MCD(X - Y, Y) si X > Y.

    pre: x e y son numeros enteros positivos
    post: devuelve el maximo comun divisor de x e y
    """
    if x == y:
        return x

    if x > y:
        return mcd(x - y, y)

    return mcd(y, x)


def mcd_lista(numeros: list[int]) -> int:
    """
    contrato

    Calcula el maximo comun divisor de todos los elementos de una lista,
    sabiendo que MCD(X, Y, Z) = MCD(MCD(X, Y), Z).

    pre: numeros es una lista no vacia de enteros positivos
    post: devuelve el maximo comun divisor de todos los elementos de numeros
    """
    if len(numeros) == 1:
        return numeros[0]

    return mcd(mcd_lista(numeros[:-1]), numeros[-1])


def main() -> None:
    numeros = [48, 36, 120, 84]

    print(f"El MCD de {numeros} es {mcd_lista(numeros)}")


if __name__ == "__main__":
    main()
