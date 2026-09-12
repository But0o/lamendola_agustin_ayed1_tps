import random as rn

def calcular_peso() -> int:
    """
    contrato

    Genera un peso al azar para simular el de una naranja recién
    cosechada.

    pre: no recibe parametros
    post: devuelve un peso simulado al azar entre 150 y 350 gramos
    """
    peso = rn.randint(150,350)
    return peso


def calidad_naranja(peso: int) -> bool:
    """
    contrato

    Determina si el peso de una naranja está dentro del rango
    aceptable para vender, o si por el contrario debe destinarse a
    jugo.

    pre: peso es un numero entero que representa el peso de una naranja en gramos
    post: devuelve True si el peso esta entre 200 y 300 gramos (naranja apta para venta), False en caso contrario
    """
    return 200 <= peso <= 300

def clasificacion_naranja(cantidad: int) -> tuple[int, int, int]:
    """
    contrato

    Recorre la cosecha de naranjas separando cuántas son aptas para
    venta y cuántas deben ir a jugo, y va sumando el peso de las que
    sirven para venta.

    pre: cantidad es un numero entero positivo, representa la cantidad de naranjas cosechadas
    post: devuelve una tupla con la cantidad de naranjas buenas, la cantidad de naranjas para jugo y el peso total acumulado de las naranjas buenas
    """
    naranjas_buenas = 0
    naranajas_jugo = 0
    peso_total = 0
    for _ in range(cantidad):
        peso = calcular_peso()
        if calidad_naranja(peso):
            naranjas_buenas +=1
            peso_total += peso
        else:
            naranajas_jugo +=1
    return naranjas_buenas, naranajas_jugo, peso_total

def calcular_cajones(naranjas_buenas: int) -> tuple[int, int]:
    """
    contrato

    Calcula cuántos cajones completos de 100 naranjas se pueden armar
    con las naranjas buenas, y cuántas naranjas quedan sueltas.

    pre: naranjas_buenas es un numero entero positivo
    post: devuelve una tupla con la cantidad de cajones completos (100 naranjas cada uno) y la cantidad de naranjas sobrantes
    """
    cantidad_cajones = naranjas_buenas // 100
    sobrante = naranjas_buenas % 100
    return cantidad_cajones,sobrante

def calcular_camiones(peso_total: int) -> int:
    """
    contrato

    Calcula cuántos camiones hacen falta para transportar el peso
    total de naranjas, sumando un camión más si el que queda a
    medio llenar supera el 80% de ocupación.

    pre: peso_total es un numero entero que representa el peso total en gramos de las naranjas buenas
    post: devuelve la cantidad de camiones necesarios para transportar el peso total, sumando un camion mas si el ultimo queda ocupado al 80% o mas
    """
    peso_total_kg = peso_total / 1000
    camiones_completos = peso_total_kg // 500
    resto_kg = peso_total_kg % 500
    if resto_kg / 500 * 100 >= 80:
        camiones_completos += 1
    return int(camiones_completos)


def main() -> None:
    cantidad = int(input("Ingrese la cantidad de naranjas que se cosecho: "))
    naranjas_buenas, naranjas_jugo, peso_total = clasificacion_naranja(cantidad)
    cantidad_cajones,sobrante = calcular_cajones(naranjas_buenas)
    print(f"Se llenaron {cantidad_cajones} cajones")
    print(f"Quedaron {naranjas_jugo} naranajas para jugo")
    print(f"Sobraron {sobrante} naranjas")
    print(f"Se utilizaron {calcular_camiones(peso_total)} camiones")

if __name__ == "__main__":
    main()
