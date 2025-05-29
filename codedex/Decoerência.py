n = int(input())
s = input().strip()
t = input().strip()

superposicao = 0
colapso = 0

for i in range(n):
    if s[i] == "*":
        superposicao += 1
        if t[i] != "*":
            colapso += 1
taxa = colapso / superposicao

print(f"{taxa:.2f}")