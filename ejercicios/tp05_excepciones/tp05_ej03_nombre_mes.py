def nombre_mes(numero: int) -> str:
    """
    contrato

    Busca el nombre del mes que corresponde a un número. Los números
    menores a 1 se rechazan a mano porque en una lista los índices
    negativos no generan error.

    pre: numero es un numero entero
    post: devuelve el nombre del mes correspondiente, o una cadena vacia si el numero de mes es invalido
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    try:
        if numero < 1:
            raise IndexError
        return meses[numero - 1]
    except IndexError:
        return ""


def main() -> None:
    numero = int(input("Ingrese un numero de mes: "))

    print(nombre_mes(numero))


if __name__ == "__main__":
    main()
