def ultimos_caracteres(cadena: str, n: int) -> str:
    """
    contrato

    Devuelve el final de una cadena, con la cantidad de caracteres
    que se pida.

    pre: cadena es una cadena de caracteres y n es un entero entre 0 y la longitud de cadena
    post: devuelve una subcadena con los ultimos n caracteres de cadena
    """
    return cadena[len(cadena) - n:]


def main() -> None:
    cadena = input("Ingrese una cadena: ")
    n = int(input("Ingrese la cantidad de caracteres: "))

    print(ultimos_caracteres(cadena, n))


if __name__ == "__main__":
    main()
