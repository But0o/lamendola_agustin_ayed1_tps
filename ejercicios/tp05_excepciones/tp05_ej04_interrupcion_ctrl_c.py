def main() -> None:
    numero = 1

    while numero <= 100000:
        try:
            print(numero)
            numero += 1
        except KeyboardInterrupt:
            respuesta = input("Desea detener el programa? (s/n): ")
            if respuesta == "s":
                break


if __name__ == "__main__":
    main()
