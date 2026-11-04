def convertir_a_natural(ingreso: str) -> int:
    """
    contrato

    Convierte lo que escribió el usuario en un número natural, lanzando
    una excepción con la razón exacta si no se puede.

    pre: ingreso es una cadena de caracteres
    post: devuelve ingreso convertido a entero si es un numero natural; en caso contrario lanza ValueError con la razon del error
    """
    try:
        float(ingreso)
    except ValueError:
        raise ValueError("Lo ingresado no es un numero")

    try:
        numero = int(ingreso)
    except ValueError:
        raise ValueError("El numero ingresado no es entero")

    if numero <= 0:
        raise ValueError("El numero ingresado no es mayor que 0")

    return numero


def ingresar_natural() -> int:
    """
    contrato

    Le pide un número natural al usuario hasta que lo ingrese bien,
    mostrando la razón del error en cada intento inválido.

    pre: no recibe parametros, el valor se ingresa por teclado
    post: devuelve el numero natural ingresado
    """
    while True:
        try:
            return convertir_a_natural(input("Ingrese un numero natural: "))
        except ValueError as error:
            print(f"Error: {error}")


def main() -> None:
    numero = ingresar_natural()

    print(f"El numero ingresado es {numero}")


if __name__ == "__main__":
    main()
