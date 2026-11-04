COLUMNAS: int = 80


def main() -> None:
    cadena = input("Ingrese una cadena: ")

    print(cadena.center(COLUMNAS))


if __name__ == "__main__":
    main()
