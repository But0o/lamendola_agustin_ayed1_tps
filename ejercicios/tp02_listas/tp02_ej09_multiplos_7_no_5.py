"""
contrato

Busca, entre dos números ingresados por teclado, todos los que sean
múltiplos de 7 pero no de 5.

pre: a y b son numeros enteros ingresados por teclado
post: resultado contiene los numeros entre a y b (inclusive) que son multiplos de 7 y no de 5
"""
a: int = int(input("Ingrese un numero entero: "))
b: int = int(input("Ingrese otro numero: "))

resultado: list[int] = [x for x in range(a,b+1) if x % 7 == 0 and x % 5 != 0]

print(resultado)
