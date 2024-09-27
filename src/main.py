from functions.exercicio1 import in_fibo
from functions.exercicio2 import verify_a

def main():
    option = -1
    while option != 0:
        print("Case para Python, selecione um exercício:")
        print("1 - Verificar se número pertence à sequência de Fibonacci")
        print("2 - Verificar se existe 'a' em uma string ")
        
        try:
            option = int(input("Escolha uma opção (0 a 2): "))

        except ValueError:
            print("Por favor, insira um número válido.")
            return

        match option:
            case 1:
                number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
                result = in_fibo(number)
                print(result)

            case 2:
                string = input("Insira sua string para verificar se existe letras a's: ")
                result = verify_a(string)
                print(result)

            case 0:
                continue

            case _:
                print("Opção inválida. Escolha um número de 0 a 2.")

if __name__ == "__main__":
    main()