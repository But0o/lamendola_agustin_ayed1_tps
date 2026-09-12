import random as rn

def lista_random(n: int) -> list[int]:
    """
    contrato

    Genera una lista con una cantidad determinada de números al azar
    entre 1 y 100.

    pre: n es un numero entero positivo
    post: devuelve una lista de n numeros aleatorios entre 1 y 100
    """
    lista = [rn.randint(1,100) for i in range(n)]
    return lista
    
def elementos_repeditos(lista: list) -> bool:
    """
    contrato

    Revisa si dentro de una lista hay algún valor que aparezca más
    de una vez.

    pre: lista es una lista cualquiera
    post: devuelve True si la lista contiene al menos un elemento repetido, False en caso contrario; no modifica la lista
    """
    for i in range(len(lista)):
        for j in range(i +1 , len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def lista_unica(lista_repetida: list) -> list:
    """
    contrato

    Arma una nueva lista quedándose solo con los valores que no
    estén repetidos, sin importar el orden.

    pre: lista_repetida es una lista cualquiera
    post: devuelve una nueva lista con los elementos unicos de lista_repetida, sin importar el orden
    """
    lista_nueva = []

    for n in lista_repetida:
        if n not in lista_nueva:
            lista_nueva.append(n)
    
    return lista_nueva

def main() -> None:
    n = int(input("Ingresar un numero para la cantidad de numeros de la lista: "))

    lista = lista_random(n)

    print("Lista generada:")
    print(lista)

    elemento_repetido = elementos_repeditos(lista)
    print(elemento_repetido)

    #lista_repetida = [10, 20, 10, 30, 20] Sirve para prueba mas rapida
    lista_repetida = lista
    lista_sin_repetidos = lista_unica(lista_repetida)
    print(lista_sin_repetidos)

if __name__ == "__main__":
    main()
