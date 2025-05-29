print("Seja bem vindo a calculadora!")
print("escolhar uma operação:")
print("1 - Adição") 
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")

opcao = int(input("Digite a opção: "))
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

def add(a, b):
  soma = a + b
  return soma

def subtract(a, b):
  sub = a - b
  return sub

def multiply(a, b):
  multipli = a * b
  return multipli

def divide(a, b):
  divide = a / b
  return divide

def exp(a, b):
  potenci = a ** b
  return potenci

if opcao == 1:
    print(add(a, b))
    
elif opcao == 2:
        print("Resultado:", subtract(a, b))
elif opcao == 3:
    print("Resultado:", multiply(a, b))
elif opcao == 4:
    print("Resultado:", divide(a, b))
elif opcao == 5:
    print("Resultado:", exp(a, b))
else:
    print("Opção inválida!")


    