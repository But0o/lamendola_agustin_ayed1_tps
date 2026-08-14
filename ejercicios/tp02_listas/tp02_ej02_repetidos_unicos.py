import random as rn

def lista_random(n):
    lista = [rn.randint(1,100) for i in range(n)]
    return lista
    
def elementos_repeditos(lista):
    for i in range(len(lista)):
        for j in range(i +1 , len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def lista_unica(lista_repetida):
    lista_nueva = []

    for n in lista_repetida:
        if n not in lista_nueva:
            lista_nueva.append(n)
    
    return lista_nueva

def main():
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