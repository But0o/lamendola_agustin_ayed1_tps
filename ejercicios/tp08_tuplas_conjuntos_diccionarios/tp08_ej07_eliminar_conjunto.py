def main() -> None:
    conjunto = set(range(10))
    print(conjunto)

    numero = int(input("Ingrese un numero a eliminar (Finalizar = -1): "))
    while numero != -1:
        try:
            conjunto.remove(numero)
        except KeyError:
            print(f"Error: el numero {numero} no esta en el conjunto")
        print(conjunto)
        numero = int(input("Ingrese un numero a eliminar (Finalizar = -1): "))


if __name__ == "__main__":
    main()
