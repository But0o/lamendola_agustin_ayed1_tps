import random as rn


def main() -> None:
    numero_secreto = rn.randint(1, 500)
    intentos = 0
    adivinado = False

    while not adivinado:
        intentos += 1
        try:
            numero = int(input("Adivine el numero entre 1 y 500: "))
            if numero_secreto > numero:
                print("El numero a adivinar es mayor")
            elif numero_secreto < numero:
                print("El numero a adivinar es menor")
            else:
                adivinado = True
        except ValueError:
            print("Error: lo ingresado no es un numero")

    print(f"Adivinaste el numero en {intentos} intentos")


if __name__ == "__main__":
    main()
