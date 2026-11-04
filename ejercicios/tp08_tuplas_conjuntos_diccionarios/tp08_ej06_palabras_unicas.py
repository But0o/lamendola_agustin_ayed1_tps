SIGNOS: str = ".,;:!?¡¿()\"'-"


def main() -> None:
    frase = input("Ingrese una frase: ")

    for signo in SIGNOS:
        frase = frase.replace(signo, " ")

    palabras = set(frase.split())

    print(sorted(palabras, key=len))


if __name__ == "__main__":
    main()
