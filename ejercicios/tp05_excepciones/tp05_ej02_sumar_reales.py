def sumar_reales(cadena1: str, cadena2: str) -> float:
    """
    contrato

    Suma dos números reales que vienen escritos como cadenas de
    caracteres.

    pre: cadena1 y cadena2 son cadenas de caracteres
    post: devuelve la suma de ambos valores como numero real, o -1 si alguna de las cadenas no contiene un numero valido
    """
    try:
        return float(cadena1) + float(cadena2)
    except ValueError:
        return -1


def main() -> None:
    cadena1 = input("Ingrese el primer numero: ")
    cadena2 = input("Ingrese el segundo numero: ")

    print(sumar_reales(cadena1, cadena2))


if __name__ == "__main__":
    main()
