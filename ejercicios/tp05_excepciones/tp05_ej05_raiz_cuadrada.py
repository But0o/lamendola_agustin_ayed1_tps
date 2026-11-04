from math import sqrt


def main() -> None:
    try:
        numero = float(input("Ingrese un numero: "))
        print(f"La raiz cuadrada es {sqrt(numero)}")
    except ValueError:
        print("Error: se debe ingresar un numero mayor o igual a 0")


if __name__ == "__main__":
    main()
