a, b = map(int, input().split())

if b > a:
    tempo = b - a
    print(f"O JOGO DUROU {tempo} HORA(S)")

else:
    
    tempo = (24 - a) + b
    print(f"O JOGO DUROU {tempo} HORA(S)")