a, b, c, d = map(int, input().split())

def impressao():
    print(f"O JOGO DUROU {horas} HORA(S) E {minuto} MINUTO(S)")

inic = a * 60 + b
final = c * 60 + d

temp = final - inic

if temp <= 0:
    temp += 24 * 60

horas = temp // 60
minuto = temp % 60
impressao()