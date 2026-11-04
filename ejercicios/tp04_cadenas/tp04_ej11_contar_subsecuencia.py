def contar_subsecuencia(cadena: str, subcadena: str) -> int:
    """
    contrato

    Cuenta cuántas veces aparece una subcadena dentro de una cadena sin
    importar mayúsculas ni minúsculas. Sus caracteres pueden estar
    separados, pero tienen que aparecer en el mismo orden.

    pre: cadena es una cadena de caracteres y subcadena es una cadena no vacia
    post: devuelve la cantidad de veces que se encuentra subcadena dentro de cadena, sin que un mismo caracter se use en dos coincidencias
    """
    cadena = cadena.lower()
    subcadena = subcadena.lower()

    cantidad = 0
    posicion = 0

    for caracter in cadena:
        if caracter == subcadena[posicion]:
            posicion += 1
            if posicion == len(subcadena):
                cantidad += 1
                posicion = 0

    return cantidad


def main() -> None:
    cadena = input("Ingrese la cadena: ")
    subcadena = input("Ingrese la subcadena: ")

    print(f"Cantidad encontrada: {contar_subsecuencia(cadena, subcadena)}")


if __name__ == "__main__":
    main()
