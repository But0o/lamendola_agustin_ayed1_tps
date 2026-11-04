def email_valido(direccion: str) -> bool:
    """
    contrato

    Revisa si una dirección de correo es válida: un solo @, un usuario
    solo con caracteres alfanuméricos y un dominio de al menos un
    caracter que termine en .com o .com.ar.

    pre: direccion es una cadena de caracteres
    post: devuelve True si direccion es una direccion de correo valida, False en caso contrario
    """
    if direccion.count("@") != 1:
        return False

    usuario, dominio = direccion.split("@")

    if not usuario.isalnum():
        return False

    if dominio.endswith(".com.ar"):
        nombre_dominio = dominio[:-len(".com.ar")]
    elif dominio.endswith(".com"):
        nombre_dominio = dominio[:-len(".com")]
    else:
        return False

    return len(nombre_dominio) >= 1


def main() -> None:
    dominios = set()

    direccion = input("Ingrese una direccion de correo: ")
    while direccion != "":
        if email_valido(direccion):
            print("La direccion es valida")
            dominios.add(direccion.split("@")[1].lower())
        else:
            print("La direccion no es valida")
        direccion = input("Ingrese una direccion de correo (Finalizar = vacio): ")

    print("Dominios ingresados:")
    for dominio in sorted(dominios):
        print(dominio)


if __name__ == "__main__":
    main()
