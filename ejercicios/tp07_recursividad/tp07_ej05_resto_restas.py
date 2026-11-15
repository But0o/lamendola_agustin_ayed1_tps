def resto(dividendo: int, divisor: int) -> int:
    """
    contrato

    Calcula el resto de la division de dos numeros enteros, utilizando
    restas sucesivas.

    pre: dividendo es un entero mayor o igual que 0 y divisor es un entero mayor que 0
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
