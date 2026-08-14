def mayor_unico(num1, num2, num3):
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

def main():
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
