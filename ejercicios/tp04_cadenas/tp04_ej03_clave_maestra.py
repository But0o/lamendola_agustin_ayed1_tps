def obtener_claves(clave_maestra: str) -> tuple[str, str]:
    """
    contrato

    Separa la clave maestra en las dos claves que tiene intercaladas,
    numerando los dígitos desde la izquierda y empezando por el 1.

    pre: clave_maestra es una cadena formada solo por digitos
    post: devuelve una tupla con la clave formada por los digitos de las posiciones impares y la clave formada por los digitos de las posiciones pares
    """
    clave1 = clave_maestra[0::2]
    clave2 = clave_maestra[1::2]

    return clave1, clave2


def main() -> None:
    clave_maestra = input("Ingrese la clave maestra: ")

    clave1, clave2 = obtener_claves(clave_maestra)

    print(f"Clave 1: {clave1}")
    print(f"Clave 2: {clave2}")


if __name__ == "__main__":
    main()
