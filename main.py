#Questão 1:

INDICE = int(13)
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(f"O total é: {SOMA}")

#Questão 2:

def sequencia_fibonacci(n):
    sequencia_fib = [0, 1]
    while sequencia_fib[-1] < n:
        sequencia_fib.append(sequencia_fib[-1] + sequencia_fib[-2])
    return sequencia_fib

def esta_na_sequencia_fibonacci(numero):
    sequencia_fib = sequencia_fibonacci(numero)
    if numero in sequencia_fib:
        return True
    else:
        return False

numero = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

if esta_na_sequencia_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")


#Questão 5:

palavra = input("Escreva uma palavra para inverte-lá: ")

print(palavra[::-1])