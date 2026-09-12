import random as rn

def calcular_peso():
    peso = rn.randint(150,350)
    return peso


def calidad_naranja(peso):
    return 200 <= peso <= 300

def clasificacion_naranja(cantidad):
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

def calcular_cajones(naranjas_buenas):
    cantidad_cajones = naranjas_buenas // 100
    sobrante = naranjas_buenas % 100
    return cantidad_cajones,sobrante

def calcular_camiones(peso_total):
    peso_total_kg = peso_total / 1000
    camiones_completos = peso_total_kg // 500
    resto_kg = peso_total_kg % 500
    if resto_kg / 500 * 100 >= 80:
        camiones_completos += 1
    return int(camiones_completos)


def main():
    cantidad = int(input("Ingrese la cantidad de naranjas que se cosecho: "))
    naranjas_buenas, naranjas_jugo, peso_total = clasificacion_naranja(cantidad)
    cantidad_cajones,sobrante = calcular_cajones(naranjas_buenas)
    print(f"Se llenaron {cantidad_cajones} cajones")
    print(f"Quedaron {naranjas_jugo} naranajas para jugo")
    print(f"Sobraron {sobrante} naranjas")
    print(f"Se utilizaron {calcular_camiones(peso_total)} camiones")

if __name__ == "__main__":
    main()