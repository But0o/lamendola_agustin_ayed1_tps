from random import randint as ran

"""
contrato

Genera una lista de números al azar y arma otra lista quedándose
solo con los impares, usando la función filter().

pre: no recibe parametros
post: lista_random contiene 10 numeros al azar entre 1 y 100; lista_impares contiene, usando filter(), los elementos impares de lista_random
"""
lista_random: list[int] = [ran(1,100) for _ in range(10)]

lista_impares = filter(lambda x: x % 2 != 0,lista_random)

print(lista_random)
print(list(lista_impares))
