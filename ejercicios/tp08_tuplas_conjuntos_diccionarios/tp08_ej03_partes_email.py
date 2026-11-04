def partes_email(direccion: str) -> tuple[str, ...]:
    """
    contrato

    Separa una dirección de correo en sus partes: el usuario y cada
    uno de los pedazos del dominio.

    pre: direccion es una cadena de caracteres
    post: devuelve una tupla con las partes de direccion, o una tupla vacia si el formato es invalido
    """
    if direccion.count("@") != 1 or " " in direccion:
        return ()

    usuario, dominio = direccion.split("@")
    partes_dominio = dominio.split(".")

    if usuario == "" or len(partes_dominio) < 2 or "" in partes_dominio:
        return ()

    return (usuario, *partes_dominio)


def main() -> None:
    direccion = input("Ingrese una direccion de correo: ")

    print(partes_email(direccion))


if __name__ == "__main__":
    main()
