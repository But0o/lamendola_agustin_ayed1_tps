def cargar_lista() -> list[int]:
    """
    contrato

    Arma una lista con los números que ingresa el usuario, hasta que
    indica que no hay más para cargar.

    pre: no recibe parametros, se ingresan por teclado numeros enteros, finalizando con -1
    post: devuelve una lista con los numeros ingresados, sin incluir el -1
    """
    lista = []

    numero = int(input("Ingrese un numero (Finalizar la carga = -1): "))
    while numero != -1:
        lista.append(numero)
        numero = int(input("Ingrese un numero (Finalizar la carga = -1): "))

    return lista


def buscar_elementos(lista: list[int]) -> None:
    """
    contrato

    Muestra la posición de los números que pide el usuario. Si un
    número no está en la lista avisa del error, y al tercer error
    aborta la búsqueda.

    pre: lista es una lista de numeros enteros
    post: informa la posicion de cada numero ingresado usando index; finaliza al ingresar -1 o al detectar el tercer error
    """
    errores = 0

    while errores < 3:
        numero = int(input("Ingrese un numero a buscar (Finalizar = -1): "))
        if numero == -1:
            return
        try:
            print(f"El numero {numero} esta en la posicion {lista.index(numero)}")
        except ValueError:
            print(f"Error: el numero {numero} no pertenece a la lista")
            errores += 1

    print("Se aborto el proceso por llegar al tercer error")


def main() -> None:
    lista = cargar_lista()

    buscar_elementos(lista)


if __name__ == "__main__":
    main()
