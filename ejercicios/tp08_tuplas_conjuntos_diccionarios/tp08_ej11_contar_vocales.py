def contarvocales(palabra: str) -> dict[str, int]:
    """
    contrato

    Cuenta cuántas veces aparece cada vocal en una palabra, sin
    diferenciar mayúsculas ni vocales con tilde.

    pre: palabra es una cadena de caracteres
    post: devuelve un diccionario cuyas claves son las vocales y sus valores la cantidad de cada una en palabra
    """
    acentos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for letra in palabra.lower():
        letra = acentos.get(letra, letra)
        if letra in vocales:
            vocales[letra] += 1

    return vocales


def main() -> None:
    frase = input("Ingrese una frase: ")

    for palabra in frase.split():
        print(f"{palabra}: {contarvocales(palabra)}")


if __name__ == "__main__":
    main()
