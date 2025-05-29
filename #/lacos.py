#LISTA
lista = [1, 2, 3, 4, 5]

for item in lista:
    print(item)
#VAI RETORNAR ISSO
'''
1
2
3
4
5
'''
    
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#VAI RETORNAR ISSO
'''
apple
banana
cherry
'''
#NESSE CASO VAI PERCORRER A LISTA COMPLETA, MAS SE FOSSE SÓ ATÉ UM DETERMINADO NUMERO DE ITENS, ERA SÓ
#COLOCAR O NUMERO NO RANGE
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
## dicionario
notas = {
    'Potuguês': 7, 
    'Matemática': 9, 
    'Lógica': 7, 
    'Algoritmo': 7
}

for chave, valor in notas.items():
    print(f"{chave}: {valor}")


for caractere in 'Python':
    print(caractere)


contador = 0

while contador < 10:
    print(f'Valor do contador é {contador}')
    contador += 1 #mesma coisa que contador = contador +1

contador = 0

while contador < 10:
    contador += 1
    print(f'Valor do contador é {contador}')    
else:
    print(f'Fim do while e o valor do contador é {contador}')
    



#while com input

x = int(input())

contador = 0
while (contador < x):
    contador = contador + 1
    if contador % 2 != 0:
        print(contador)