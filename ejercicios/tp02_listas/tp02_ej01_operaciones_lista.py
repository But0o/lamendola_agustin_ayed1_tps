import random as rn

def cargar_lista() -> list[int]:
    """
    contrato

    Genera una lista con una cantidad al azar de números de cuatro
    dígitos, también elegidos al azar.

    pre: no recibe parametros
    post: devuelve una lista con una cantidad al azar (entre 10 y 99) de numeros de cuatro digitos generados al azar
    """
    lista = []

    cantidad = rn.randint(10,99)

    for i in range(cantidad):
        numero = rn.randint(1000 , 9999)
        lista.append(numero)

    return lista

def producto_lista(lista: list[int]) -> int:
    """
    contrato

    Multiplica entre sí todos los números de una lista y devuelve el
    resultado.

    pre: lista es una lista de numeros
    post: devuelve el producto de todos los elementos de la lista
    """

    producto = 1

    for numero in lista:
        producto *= numero

    return producto

def eliminar_valor(lista: list[int], n: int) -> list[int]:
    """
    contrato

    Recorre una lista y devuelve una copia sin ninguna aparición de
    un valor determinado.

    pre: lista es una lista de numeros, n es el valor a eliminar
    post: devuelve una nueva lista sin ninguna aparicion del valor n, sin usar listas auxiliares para el filtrado
    """
    i = 0
    lista_eliminada = lista.copy()

    while i < len(lista_eliminada):
        if lista_eliminada[i] == n:
            lista_eliminada.pop(i)
        else:
            i += 1
    return lista_eliminada

def lista_capicua(lista: list) -> bool:
    """
    contrato

    Verifica si una lista se lee igual de adelante hacia atrás que
    de atrás hacia adelante.

    pre: lista es una lista cualquiera
    post: devuelve True si la lista es capicua (se lee igual de izquierda a derecha que de derecha a izquierda), False en caso contrario
    """
    for i in range(len(lista)):
        if lista[i] != lista[i-1]:
            return False
        else:
            return True


def main() -> None:
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
