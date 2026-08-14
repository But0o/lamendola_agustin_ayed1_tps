def diadelasemana(dia,mes,anio):
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def calendario(mes,anio):
    dias = 0

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias = 31

    elif mes in (4, 6, 9, 11):
        dias = 30

    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            dias = 29
        else:
            dias = 28
            
    primer_dia = diadelasemana(1,mes,anio)

    print("Dom Lun Mar Mie Jue Vie Sab")

    for i in range(primer_dia):
        print("    ", end="")

    dia_semana = primer_dia

    for dia in range(1, dias + 1 ):
        print(f"{dia:>3} ", end="")

        dia_semana += 1

        if dia_semana == 7:
            print("")
            dia_semana = 0


def main():
    print("----- CALENDARIO -----")

    mes = int(input("Ingrese el mes (1-12): "))
    anio = int(input("Ingrese el año: "))

    if mes < 1 or mes > 12:
        print("El mes ingresado no es válido")

    elif anio <= 0:
        print("El año ingresado no es válido")

    else:
        calendario(mes, anio)


if __name__ == "__main__":
    main()



