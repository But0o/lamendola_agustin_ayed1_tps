def mayor_unico(num1: int, num2: int, num3: int) -> int:
    """
    contrato

    Busca cuál de los tres números es el más grande, pero solo lo entrega
    si es mayor que los otros dos sin empatar con ninguno de ellos.
    Si hay un empate en el primer puesto, se considera que no existe
    un mayor único.

    pre: num1, num2 y num3 son numeros enteros positivos
    post: devuelve el mayor de los tres solo si es unico (mayor estricto), o -1 si no hay un mayor unico
    """
    if num1 > num2:
        if num1 > num3:
            return num1
    if num2 > num1:
        if num2 > num3:
            return num2
    if num3 > num1:
        if num3 > num2:
            return num3
    return -1

def main() -> None:
    num1 = int(input("Ingresar un numero : "))
    num2 = int(input("Ingresar un numero : "))
    num3 = int(input("Ingresar un numero : "))

    mayor = mayor_unico(num1, num2, num3)
    if mayor_unico(num1,num2,num3) == -1:
        print("No hay numero mayor unico")
    else:
        print(f"El numero mayor es {mayor}")

if __name__ == "__main__":
    main()
