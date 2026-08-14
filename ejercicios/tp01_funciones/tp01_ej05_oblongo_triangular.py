OBLONGO = lambda n: (4 * n + 1) ** 0.5 == int((4 * n + 1) ** 0.5)
TRIANGULAR = lambda n: (8 * n + 1) ** 0.5 == int((8 * n + 1) ** 0.5)

def main():
    numero = int(input("Ingrese un número entero: "))

    resultado_oblongo = OBLONGO(numero)
    resultado_triangular = TRIANGULAR(numero)

    print(f"El numero ingresado es Oblongo? {resultado_oblongo}")
    print(f"El numero ingresado es Triangular? {resultado_triangular}")

if __name__ == "__main__":
    main()

