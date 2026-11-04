UNIDADES: list[str] = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
DIEZ_A_DIECINUEVE: list[str] = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
VEINTE_A_VEINTINUEVE: list[str] = ["veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
DECENAS: list[str] = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
CENTENAS: list[str] = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]


def menor_a_cien(numero: int) -> str:
    """
    contrato

    Escribe en letras un número de hasta dos cifras.

    pre: numero es un entero entre 0 y 99
    post: devuelve numero expresado en letras; si numero es 0 devuelve una cadena vacia
    """
    if numero < 10:
        return UNIDADES[numero]
    if numero < 20:
        return DIEZ_A_DIECINUEVE[numero - 10]
    if numero < 30:
        return VEINTE_A_VEINTINUEVE[numero - 20]

    decena = DECENAS[numero // 10]
    unidad = numero % 10

    if unidad == 0:
        return decena
    return f"{decena} y {UNIDADES[unidad]}"


def menor_a_mil(numero: int) -> str:
    """
    contrato

    Escribe en letras un número de hasta tres cifras, teniendo en
    cuenta que el 100 exacto se dice "cien" y no "ciento".

    pre: numero es un entero entre 0 y 999
    post: devuelve numero expresado en letras; si numero es 0 devuelve una cadena vacia
    """
    if numero == 100:
        return "cien"

    centena = CENTENAS[numero // 100]
    resto = menor_a_cien(numero % 100)

    if centena != "" and resto != "":
        return f"{centena} {resto}"
    return centena + resto


def acortar_uno(texto: str) -> str:
    """
    contrato

    Corrige la terminación de un número que va seguido de "mil" o de
    "millones", porque se dice "veintiún mil" y no "veintiuno mil".

    pre: texto es un numero expresado en letras
    post: devuelve texto con el "uno" final cambiado por "un" ("veintiuno" por "veintiún"); si no termina en "uno" lo devuelve igual
    """
    if texto.endswith("veintiuno"):
        return texto[:-len("veintiuno")] + "veintiún"
    if texto.endswith("uno"):
        return texto[:-1]
    return texto


def menor_a_un_millon(numero: int) -> str:
    """
    contrato

    Escribe en letras un número de hasta seis cifras, separando los
    miles del resto.

    pre: numero es un entero entre 0 y 999999
    post: devuelve numero expresado en letras; si numero es 0 devuelve una cadena vacia
    """
    miles = numero // 1000
    resto = menor_a_mil(numero % 1000)

    if miles == 0:
        return resto

    if miles == 1:
        texto_miles = "mil"
    else:
        texto_miles = f"{acortar_uno(menor_a_mil(miles))} mil"

    if resto == "":
        return texto_miles
    return f"{texto_miles} {resto}"


def numero_a_letras(numero: int) -> str:
    """
    contrato

    Escribe en letras un número, separándolo en millones y en lo que
    queda por debajo del millón.

    pre: numero es un entero entre 0 y 1000000000000
    post: devuelve una cadena con numero expresado en letras
    """
    if numero == 0:
        return "cero"
    if numero == 1000000000000:
        return "un billón"

    millones = numero // 1000000
    resto = menor_a_un_millon(numero % 1000000)

    if millones == 0:
        return resto

    if millones == 1:
        texto_millones = "un millón"
    else:
        texto_millones = f"{acortar_uno(menor_a_un_millon(millones))} millones"

    if resto == "":
        return texto_millones
    return f"{texto_millones} {resto}"


def main() -> None:
    numero = int(input("Ingrese un numero entre 0 y 1 billon: "))

    print(numero_a_letras(numero))


if __name__ == "__main__":
    main()

# ¿En que cambiaria la funcion si tambien aceptara numeros negativos?
# hay que preguntar si el numero es menor a 0 y convertir su valor absoluto
# y agregarle la palabra "menos" adelante.
#
# ¿Y numeros con decimales?
# hay que separar la parte entera de la parte decimal, convertir cada una por
# separado y unirlas con la palabra "con" (por ejemplo "dos con cincuenta").
