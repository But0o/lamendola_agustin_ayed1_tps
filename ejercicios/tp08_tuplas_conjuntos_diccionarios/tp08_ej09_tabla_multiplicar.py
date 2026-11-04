def main() -> None:
    n = int(input("Ingrese un numero entero: "))

    tabla = {i: n * i for i in range(1, 13)}

    for i, resultado in tabla.items():
        print(f"{n} x {i:2} = {resultado}")


if __name__ == "__main__":
    main()
