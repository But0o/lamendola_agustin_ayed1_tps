RUTA_ALTURAS = "ejercicios/tp06_archivos/datos/alturas.txt"
RUTA_PROMEDIOS = "ejercicios/tp06_archivos/datos/promedios.txt"


def grabar_rango_alturas(ruta: str) -> None:
    """
    contrato

    Graba en un archivo las alturas de los atletas de distintas disciplinas,
    ingresadas por teclado. Cada dato se graba en una linea distinta.

    pre: ruta es la ruta del archivo a generar; los nombres de los deportes no son numeros
    post: el archivo queda con la disciplina seguida de las alturas de sus atletas, una por linea; se termina de cargar disciplinas con un nombre vacio y las alturas de una disciplina con 0
    """
    with open(ruta, "wt", encoding="utf-8") as arch:
        deporte = input("Deporte (vacio para terminar): ")
        while deporte != "":
            arch.write(f"{deporte}\n")

            altura = float(input("Altura del atleta (0 para terminar el deporte): "))
            while altura != 0:
                arch.write(f"{altura}\n")
                altura = float(input("Altura del atleta (0 para terminar el deporte): "))

            deporte = input("Deporte (vacio para terminar): ")


def grabar_promedio(ruta_alturas: str, ruta_promedios: str) -> None:
    """
    contrato

    Graba en un archivo el promedio de las alturas de cada disciplina,
    leyendo los datos del archivo generado por grabar_rango_alturas.

    pre: ruta_alturas es la ruta del archivo generado por grabar_rango_alturas; ruta_promedios es la ruta del archivo a generar
    post: ruta_promedios queda con la disciplina y su promedio en lineas diferentes
    """
    with open(ruta_alturas, "rt", encoding="utf-8") as entrada, open(ruta_promedios, "wt", encoding="utf-8") as salida:
        deporte = ""
        suma = 0
        cantidad = 0

        for linea in entrada:
            linea = linea.strip()
            try:
                suma += float(linea)
                cantidad += 1
            except ValueError:
                if cantidad > 0:
                    salida.write(f"{deporte}\n{suma / cantidad:.2f}\n")
                deporte = linea
                suma = 0
                cantidad = 0

        if cantidad > 0:
            salida.write(f"{deporte}\n{suma / cantidad:.2f}\n")


def mostrar_mas_altos(ruta_promedios: str) -> list[str]:
    """
    contrato

    Obtiene las disciplinas cuyos atletas superan la estatura promedio
    general, leyendo los datos del archivo de promedios.

    pre: ruta_promedios es la ruta del archivo generado por grabar_promedio, con al menos una disciplina
    post: devuelve la lista de disciplinas cuyo promedio es mayor al promedio general
    """
    with open(ruta_promedios, "rt", encoding="utf-8") as arch:
        lineas = [linea.strip() for linea in arch]

    deportes = lineas[0::2]
    promedios = [float(promedio) for promedio in lineas[1::2]]
    promedio_general = sum(promedios) / len(promedios)

    return [deporte for deporte, promedio in zip(deportes, promedios) if promedio > promedio_general]


def main() -> None:
    grabar_rango_alturas(RUTA_ALTURAS)
    grabar_promedio(RUTA_ALTURAS, RUTA_PROMEDIOS)

    print("Disciplinas que superan la estatura promedio general:")
    for deporte in mostrar_mas_altos(RUTA_PROMEDIOS):
        print(deporte)


if __name__ == "__main__":
    main()
