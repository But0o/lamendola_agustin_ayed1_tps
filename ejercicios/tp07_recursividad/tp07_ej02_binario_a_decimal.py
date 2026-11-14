def binario_a_decimal(binario: int) -> int:
    """
    contrato

    Convierte un numero binario a base decimal.

    pre: binario es un numero entero no negativo formado solo por ceros y unos
    post: devuelve el valor decimal de binario
    """
    if binario == 0:
        return 0

    return binario % 10 + 2 * binario_a_decimal(binario // 10)


def main() -> None:
    binario = int(input("Ingrese un numero binario: "))

    print(f"El numero en decimal es {binario_a_decimal(binario)}")


if __name__ == "__main__":
    main()
