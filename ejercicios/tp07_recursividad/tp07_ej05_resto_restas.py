def resto(dividendo: int, divisor: int) -> int:
    """
    contrato

    Calcula el resto de la division entera de dos numeros, utilizando
    restas sucesivas.

    pre: dividendo es un entero no negativo y divisor es un entero positivo
    post: devuelve el resto de dividir dividendo por divisor
    """
    if dividendo < divisor:
        return dividendo

    return resto(dividendo - divisor, divisor)


def main() -> None:
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    print(f"El resto de dividir {dividendo} por {divisor} es {resto(dividendo, divisor)}")


if __name__ == "__main__":
    main()
