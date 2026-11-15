def producto(a: int, b: int) -> int:
    """
    contrato

    Calcula el producto de dos numeros enteros por sumas sucesivas.

    pre: a y b son numeros enteros
    post: devuelve a * b, calculado sumando a, b veces
    """
    if b == 0:
        return 0

    if b < 0:
        return -producto(a, -b)

    return a + producto(a, b - 1)


def main() -> None:
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))

    print(f"El producto de {a} y {b} es {producto(a, b)}")


if __name__ == "__main__":
    main()
