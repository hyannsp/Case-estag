# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
def verify_a(string):
    count = 0
    for simbol in string.lower():
        if simbol == 'a':
            count +=1
    
    if count > 0:
        return f"A palavra {string} tem {count} letras a(s)"
    else:
        return f"A palavra {string} não tem letras a's"