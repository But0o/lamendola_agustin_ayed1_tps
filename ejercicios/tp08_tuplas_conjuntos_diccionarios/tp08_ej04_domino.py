def encajan(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """
    contrato

    Indica si dos fichas de dominó encajan, o sea si comparten al menos
    un mismo número.

    pre: ficha1 y ficha2 son tuplas de dos numeros enteros
    post: devuelve True si las fichas encajan, False en caso contrario
    """
    return len(set(ficha1) & set(ficha2)) > 0


def main() -> None:
    ficha1 = (int(input("Ficha 1, primer numero: ")), int(input("Ficha 1, segundo numero: ")))
    ficha2 = (int(input("Ficha 2, primer numero: ")), int(input("Ficha 2, segundo numero: ")))

    print(encajan(ficha1, ficha2))


if __name__ == "__main__":
    main()
