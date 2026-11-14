def quitar_comentario(linea: str) -> str:
    """
    contrato

    Elimina el comentario de una linea de codigo Python, respetando los #
    que estan encerrados entre comillas simples o dobles.

    pre: linea es una linea de codigo Python
    post: devuelve la linea sin el comentario y sin el salto de linea final
    """
    comilla = ""
    i = 0

    while i < len(linea):
        caracter = linea[i]
        if comilla != "":
            if caracter == "\\":
                i += 1
            elif caracter == comilla:
                comilla = ""
        elif caracter in "'\"":
            comilla = caracter
        elif caracter == "#":
            return linea[:i].rstrip()
        i += 1

    return linea.rstrip("\n")


def eliminar_comentarios(ruta_entrada: str, ruta_salida: str) -> None:
    """
    contrato

    Copia un programa Python a otro archivo sin sus comentarios (#) ni sus
    cadenas de documentacion (docstrings). Lee el archivo linea por linea.

    pre: ruta_entrada es la ruta de un programa Python existente; ruta_salida es la ruta del archivo a generar
    post: ruta_salida queda con el programa sin comentarios ni docstrings
    """
    delimitador_abierto = ""

    with open(ruta_entrada, "rt", encoding="utf-8") as entrada, open(ruta_salida, "wt", encoding="utf-8") as salida:
        for linea in entrada:
            if delimitador_abierto != "":
                if delimitador_abierto in linea:
                    delimitador_abierto = ""
                continue

            sin_sangria = linea.lstrip()
            if sin_sangria.startswith('"""') or sin_sangria.startswith("'''"):
                delimitador = sin_sangria[:3]
                if delimitador not in sin_sangria[3:]:
                    delimitador_abierto = delimitador
                continue

            nueva = quitar_comentario(linea)
            if nueva.strip() == "" and linea.strip() != "":
                continue

            salida.write(nueva + "\n")


def main() -> None:
    ruta = input("Ingrese la ruta del programa Python: ")
    base = ruta[:-3] if ruta.endswith(".py") else ruta
    ruta_salida = f"{base}_sin_comentarios.py"

    eliminar_comentarios(ruta, ruta_salida)
    print(f"Programa sin comentarios grabado en {ruta_salida}")


if __name__ == "__main__":
    main()
