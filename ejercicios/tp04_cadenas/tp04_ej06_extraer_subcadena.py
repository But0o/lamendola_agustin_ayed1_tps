def extraer_con_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    contrato

    Saca un pedazo de una cadena, indicando desde dónde empieza y
    cuántos caracteres tiene, usando rebanadas.

    pre: cadena es una cadena de caracteres, posicion y cantidad son enteros mayores o iguales a 0
    post: devuelve la subcadena de cadena que empieza en posicion y tiene hasta cantidad caracteres
    """
    return cadena[posicion:posicion + cantidad]


def extraer_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    contrato

    Saca un pedazo de una cadena, indicando desde dónde empieza y
    cuántos caracteres tiene, armándolo caracter por caracter.

    pre: cadena es una cadena de caracteres, posicion y cantidad son enteros mayores o iguales a 0
    post: devuelve la subcadena de cadena que empieza en posicion y tiene hasta cantidad caracteres; no utiliza rebanadas
    """
    subcadena = ""
    i = posicion

    while i < posicion + cantidad and i < len(cadena):
        subcadena += cadena[i]
        i += 1

    return subcadena


def main() -> None:
    cadena = input("Ingrese una cadena: ")
    posicion = int(input("Ingrese la posicion: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))

    # Punto A
    print("Punto A")
    print(extraer_con_rebanadas(cadena, posicion, cantidad))
    # Punto B
    print("Punto B")
    print(extraer_sin_rebanadas(cadena, posicion, cantidad))


if __name__ == "__main__":
    main()
