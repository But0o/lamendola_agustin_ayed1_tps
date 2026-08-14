def fecha_valida(dia,mes,anio):
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

def main():
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