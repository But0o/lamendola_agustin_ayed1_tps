import csv
import random
from datetime import date, datetime

PISOS = 10
HABITACIONES = 6
RUTA = "ejercicios/tp06_archivos/datos/huespedes.csv"


def convertir_fecha(texto: str) -> date:
    """
    contrato

    Convierte una fecha en formato DDMMAAAA a un objeto date, para poder
    compararla y restarla con otras fechas.

    pre: texto es una cadena de 8 digitos con formato DDMMAAAA
    post: devuelve la fecha correspondiente; lanza ValueError si no es una fecha valida
    """
    return datetime.strptime(texto, "%d%m%Y").date()


def registrar_huespedes(ruta: str) -> None:
    """
    contrato

    Registra los ingresos de huespedes hasta que se ingrese el DNI -1 (o
    hasta que el hotel este completo) y los graba en un archivo CSV.

    pre: ruta es la ruta del archivo CSV a generar
    post: el archivo queda con un registro por huesped (DNI, nombre, fecha de ingreso, fecha de egreso, ocupantes); no hay DNI repetidos y la salida es posterior al ingreso
    """
    dnis = set()

    with open(ruta, "wt", encoding="utf-8", newline="") as arch:
        escritor = csv.writer(arch)

        dni = int(input("DNI (-1 para terminar): "))
        while dni != -1 and len(dnis) < PISOS * HABITACIONES:
            if dni in dnis:
                print("El DNI ya fue registrado")
            else:
                nombre = input("Apellido y nombre: ")
                ingreso = input("Fecha de ingreso (DDMMAAAA): ")
                egreso = input("Fecha de egreso (DDMMAAAA): ")
                ocupantes = int(input("Cantidad de ocupantes: "))

                if convertir_fecha(egreso) <= convertir_fecha(ingreso):
                    print("La fecha de egreso debe ser mayor a la de ingreso")
                else:
                    escritor.writerow([dni, nombre, ingreso, egreso, ocupantes])
                    dnis.add(dni)

            dni = int(input("DNI (-1 para terminar): "))


def asignar_habitaciones(ruta: str) -> list[list[dict | None]]:
    """
    contrato

    Lee el archivo de huespedes y le asigna a cada uno una habitacion
    libre elegida al azar.

    pre: ruta es la ruta de un archivo CSV con a lo sumo PISOS * HABITACIONES huespedes
    post: devuelve una matriz de PISOS x HABITACIONES donde cada celda tiene el huesped alojado (diccionario) o None si esta vacia; ninguna habitacion se asigna dos veces
    """
    hotel = [[None] * HABITACIONES for _ in range(PISOS)]
    libres = [(piso, hab) for piso in range(PISOS) for hab in range(HABITACIONES)]
    random.shuffle(libres)

    with open(ruta, encoding="utf-8", newline="") as arch:
        for dni, nombre, ingreso, egreso, ocupantes in csv.reader(arch):
            piso, hab = libres.pop()
            hotel[piso][hab] = {
                "dni": int(dni),
                "nombre": nombre,
                "ingreso": convertir_fecha(ingreso),
                "egreso": convertir_fecha(egreso),
                "ocupantes": int(ocupantes),
                "piso": piso + 1,
                "habitacion": hab + 1,
            }

    return hotel


def pisos_con_mas_habitaciones_ocupadas(hotel: list[list[dict | None]]) -> list[int]:
    """
    contrato

    Busca el piso con mayor cantidad de habitaciones ocupadas.

    pre: hotel es la matriz devuelta por asignar_habitaciones
    post: devuelve la lista de numeros de piso (desde 1) con la mayor cantidad de habitaciones ocupadas
    """
    ocupadas = [sum(1 for h in piso if h is not None) for piso in hotel]
    maximo = max(ocupadas)

    return [i + 1 for i, cantidad in enumerate(ocupadas) if cantidad == maximo]


def contar_habitaciones_vacias(hotel: list[list[dict | None]]) -> int:
    """
    contrato

    Cuenta las habitaciones vacias de todo el hotel.

    pre: hotel es la matriz devuelta por asignar_habitaciones
    post: devuelve la cantidad de habitaciones sin huesped
    """
    return sum(1 for piso in hotel for h in piso if h is None)


def pisos_con_mas_personas(hotel: list[list[dict | None]]) -> list[int]:
    """
    contrato

    Busca el piso con mayor cantidad de personas alojadas.

    pre: hotel es la matriz devuelta por asignar_habitaciones
    post: devuelve la lista de numeros de piso (desde 1) con la mayor cantidad de personas
    """
    personas = [sum(h["ocupantes"] for h in piso if h is not None) for piso in hotel]
    maximo = max(personas)

    return [i + 1 for i, cantidad in enumerate(personas) if cantidad == maximo]


def proximas_a_desocupar(hotel: list[list[dict | None]], hoy: date) -> list[dict]:
    """
    contrato

    Busca las habitaciones que se desocupan primero a partir de la fecha actual.

    pre: hotel es la matriz devuelta por asignar_habitaciones; hoy es la fecha actual
    post: devuelve la lista de huespedes cuya fecha de egreso es la mas cercana a hoy (sin ser anterior); la lista es vacia si ninguna habitacion se desocupa desde hoy
    """
    vigentes = [h for piso in hotel for h in piso if h is not None and h["egreso"] >= hoy]
    if not vigentes:
        return []

    proxima = min(h["egreso"] for h in vigentes)

    return [h for h in vigentes if h["egreso"] == proxima]


def huespedes_por_dias(hotel: list[list[dict | None]]) -> list[dict]:
    """
    contrato

    Arma el listado de huespedes ordenado por cantidad de dias de alojamiento.

    pre: hotel es la matriz devuelta por asignar_habitaciones
    post: devuelve la lista de huespedes ordenada de menor a mayor cantidad de dias
    """
    huespedes = [h for piso in hotel for h in piso if h is not None]

    return sorted(huespedes, key=lambda h: (h["egreso"] - h["ingreso"]).days)


def main() -> None:
    registrar_huespedes(RUTA)
    hotel = asignar_habitaciones(RUTA)

    # Punto B
    pisos = pisos_con_mas_habitaciones_ocupadas(hotel)
    print(f"Piso con mas habitaciones ocupadas: {pisos}")

    # Punto C
    print(f"Habitaciones vacias: {contar_habitaciones_vacias(hotel)}")

    # Punto D
    print(f"Piso con mas personas: {pisos_con_mas_personas(hotel)}")

    # Punto E
    hoy = convertir_fecha(input("Fecha actual (DDMMAAAA): "))
    proximas = proximas_a_desocupar(hotel, hoy)
    if proximas:
        for h in proximas:
            print(f"Piso {h['piso']}, habitacion {h['habitacion']} se desocupa el {h['egreso']:%d/%m/%Y}")
    else:
        print("Ninguna habitacion se desocupa desde la fecha actual")

    # Punto F
    for h in huespedes_por_dias(hotel):
        dias = (h["egreso"] - h["ingreso"]).days
        print(f"{h['dni']} - {h['nombre']} - {dias} dias")


if __name__ == "__main__":
    main()
