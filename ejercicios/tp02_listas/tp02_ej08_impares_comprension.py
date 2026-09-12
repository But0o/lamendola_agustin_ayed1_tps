"""
contrato

Arma una lista con todos los números impares que hay entre 100 y
200, usando una comprensión de lista.

pre: no recibe parametros
post: lista_impares contiene todos los numeros impares comprendidos entre 100 y 200
"""
lista_impares: list[int] = [num for num in range(100,201) if not num % 2 == 0]

print(lista_impares)
