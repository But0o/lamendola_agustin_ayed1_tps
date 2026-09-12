TARIFA_MAXIMA = 1684

def calcular_valor(viajes: int) -> float:
    """
    contrato

    Calcula cuánto gastó una persona en el mes viajando en subte,
    según la cantidad de viajes que realizó. Cuantos más viajes hace,
    mayor es el descuento que se le aplica sobre la tarifa máxima.

    pre: viajes es un numero entero positivo, representa la cantidad de viajes realizados en el mes
    post: devuelve el total gastado en el mes aplicando el descuento correspondiente segun la cantidad de viajes
    """
    if viajes <= 20:
        precio_pasaje = TARIFA_MAXIMA
    elif viajes <= 30:
        descuento = TARIFA_MAXIMA * 0.2
        precio_pasaje = TARIFA_MAXIMA - descuento
        
    elif viajes <= 40:
        descuento = TARIFA_MAXIMA * 0.3
        precio_pasaje = TARIFA_MAXIMA - descuento
        
    else:
        descuento = TARIFA_MAXIMA * 0.4
        precio_pasaje = TARIFA_MAXIMA - descuento

    total = precio_pasaje * viajes
    return total

def main() -> None:
    viajes = int(input("Ingresa el total de viajes del mes: "))

    while viajes <= 0:
        print("La cantidad de viajes debe ser mayor a 0.")
        viajes = int(input("Ingresa nuevamente el total de viajes: "))
        
    print(calcular_valor(viajes))

if __name__ == "__main__":
    main()
