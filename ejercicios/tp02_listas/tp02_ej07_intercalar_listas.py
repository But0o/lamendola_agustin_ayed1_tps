def intercalar(lista1,lista2):
    i = 0

    while i < len(lista2):
        posicion = i * 2 + 1
        lista1[posicion:posicion] = [lista2[i]]
        i += 1
    return lista1


def main():

    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]

    lista = intercalar(lista1,lista2)

    print(lista)



if __name__ == "__main__":
    main()