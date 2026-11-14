import os


def dividir_archivo(ruta: str, tamanio_maximo: int) -> int:
    """
    contrato

    Divide un archivo de texto en partes de a lo sumo tamanio_maximo bytes,
    sin cortar ningun registro (linea). Lee el archivo linea por linea, sin
    cargarlo completo en memoria.

    pre: ruta es la ruta de un archivo de texto existente y tamanio_maximo es un entero positivo (en bytes)
    post: genera los archivos <nombre>_parte<N><extension> junto al original y devuelve la cantidad de partes; lanza ValueError si algun registro supera tamanio_maximo y OSError si no se puede leer o escribir un archivo
    """
    base, extension = os.path.splitext(ruta)
    partes = 0
    tamanio_actual = 0
    salida = None

    try:
        with open(ruta, "rt", encoding="utf-8", newline="") as entrada:
            for linea in entrada:
                tamanio_linea = len(linea.encode("utf-8"))
                if tamanio_linea > tamanio_maximo:
                    raise ValueError("Hay un registro mas grande que el tamanio maximo")

                if salida is None or tamanio_actual + tamanio_linea > tamanio_maximo:
                    if salida is not None:
                        salida.close()
                    partes += 1
                    salida = open(f"{base}_parte{partes}{extension}", "wt", encoding="utf-8", newline="")
                    tamanio_actual = 0

                salida.write(linea)
                tamanio_actual += tamanio_linea
    finally:
        if salida is not None:
            salida.close()

    return partes


def main() -> None:
    ruta = input("Ingrese la ruta del archivo a dividir: ")
    tamanio_maximo = int(input("Ingrese el tamanio maximo de cada parte (en bytes): "))

    try:
        partes = dividir_archivo(ruta, tamanio_maximo)
        print(f"El archivo se dividio en {partes} partes")
    except (OSError, ValueError) as error:
        print(f"Error: no se pudo dividir el archivo ({error})")


if __name__ == "__main__":
    main()
