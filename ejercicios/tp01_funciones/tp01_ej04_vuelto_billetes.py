def calcular_vuelto(recibido,compra):
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

def main():
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