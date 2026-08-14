def eliminar_valores(lista1,lista2):
    i = 0
    while i < len(lista1):
        if lista1[i] in lista2:
            lista1.pop(i)
        else:
            i +=1
    return lista1

def main():
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