def decimal_a_romano(numero: int) -> str:
    """
    contrato

    Convierte un número al sistema romano, restándole siempre el valor
    más grande posible y agregando el símbolo que le corresponde. Como
    los romanos no tenían un símbolo para el cero, ese caso queda vacío.

    pre: numero es un entero entre 0 y 3999
    post: devuelve una cadena con numero expresado en romano; si numero es 0 devuelve una cadena vacia
    """
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    romano = ""

    for i in range(len(valores)):
        while numero >= valores[i]:
            romano += simbolos[i]
            numero -= valores[i]

    return romano


def main() -> None:
    numero = int(input("Ingrese un numero entre 0 y 3999: "))

    print(decimal_a_romano(numero))


if __name__ == "__main__":
    main()

# ¿En que cambiaria la funcion si el rango de valores fuese diferente?
# hay que modificar las listas valores y simbolos. Para pasar de 3999 se
# agregan los valores mayores con sus simbolos.
