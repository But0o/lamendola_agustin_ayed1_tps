from random import randint as ran

lista_random = [ran(1,100) for _ in range(10)]

lista_impares = filter(lambda x: x % 2 != 0,lista_random)

print(lista_random)
print(list(lista_impares))