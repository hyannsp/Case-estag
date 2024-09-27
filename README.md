# Case para candidatura
## Técnica:

### 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

### 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

### 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

**Ao final do processamento, qual será o valor da variável SOMA?**  
**R:** Ao final do processamento, soma será igual a 77! Visto que a iteração repetirá 11 vezes e somar a própria variável com o fator iterativo. 0+2=2; 2+3=5; 5+4=9; ... 65 + 12 = 77.
### 4) Descubra a lógica e complete o próximo elemento:
    a) 1, 3, 5, 7, ___
    b) 2, 4, 8, 16, 32, 64, ____
    c) 0, 1, 4, 9, 16, 25, 36, ____
    d) 4, 16, 36, 64, ____
    e) 1, 1, 2, 3, 5, 8, ____
    f) 2,10, 12, 16, 17, 18, 19, ____

**R:**  
    a) 9 (numeros impares)
    b) 128 (2^n)
    c) 49 (n²)
    d) 100 (n par²)
    e) 13 (Fibonacci)
    f) 20
### 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  
**R:** Deve-se ligar uma lâmpada e esperar o suficiente para que ela fiquei quente. Em seguida apagar e ligar outra e ir para uma sala qualquer. Caso esteja ligada, é do segundo interruptor, caso esteja quente, do primeiro, se não do terceiro. Assim descobre-se qual interruptor pertence àquele quarto, em seguida acenda a lâmpada de outro interruptor e deixe apagada a do que restar e entre em outro quarto, assim é possível descobrir qual lâmpada pertence a qual quarto.