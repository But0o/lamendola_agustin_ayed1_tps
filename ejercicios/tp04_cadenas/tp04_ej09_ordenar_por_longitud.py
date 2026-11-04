SIGNOS: str = ".,;:!?¡¿()\"'-"


def longitud_sin_signos(palabra: str) -> int:
    """
    contrato

    Cuenta los caracteres de una palabra dejando afuera los signos de
    puntuación.

    pre: palabra es una cadena de caracteres
    post: devuelve la cantidad de caracteres de palabra que no son signos de puntuacion
    """
    longitud = 0

    for caracter in palabra:
        if caracter not in SIGNOS:
            longitud += 1

    return longitud


def ordenar_por_longitud(cadena: str) -> str:
    """
    contrato

    Ordena las palabras de una cadena de la más corta a la más larga,
    sin contar los signos de puntuación al medirlas pero dejándolos
    en la cadena final.

    pre: cadena es una cadena de caracteres con palabras separadas por uno o mas espacios
    post: devuelve otra cadena con las palabras ordenadas segun su longitud, con un espacio entre cada una
    """
    palabras = cadena.split()
    palabras.sort(key=longitud_sin_signos)

    return " ".join(palabras)


def main() -> None:
    cadena = input("Ingrese una cadena: ")

    print(ordenar_por_longitud(cadena))


if __name__ == "__main__":
    main()
