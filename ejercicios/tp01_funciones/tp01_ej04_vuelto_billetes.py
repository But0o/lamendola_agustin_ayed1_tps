def calcular_vuelto(recibido,compra):
    if recibido < compra:
        return -2
    else:
        vuelto = recibido - compra

        billetes_5000 = vuelto // 5000
        vuelto = vuelto % 5000

        billetes_1000 = vuelto // 1000
        vuelto = vuelto % 1000

        billetes_500 = vuelto // 500
        vuelto = vuelto % 500

        billetes_200 = vuelto // 200
        vuelto = vuelto % 200

        billetes_100 = vuelto // 100
        vuelto = vuelto % 100

        billetes_50 = vuelto // 50
        vuelto = vuelto % 50

        billetes_10 = vuelto // 10
        vuelto = vuelto % 10

        if vuelto != 0:
            return -1
        else:
            return billetes_5000, billetes_1000, billetes_500, billetes_200, billetes_100, billetes_50, billetes_10


def main():
    compra = int(input("Ingrese el total de la compra: "))
    recibido = int(input("Ingrese el dinero recibido: "))

    resultado = calcular_vuelto(recibido, compra)

    if resultado == -1:
        print("No se pudo dar vuelto exacto")
    elif resultado == -2:
        print("El dinero no es suficiente")
    else:
        billetes_5000, billetes_1000, billetes_500, billetes_200, billetes_100, billetes_50, billetes_10 = resultado

        print(f"Billetes de $5000: {billetes_5000} \nBilletes de $1000: {billetes_1000} \nBilletes de $500: {billetes_500} \nBilletes de $200: {billetes_200} \nBilletes de $100: {billetes_100} \nBilletes de $50: {billetes_50} \nBilletes de $10: {billetes_10}")

    
if __name__ == "__main__":
    main()