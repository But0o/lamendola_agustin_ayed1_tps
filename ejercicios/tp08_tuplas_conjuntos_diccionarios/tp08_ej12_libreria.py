def incrementar_cuadernos(precios: dict[str, float]) -> None:
    """
    contrato

    Aumenta un 15% el precio de todos los cuadernos de la lista.

    pre: precios es un diccionario con los items como claves y sus precios como valores
    post: modifica precios incrementando un 15% los items cuyo nombre contiene "cuaderno"
    """
    for item in precios:
        if "cuaderno" in item.lower():
            precios[item] = precios[item] * 1.15


def item_mas_costoso(precios: dict[str, float]) -> str:
    """
    contrato

    Busca cuál es el ítem con el precio más alto de la lista.

    pre: precios es un diccionario no vacio con los items como claves y sus precios como valores
    post: devuelve el nombre del item mas costoso; no modifica precios
    """
    mas_costoso = ""
    precio_mas_alto = 0

    for item, precio in precios.items():
        if precio > precio_mas_alto:
            precio_mas_alto = precio
            mas_costoso = item

    return mas_costoso


def main() -> None:
    precios = {
        "Cuaderno rayado": 3500.0,
        "Cuaderno cuadriculado": 3800.0,
        "Lapiz": 450.0,
        "Lapicera": 900.0,
        "Goma de borrar": 300.0,
        "Mochila": 25000.0,
    }

    incrementar_cuadernos(precios)

    print("Lista de precios")
    for item, precio in precios.items():
        print(f"{item}: ${precio:.2f}")

    print(f"El item mas costoso es: {item_mas_costoso(precios)}")


if __name__ == "__main__":
    main()
