salario = float(input())

salario_formatado = round(salario, 2)

if salario_formatado <= 400:
    new_salario = (salario_formatado * 0.15) + salario_formatado
    reajuste = salario_formatado * 0.15
    percentual = 15

elif salario_formatado >= 400.01 and salario_formatado <= 800:
    new_salario = (salario_formatado * 0.12) + salario_formatado
    reajuste = salario_formatado * 0.12
    percentual = 12

elif salario_formatado >= 800.01 and salario_formatado <= 1200:
    new_salario = (salario_formatado * 0.10) + salario_formatado
    reajuste = salario_formatado * 0.10
    percentual = 10

elif salario_formatado >= 1200.01 and salario_formatado <= 2000:
    new_salario = (salario_formatado * 0.07) + salario_formatado
    reajuste = salario_formatado * 0.07
    percentual = 7
else:
    new_salario = (salario_formatado * 0.04) + salario_formatado
    reajuste = salario_formatado * 0.04
    percentual = 4
   
print(f"Novo salario: {new_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
