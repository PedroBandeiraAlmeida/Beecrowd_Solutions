import math
import time

y, k = map(int, input().split())

def parar(y, k):
    x = 1
    while True:
        parar = math.gcd(x, y)
        if parar == y:
            x += y * k
            break
        x += parar
        k -= 1
        if k == 0:
            break
    return x

print(parar(y, k))
