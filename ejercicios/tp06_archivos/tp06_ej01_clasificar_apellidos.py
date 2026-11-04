def clasificar_apellido(apellido,paises):
    for clave, valor in paises.items():
        if apellido.endswith(clave):
            return valor
    return "DESCARTE.txt"

def main():
    paises = {"ian": "ARMENIA.txt", "ini": "ITALIA.txt", "ez": "ESPANIA.txt"}

    with open("ejercicios/tp06_archivos/datos/nombres.csv", encoding= "utf-8-sig") as entrada:

        for linea in entrada:
                linea = linea.strip()
                if linea == "":
                    continue
                
                apellido = linea.split(", ")[0]
                nombre_archivo = clasificar_apellido(apellido,paises)
                with open(f"ejercicios/tp06_archivos/datos/{nombre_archivo}", "at",  encoding= "utf-8") as arch:
                    arch.write(linea + "\n")

main()