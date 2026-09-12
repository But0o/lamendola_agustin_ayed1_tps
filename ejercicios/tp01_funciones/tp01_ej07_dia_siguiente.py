def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    contrato

    Toma una fecha y calcula cuál es el día siguiente, pasando
    correctamente al mes o al año que corresponde cuando la fecha
    llega al último día de un mes.

    pre: dia, mes y anio forman una fecha valida
    post: devuelve la tupla (dia, mes, anio) correspondiente al dia siguiente de la fecha dada
    """
    dias = 0

    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias = 31
    elif mes in (4,6,9,11):
        dias = 30
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            dias = 29
        else:
            dias = 28

    if dia < dias:
        dia = dia + 1
    elif mes == 12:
        dia = 1
        mes = 1
        anio = anio + 1
    else:
        dia = 1
        mes = mes + 1
    return dia, mes, anio

def sumar_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """
    contrato

    Toma una fecha y le suma una cantidad de días indicada, avanzando
    día por día hasta llegar a la fecha final.

    pre: dia, mes y anio forman una fecha valida, n es un numero entero positivo
    post: devuelve la tupla (dia, mes, anio) resultante de sumarle n dias a la fecha dada
    """
    for i in range(n):
        dia,mes,anio = dia_siguiente(dia,mes,anio)
    return dia,mes,anio

def diferencia_dias(dia: int, mes: int, anio: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    contrato

    Cuenta cuántos días hay entre dos fechas, avanzando de a un día
    desde la primera hasta llegar a la segunda.

    pre: (dia, mes, anio) y (dia2, mes2, anio2) son fechas validas
    post: devuelve la cantidad de dias que hay entre ambas fechas
    """
    contador = 0
    fecha1 = dia,mes,anio
    fecha2= dia2,mes2,anio2
    while fecha1 != fecha2:
        dia,mes,anio = dia_siguiente(dia,mes,anio)
        fecha1 = dia,mes,anio
        contador += 1
    return contador


def main() -> None:
    print("----- MENÚ DE FECHAS -----")
    print("1. Calcular día siguiente")
    print("2. Sumar N días a una fecha")
    print("3. Calcular días entre dos fechas")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        dia = int(input("Ingrese un día: "))
        mes = int(input("Ingrese un mes: "))
        anio = int(input("Ingrese un año: "))

        resultado = dia_siguiente(dia, mes, anio)

        print(f"El día siguiente es: {resultado}")

    elif opcion == 2:
        dia = int(input("Ingrese un día: "))
        mes = int(input("Ingrese un mes: "))
        anio = int(input("Ingrese un año: "))
        n = int(input("Ingrese la cantidad de días a sumar: "))

        resultado = sumar_dias(dia, mes, anio, n)

        print(f"La nueva fecha es: {resultado}")

    elif opcion == 3:
        print("Ingrese la primera fecha:")
        dia = int(input("Día: "))
        mes = int(input("Mes: "))
        anio = int(input("Año: "))

        print("Ingrese la segunda fecha:")
        dia2 = int(input("Día: "))
        mes2 = int(input("Mes: "))
        anio2 = int(input("Año: "))

        resultado = diferencia_dias(dia, mes, anio, dia2, mes2, anio2)

        print(f"La diferencia es de {resultado} días")

    else:
        print("La opción ingresada no es válida")

if __name__ == "__main__":
    main()
