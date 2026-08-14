def lista_cuadrada(n):
    lista = []

    for i in range(1,n +1):
        numero_cuadrado = pow(i,2)
        lista.append(numero_cuadrado)
    return lista

def main():
    n = int(input("Ingrese un numeron: "))
    cuadrado = lista_cuadrada(n)
    print(cuadrado)

if __name__ == "__main__":
    main()