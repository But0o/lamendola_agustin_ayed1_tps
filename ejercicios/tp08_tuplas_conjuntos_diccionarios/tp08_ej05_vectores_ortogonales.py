def son_ortogonales(vector1: tuple[float, float], vector2: tuple[float, float]) -> bool:
    """
    contrato

    Indica si dos vectores son perpendiculares entre sí, revisando si
    su producto escalar da 0.

    pre: vector1 y vector2 son tuplas de dos numeros reales (x, y)
    post: devuelve True si los vectores son ortogonales, False en caso contrario
    """
    return vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0


def main() -> None:
    vector1 = (float(input("Vector 1, componente x: ")), float(input("Vector 1, componente y: ")))
    vector2 = (float(input("Vector 2, componente x: ")), float(input("Vector 2, componente y: ")))

    print(son_ortogonales(vector1, vector2))


if __name__ == "__main__":
    main()
