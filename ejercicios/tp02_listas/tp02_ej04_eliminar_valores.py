def eliminar_valores(lista1: list, lista2: list) -> list:
    """
    contrato

    Recorre una lista y le va sacando todos los valores que también
    aparezcan en una segunda lista.

    pre: lista1 es la lista de numeros enteros a modificar, lista2 es la lista de valores a eliminar
    post: modifica lista1 eliminando todos los valores que tambien esten en lista2 y devuelve la lista1 modificada
    """
    i = 0
    while i < len(lista1):
        if lista1[i] in lista2:
            lista1.pop(i)
        else:
            i +=1
    return lista1

def main() -> None:
    lista1 = [10, 20, 30, 40, 20, 50, 30]
    lista2 = [20, 30]


    print("Esta es la lista original")
    print(lista1)

    print("Esta es la lista de los que se tiene que elimiar")
    print(lista2)

    print("Esta es la lista despues de eliminar los datos")
    print(eliminar_valores(lista1,lista2))


if __name__ == "__main__":
    main()
