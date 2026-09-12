def cargar_socios() -> tuple[list[int], list[int]]:
    """
    contrato

    Registra los ingresos de los socios al club, sumando uno cada
    vez que el mismo socio vuelve a ingresar, hasta que se carga un
    0 para terminar.

    pre: no recibe parametros, se ingresan por teclado numeros de socio de 5 digitos hasta ingresar 0
    post: devuelve una tupla con la lista de socios (sin repetidos) y la lista de la cantidad de ingresos de cada uno, en el mismo orden
    """
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

def informar_ingresos(socios: list[int], ingresos: list[int]) -> None:
    """
    contrato

    Muestra por pantalla cuántas veces ingresó un socio al club.

    pre: socios es la lista de numeros de socio, ingresos es la lista con la cantidad de ingresos de cada uno (mismo orden)
    post: informa por pantalla cuantas veces ingreso cada socio
    """
    for socio, ingreso in zip(socios, ingresos):
        socio1 = socio
        ingreso1 = ingreso

    print(f"El socio {socio1} ingreso {ingreso1} veces")

def dar_de_baja(socios: list[int], ingresos: list[int]) -> tuple[int, int]:
    """
    contrato

    Elimina a un socio y su historial de ingresos, mostrando el
    listado de socios antes y después de sacarlo.

    pre: socios es la lista de numeros de socio, ingresos es la lista con la cantidad de ingresos de cada uno (mismo orden)
    post: elimina de ambas listas al socio ingresado por teclado y devuelve una tupla con el numero de socio eliminado y su cantidad de ingresos eliminados
    """
    socio = int(input("Ingrese el numero de socio a eliminar: "))
    informar_ingresos(socios, ingresos)
    indice = socios.index(socio)
    socio_eliminado = socios.pop(indice)
    cantidad_ingresos_eliminados = ingresos.pop(indice)
    informar_ingresos(socios, ingresos)
    return socio_eliminado,cantidad_ingresos_eliminados


def main() -> None:
    """ PUNTO A """
    socios, ingresos = cargar_socios()

    """ PUNTO B """
    socios, eliminados = dar_de_baja(socios, ingresos)
    print(f"Se eliminaron {eliminados} ingresos")
    socios_post_eliminado = socios
    ingresos_post_eliminados = eliminados
    print(f"El socio {socios_post_eliminado} ingreso {ingresos_post_eliminados} veces")

if __name__ == "__main__":
    main()
