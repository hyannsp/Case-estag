# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Retorna uma array dos resultados em fibonacci até ultrapassar o número
def fibo(max):
    fibo_sequence = [0, 1]
    while fibo_sequence[-1] <= max: # Repete enquanto não ultrapassar o número definido
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence

def in_fibo(number):
    fib_sequence = fibo(number) # Retorna a array de números fibonacci
    
    # Verifica se o número existe na sequência
    if number in fib_sequence:
        return f'O número {number} pertence à sequência de Fibonacci.'
    else:
        return f'O número {number} não pertence à sequência de Fibonacci.'

