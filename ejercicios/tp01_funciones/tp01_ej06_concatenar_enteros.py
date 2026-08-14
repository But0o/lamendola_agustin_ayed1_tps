def concatenar_num(num1,num2):
    copia = 0
    multiplicador = 1
    if num1 > 0 and num2 > 0:
        copia = num2
        while copia > 0:
            copia = copia // 10
            multiplicador = multiplicador * 10
        concatenado = num1 * multiplicador + num2
    else:
        return -1
    return concatenado


def main():
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = concatenar_num(num1,num2)
    if resultado == -1:
        print("Los numeros ingresados no son validos")
    else:
        print(f"El resultado de la concatenacion es: {resultado}")

if __name__ == "__main__":
    main()