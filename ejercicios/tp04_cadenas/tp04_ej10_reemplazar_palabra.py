def es_palabra_completa(cadena: str, inicio: int, fin: int) -> bool:
    """
    contrato

    Revisa si el pedazo de cadena indicado es una palabra completa, o
    sea que no tiene letras ni números pegados antes ni después.

    pre: cadena es una cadena de caracteres, inicio y fin son posiciones validas con inicio < fin <= len(cadena)
    post: devuelve True si el fragmento entre inicio y fin (sin incluir fin) es una palabra completa, False en caso contrario
    """
    if inicio > 0 and cadena[inicio - 1].isalnum():
        return False
    if fin < len(cadena) and cadena[fin].isalnum():
        return False

    return True


def reemplazar_palabra(cadena: str, palabra: str, reemplazo: str) -> tuple[str, int]:
    """
    contrato

    Cambia todas las apariciones de una palabra por otra dentro de una
    cadena, sin tocar los fragmentos de otras palabras.

    pre: cadena es una cadena de caracteres, palabra es una cadena no vacia y reemplazo es una cadena de caracteres
    post: devuelve una tupla con la cadena obtenida y la cantidad de reemplazos realizados
    """
    resultado = ""
    cantidad = 0
    copiado_hasta = 0

    posicion = cadena.find(palabra)
    while posicion != -1:
        fin = posicion + len(palabra)
        if es_palabra_completa(cadena, posicion, fin):
            resultado += cadena[copiado_hasta:posicion] + reemplazo
            copiado_hasta = fin
            cantidad += 1
            posicion = cadena.find(palabra, fin)
        else:
            posicion = cadena.find(palabra, posicion + 1)

    resultado += cadena[copiado_hasta:]

    return resultado, cantidad


def main() -> None:
    cadena = input("Ingrese una cadena: ")
    palabra = input("Ingrese la palabra a reemplazar: ")
    reemplazo = input("Ingrese la palabra nueva: ")

    resultado, cantidad = reemplazar_palabra(cadena, palabra, reemplazo)

    print(resultado)
    print(f"Cantidad de reemplazos: {cantidad}")


if __name__ == "__main__":
    main()
