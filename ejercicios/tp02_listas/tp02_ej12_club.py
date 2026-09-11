def cargar_socios():
    socios = []
    ingresos = []
    while True:
        socio = int(input("Ingrese su numero de socio: "))
        if socio == 0:
            break
        elif len(str(socio)) == 5:
            if socio in socios:
                pos = socios.index(socio)
                ingresos[pos] += 1
            else:
                socios.append(socio)
                ingresos.append(1)
        else:
            print("Ingrese un numero valido")
    return socios, ingresos

def informar_ingresos(socios, ingresos):
    for socio, ingreso in zip(socios, ingresos):
        socio1 = socio
        ingreso1 = ingreso

    print(f"El socio {socio1} ingreso {ingreso1} veces")

def dar_de_baja(socios, ingresos):
    socio = int(input("Ingrese el numero de socio a eliminar: "))
    informar_ingresos(socios, ingresos)
    indice = socios.index(socio)
    socio_eliminado = socios.pop(indice)
    cantidad_ingresos_eliminados = ingresos.pop(indice)
    informar_ingresos(socios, ingresos)
    return socios, ingresos, cantidad_ingresos_eliminados


socios, ingresos = cargar_socios()
socios, ingresos, eliminados = dar_de_baja(socios, ingresos)
print(f"Se eliminaron {eliminados} ingresos")