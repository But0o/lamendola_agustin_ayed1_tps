import random as rn

def cargar_lista():
    lista = []

    cantidad = rn.randint(10,99)

    for i in range(cantidad):
        numero = rn.randint(1000 , 9999)
        lista.append(numero)

    return lista

def producto_lista(lista):

    producto = 1

    for numero in lista:
        producto *= numero

    return producto

def eliminar_valor(lista,n):
    i = 0
    lista_eliminada = lista.copy()

    while i < len(lista_eliminada):
        if lista_eliminada[i] == n:
            lista_eliminada.pop(i)
        else:
            i += 1
    return lista_eliminada

def lista_capicua(lista):
    for i in range(len(lista)):
        if lista[i] != lista[i-1]:
            return False
        else:
            return True


def main():
    # Punto A
    lista = [50, 17, 91, 17, 50]  #lista de pruebas
    #lista = cargar_lista()
    print("Lista generada:")
    print(lista)

    # Punto B
    producto = producto_lista(lista)
    
    print("Producto de los elementos:")
    print(producto)

    # Punto C
    n = int(input("Ingrese el número que desea eliminar: "))
    lista_eliminada = eliminar_valor(lista, n)

    print("Lista después de eliminar el valor:")
    print(lista_eliminada)


    # Punto D
    print(f"La lista es capicua? {lista}")
    print(lista_capicua(lista))


if __name__ == "__main__":
    main()