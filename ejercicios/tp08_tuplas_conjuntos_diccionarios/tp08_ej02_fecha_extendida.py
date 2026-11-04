ANIO_CORTE: int = 30


def fecha_extendida(fecha: tuple[int, int, int]) -> str:
    """
    contrato

    Escribe una fecha en formato extendido. Si el año viene en dos
    dígitos, los mayores al año de corte se toman como del siglo pasado.

    pre: fecha es una tupla de enteros (dia, mes, anio) con una fecha valida
    post: devuelve una cadena con la fecha en formato extendido, por ejemplo "12 de Octubre de 2030"
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    dia, mes, anio = fecha

    if anio < 100:
        if anio > ANIO_CORTE:
            anio += 1900
        else:
            anio += 2000

    return f"{dia} de {meses[mes - 1]} de {anio}"


def main() -> None:
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    print(fecha_extendida((dia, mes, anio)))


if __name__ == "__main__":
    main()
