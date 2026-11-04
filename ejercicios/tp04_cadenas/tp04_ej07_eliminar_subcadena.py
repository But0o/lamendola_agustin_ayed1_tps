def eliminar_con_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    contrato

    Quita un pedazo de una cadena, indicando desde dónde empieza y
    cuántos caracteres tiene, usando rebanadas.

    pre: cadena es una cadena de caracteres, posicion y cantidad son enteros mayores o iguales a 0
    post: devuelve una cadena igual a cadena pero sin los cantidad caracteres que empiezan en posicion
    """
    return cadena[:posicion] + cadena[posicion + cantidad:]


def eliminar_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    contrato

    Quita un pedazo de una cadena, indicando desde dónde empieza y
    cuántos caracteres tiene, copiando solo los caracteres que quedan.

    pre: cadena es una cadena de caracteres, posicion y cantidad son enteros mayores o iguales a 0
    post: devuelve una cadena igual a cadena pero sin los cantidad caracteres que empiezan en posicion; no utiliza rebanadas
    """
    resultado = ""

    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            resultado += cadena[i]

    return resultado


def main() -> None:
    cadena = input("Ingrese una cadena: ")
    posicion = int(input("Ingrese la posicion: "))
    cantidad = int(input("Ingrese la cantidad de caracteres: "))

    # Punto A
    print("Punto A")
    print(eliminar_con_rebanadas(cadena, posicion, cantidad))
    # Punto B
    print("Punto B")
    print(eliminar_sin_rebanadas(cadena, posicion, cantidad))


if __name__ == "__main__":
    main()
