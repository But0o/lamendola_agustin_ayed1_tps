def buscarclave(diccionario: dict, valor: object) -> list:
    """
    contrato

    Busca todas las claves de un diccionario que apuntan a un mismo
    valor.

    pre: diccionario es un diccionario cualquiera y valor es el dato a buscar
    post: devuelve una lista con las claves que mapean a valor; si no hay ninguna, la lista queda vacia
    """
    return [clave for clave, dato in diccionario.items() if dato == valor]


def main() -> None:
    diccionario = {"a": 1, "b": 2, "c": 1, "d": 3}
    print(f"Diccionario: {diccionario}")

    valor = int(input("Ingrese un valor a buscar: "))

    print(buscarclave(diccionario, valor))


if __name__ == "__main__":
    main()
