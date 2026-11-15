def suma_naturales(n: int) -> int:
    """
    contrato

    Calcula la suma de los N primeros numeros naturales.

    pre: n es un numero entero mayor o igual que 0
    post: devuelve 1 + 2 + ... + n (0 si n es 0)
    """
    if n == 0:
        return 0

    return n + suma_naturales(n - 1)


def main() -> None:
    n = int(input("Ingrese la cantidad de numeros naturales a sumar: "))

    print(f"La suma de los {n} primeros numeros naturales es {suma_naturales(n)}")


if __name__ == "__main__":
    main()
