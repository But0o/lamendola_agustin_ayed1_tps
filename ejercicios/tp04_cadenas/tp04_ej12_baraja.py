def main() -> None:
    palos = ["Oros", "Copas", "Espadas", "Bastos"]

    baraja = [f"{numero} {palo}" for palo in palos for numero in range(1, 13)]

    print(baraja)


if __name__ == "__main__":
    main()
