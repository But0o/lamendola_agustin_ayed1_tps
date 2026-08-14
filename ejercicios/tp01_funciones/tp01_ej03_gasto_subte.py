TARIFA_MAXIMA = 1684

def calcular_valor(viajes):
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

def main():
    viajes = int(input("Ingresa el total de viajes del mes: "))

    while viajes <= 0:
        print("La cantidad de viajes debe ser mayor a 0.")
        viajes = int(input("Ingresa nuevamente el total de viajes: "))
        
    print(calcular_valor(viajes))

if __name__ == "__main__":
    main()