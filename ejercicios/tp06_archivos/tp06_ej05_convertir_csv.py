import csv

RUTA_FORMATO1 = "ejercicios/tp06_archivos/datos/empleados_formato1.txt"
RUTA_FORMATO2 = "ejercicios/tp06_archivos/datos/empleados_formato2.txt"
RUTA_CSV1 = "ejercicios/tp06_archivos/datos/empleados_formato1.csv"
RUTA_CSV2 = "ejercicios/tp06_archivos/datos/empleados_formato2.csv"

# Apellido y Nombre, Fecha de alta, Domicilio (un espacio de separacion entre campos)
ANCHOS = (18, 8, 35)


def leer_campos_ancho_fijo(linea: str) -> list[str]:
    """
    contrato

    Separa un registro de longitud fija en sus campos.

    pre: linea es un registro con los campos de ANCHOS separados por un espacio
    post: devuelve la lista de campos sin los espacios del final
    """
    campos = []
    posicion = 0

    for ancho in ANCHOS:
        campos.append(linea[posicion:posicion + ancho].rstrip())
        posicion += ancho + 1

    return campos


def leer_campos_con_longitud(linea: str) -> list[str]:
    """
    contrato

    Separa un registro en el que cada campo esta precedido por un numero de
    dos digitos con su longitud. Soporta cualquier cantidad de campos.

    pre: linea es un registro sin salto de linea donde cada campo va precedido por su longitud de dos digitos
    post: devuelve la lista de campos
    """
    campos = []
    posicion = 0

    while posicion < len(linea):
        longitud = int(linea[posicion:posicion + 2])
        campos.append(linea[posicion + 2:posicion + 2 + longitud])
        posicion += 2 + longitud

    return campos


def convertir_a_csv(ruta_entrada: str, ruta_salida: str, leer_campos) -> None:
    """
    contrato

    Convierte un archivo de empleados a CSV, usando leer_campos para separar
    los campos de cada registro.

    pre: ruta_entrada es la ruta de un archivo de empleados existente; leer_campos recibe un registro y devuelve la lista de sus campos
    post: ruta_salida queda con un registro CSV por cada registro del archivo de entrada
    """
    with open(ruta_entrada, "rt", encoding="utf-8") as entrada, open(ruta_salida, "wt", encoding="utf-8", newline="") as salida:
        escritor = csv.writer(salida)

        for linea in entrada:
            linea = linea.rstrip("\n")
            if linea.strip() == "":
                continue

            escritor.writerow(leer_campos(linea))


def main() -> None:
    convertir_a_csv(RUTA_FORMATO1, RUTA_CSV1, leer_campos_ancho_fijo)
    convertir_a_csv(RUTA_FORMATO2, RUTA_CSV2, leer_campos_con_longitud)

    print("Archivos CSV generados")


if __name__ == "__main__":
    main()
