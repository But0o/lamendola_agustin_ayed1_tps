def concatenar_num(num1: int, num2: int) -> int:
    """
    contrato

    Une dos números enteros positivos uno a continuación del otro,
    como si fueran texto, y devuelve el número que resulta de esa
    unión. Si alguno de los dos números no es positivo, avisa que
    los datos no son válidos.

    pre: num1 y num2 son numeros enteros positivos
    post: devuelve el numero resultante de concatenar num1 y num2; devuelve -1 si alguno de los dos no es positivo
    """
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


def main() -> None:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese otro numero: "))
    resultado = concatenar_num(num1,num2)
    if resultado == -1:
        print("Los numeros ingresados no son validos")
    else:
        print(f"El resultado de la concatenacion es: {resultado}")

if __name__ == "__main__":
    main()
