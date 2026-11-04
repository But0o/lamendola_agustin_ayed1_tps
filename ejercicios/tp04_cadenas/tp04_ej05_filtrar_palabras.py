def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """
    contrato

    Se queda con las palabras de una frase que tengan al menos una
    cierta cantidad de caracteres, recorriéndolas con un ciclo.

    pre: frase es una cadena de caracteres y n es un numero entero
    post: devuelve una cadena con las palabras de frase que tienen n o mas caracteres, separadas por un espacio
    """
    palabras = []

    for palabra in frase.split():
        if len(palabra) >= n:
            palabras.append(palabra)

    return " ".join(palabras)


def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    contrato

    Se queda con las palabras de una frase que tengan al menos una
    cierta cantidad de caracteres, usando una lista por comprensión.

    pre: frase es una cadena de caracteres y n es un numero entero
    post: devuelve una cadena con las palabras de frase que tienen n o mas caracteres, separadas por un espacio
    """
    palabras = [palabra for palabra in frase.split() if len(palabra) >= n]

    return " ".join(palabras)


def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    contrato

    Se queda con las palabras de una frase que tengan al menos una
    cierta cantidad de caracteres, usando la función filter().

    pre: frase es una cadena de caracteres y n es un numero entero
    post: devuelve una cadena con las palabras de frase que tienen n o mas caracteres, separadas por un espacio
    """
    palabras = filter(lambda palabra: len(palabra) >= n, frase.split())

    return " ".join(palabras)


def main() -> None:
    frase = input("Ingrese una frase: ")
    n = int(input("Ingrese la cantidad minima de caracteres: "))

    # Punto A
    print("Punto A")
    print(filtrar_palabras_ciclos(frase, n))
    # Punto B
    print("Punto B")
    print(filtrar_palabras_comprension(frase, n))
    # Punto C
    print("Punto C")
    print(filtrar_palabras_filter(frase, n))


if __name__ == "__main__":
    main()
