def cantidad_digitos(numero: int) -> int:
    """
    contrato

    Calcula la cantidad de digitos de un numero entero, sin usar cadenas
    de caracteres.

    pre: numero es un numero entero
    post: devuelve la cantidad de digitos de numero (el 0 tiene un digito)
    """
    if numero < 0:
        return cantidad_digitos(-numero)

    if numero < 10:
        return 1

    return 1 + cantidad_digitos(numero // 10)


def main() -> None:
    numero = int(input("Ingrese un numero entero: "))

    print(f"El numero tiene {cantidad_digitos(numero)} digitos")


if __name__ == "__main__":
    main()
