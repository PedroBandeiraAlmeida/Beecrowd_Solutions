lista = [1, 2, 3]

def myfunc(lista):
    total = 0
    for n in lista:
        total = total + n
    print(total)

myfunc(lista)

#como imprimir um numero aleatorio
import random

print(random.randrange(1, 10))

"""Aqui eu consigo receber 6 entradas no sistema, graças ao range, depois ele vai fazendo os if"""
quantidade = 0
for i in range(6):
    if float(input()) > 0.0:
        quantidade = quantidade + 1

print(quantidade, "valores positivos")
