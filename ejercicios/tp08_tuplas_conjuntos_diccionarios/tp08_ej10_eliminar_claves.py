def eliminarclaves(diccionario: dict, claves: list) -> tuple[dict, int]:
    """
    contrato

    Borra de un diccionario todas las claves que aparecen en una lista,
    contando cuántas se pudieron eliminar.

    pre: diccionario es un diccionario cualquiera y claves es una lista de claves
    post: modifica diccionario quitando las claves de la lista y devuelve una tupla con diccionario modificado y la cantidad de claves eliminadas
    """
    cantidad = 0

    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            cantidad += 1

    return diccionario, cantidad


def main() -> None:
    diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
    claves = ["a", "c", "z"]

    print(f"Diccionario: {diccionario}")
    print(f"Claves a eliminar: {claves}")

    diccionario, cantidad = eliminarclaves(diccionario, claves)

    print(f"Diccionario modificado: {diccionario}")
    print(f"Claves eliminadas: {cantidad}")


if __name__ == "__main__":
    main()
