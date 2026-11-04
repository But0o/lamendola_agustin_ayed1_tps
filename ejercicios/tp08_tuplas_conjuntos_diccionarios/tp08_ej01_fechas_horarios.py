def dias_del_mes(mes: int, anio: int) -> int:
    """
    contrato

    Indica cuántos días tiene un mes, teniendo en cuenta que los años
    bisiestos agregan un día extra a febrero.

    pre: mes es un entero entre 1 y 12, anio es un entero positivo
    post: devuelve la cantidad de dias del mes indicado
    """
    if mes in (4, 6, 9, 11):
        return 30
    if mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
            return 29
        return 28
    return 31


def fecha_valida(fecha: tuple[int, int, int]) -> bool:
    """
    contrato

    Revisa si una fecha realmente existe en el calendario.

    pre: fecha es una tupla de enteros (dia, mes, anio)
    post: devuelve True si fecha es una fecha valida, False en caso contrario
    """
    dia, mes, anio = fecha

    if anio <= 0:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > dias_del_mes(mes, anio):
        return False

    return True


def ingresar_fecha() -> tuple[int, int, int]:
    """
    contrato

    Le pide una fecha al usuario hasta que ingrese una que sea válida.

    pre: no recibe parametros, los valores se ingresan por teclado como numeros enteros
    post: devuelve una tupla (dia, mes, anio) con una fecha valida
    """
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))

    while not fecha_valida((dia, mes, anio)):
        print("La fecha ingresada no es valida")
        dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese el mes: "))
        anio = int(input("Ingrese el año: "))

    return dia, mes, anio


def sumar_dias(fecha: tuple[int, int, int], n: int) -> tuple[int, int, int]:
    """
    contrato

    Calcula la fecha que resulta de avanzar una cantidad de días,
    pasando al mes y al año siguiente cuando corresponde.

    pre: fecha es una tupla (dia, mes, anio) con una fecha valida y n es un entero mayor o igual a 0
    post: devuelve una tupla (dia, mes, anio) con la fecha resultante de sumar n dias a fecha
    """
    dia, mes, anio = fecha

    for _ in range(n):
        dia += 1
        if dia > dias_del_mes(mes, anio):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1

    return dia, mes, anio


def ingresar_horario() -> tuple[int, int]:
    """
    contrato

    Le pide un horario al usuario hasta que ingrese uno que sea correcto.

    pre: no recibe parametros, los valores se ingresan por teclado como numeros enteros
    post: devuelve una tupla (horas, minutos) con horas entre 0 y 23 y minutos entre 0 y 59
    """
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))

    while horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        print("El horario ingresado no es correcto")
        horas = int(input("Ingrese las horas: "))
        minutos = int(input("Ingrese los minutos: "))

    return horas, minutos


def diferencia_horarios(horario1: tuple[int, int], horario2: tuple[int, int]) -> tuple[int, int]:
    """
    contrato

    Calcula el tiempo que pasa entre dos horarios. Si el primero es
    mayor al segundo, se considera que corresponde al día anterior.

    pre: horario1 y horario2 son tuplas (horas, minutos) con horarios correctos
    post: devuelve una tupla (horas, minutos) con la diferencia entre ambos horarios, que nunca supera las 24 horas
    """
    minutos1 = horario1[0] * 60 + horario1[1]
    minutos2 = horario2[0] * 60 + horario2[1]

    if minutos1 > minutos2:
        minutos2 += 24 * 60

    diferencia = minutos2 - minutos1

    return diferencia // 60, diferencia % 60


def main() -> None:
    # Punto A
    print("Punto A")
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha}")
    print("------------------")
    # Punto B
    print("Punto B")
    n = int(input("Ingrese la cantidad de dias a sumar: "))
    print(f"Fecha resultante: {sumar_dias(fecha, n)}")
    print("------------------")
    # Punto C
    print("Punto C")
    print("Primer horario")
    horario1 = ingresar_horario()
    print("Segundo horario")
    horario2 = ingresar_horario()
    print(f"Horarios ingresados: {horario1} y {horario2}")
    print("------------------")
    # Punto D
    print("Punto D")
    print(f"Diferencia: {diferencia_horarios(horario1, horario2)}")


if __name__ == "__main__":
    main()
