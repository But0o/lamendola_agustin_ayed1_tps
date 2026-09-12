def calcular_vuelto(recibido: int, compra: int) -> tuple[list[int], list[int]] | int:
    """
    contrato

    Calcula cuántos billetes de cada denominación hay que entregar de
    vuelto, usando la menor cantidad de billetes posible. Si el dinero
    recibido no alcanza para pagar la compra, o si el vuelto no se
    puede armar con los billetes disponibles, se avisa mediante un
    código de error en vez de devolver los billetes.

    pre: recibido y compra son numeros enteros
    post: devuelve una tupla con la lista de denominaciones de billetes y la cantidad a entregar de cada una minimizando la cantidad de billetes; devuelve -1 si el vuelto no se puede formar con las denominaciones disponibles; devuelve -2 si el dinero recibido es insuficiente
    """
    if recibido < compra:
        return -2
    else:
        vuelto = recibido - compra
        billetes = [5000,1000,500,200,100,50,10]
        cant_billetes = []
        for denominacion in billetes:
            resultado_billetes = vuelto // denominacion
            cant_billetes.append(resultado_billetes)
            vuelto = vuelto % denominacion
        if vuelto != 0:
            return -1
        else:
            return billetes, cant_billetes

def main() -> None:
    compra = int(input("Ingrese el total de la compra: "))
    recibido = int(input("Ingrese el dinero recibido: "))

    resultado = calcular_vuelto(recibido, compra)

    if resultado == -1:
        print("No se pudo dar vuelto exacto")
    elif resultado == -2:
        print("El dinero no es suficiente")
    else:
        billetes, cant_billetes= resultado
        for bil,cant in zip(billetes, cant_billetes, strict = True):
            print(f"Billetes de ${bil}: {cant}")

    
if __name__ == "__main__":
    main()
