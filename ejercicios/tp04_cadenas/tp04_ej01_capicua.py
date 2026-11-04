def es_capicua(cadena: str) -> bool:
    """
    contrato

    Revisa si una cadena se lee igual de izquierda a derecha que de
    derecha a izquierda, comparando sus caracteres de a pares.

    pre: cadena es una cadena de caracteres
    post: devuelve True si cadena es capicua, False en caso contrario; no utiliza cadenas auxiliares ni rebanadas
    """
    izquierda = 0
    derecha = len(cadena) - 1

    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True


def main() -> None:
    cadena = input("Ingrese una cadena: ")

    if es_capicua(cadena):
        print("La cadena es capicua")
    else:
        print("La cadena no es capicua")


if __name__ == "__main__":
    main()
