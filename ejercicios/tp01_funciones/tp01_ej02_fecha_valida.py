def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    contrato

    Revisa si el día, el mes y el año indicados forman una fecha que
    realmente existe en el calendario. Tiene en cuenta que cada mes
    tiene una cantidad distinta de días y que los años bisiestos
    agregan un día extra a febrero.

    pre: dia, mes y anio son numeros enteros
    post: devuelve True si dia, mes y anio forman una fecha valida (contemplando años bisiestos), False en caso contrario
    """
    if anio <= 0:
        return False
    if mes < 1:
        return False
    if mes > 12:
        return False

    dias_mes = 0
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_mes = 31
    elif mes in (4, 6, 9, 11):
        dias_mes = 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            dias_mes = 29
        else:
            dias_mes = 28

    if dia < 1:
        return False
    if dia > dias_mes:
        return False

    return True

def main() -> None:
    dia = int(input("Ingresar un dia: "))
    mes = int(input("Ingresar un mes: "))
    anio = int(input("Ingresar un año: "))

    resultado = fecha_valida(dia,mes,anio)

    if resultado is True:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
