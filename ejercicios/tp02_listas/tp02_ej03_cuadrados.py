def lista_cuadrada(n: int) -> list[int]:
    """
    contrato

    Arma una lista con el cuadrado de cada número entre 1 y N.

    pre: n es un numero entero positivo
    post: devuelve una lista con los cuadrados de los numeros entre 1 y n, ambos incluidos
    """
    lista = []

    for i in range(1,n +1):
        numero_cuadrado = pow(i,2)
        lista.append(numero_cuadrado)
    return lista

def main() -> None:
    n = int(input("Ingrese un numeron: "))
    cuadrado = lista_cuadrada(n)
    print(cuadrado)

if __name__ == "__main__":
    main()
