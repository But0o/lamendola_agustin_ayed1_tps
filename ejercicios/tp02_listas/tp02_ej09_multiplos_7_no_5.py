a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro numero: "))

resultado = [x for x in range(a,b+1) if x % 7 == 0 and x % 5 != 0]

print(resultado)