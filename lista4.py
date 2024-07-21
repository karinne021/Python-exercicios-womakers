def soma(a, b, c):
    soma = a + b + c
    print(f'A soma é: {soma}')


def reverso(num):
    num_reverso = int(str(num)[::-1])
    print(f'O reverso do número é: {num_reverso}')


def converte_fahrenheit(temp):
    f = (temp * (9/5))+32
    print(f'{temp}°C corresponde a {f:.2f}°F')

def converte_celsius(temp):
    c = (temp - 32)*(5/9)
    print(f'{temp}°F corresponde a {c:.2f}°C')

def menu(temp):
    escolhe_op = int(input('Escolha a opção que deseja converter: \n1 - °C para °F\n2 - °F para °C\n'))
    if (escolhe_op == 1):
        converte_fahrenheit(temperatura)
    elif (escolhe_op == 2):
        converte_celsius(temperatura)
    else:
        print('Opção inválida!')


def conversao_moeda(valor):
    print('A quantidade de moeda estrangeira que poderia comprar é: ')
    print(f'Dólar Americano: {(valor / 4.91):.2f}')
    print(f'Peso Argentino: {(valor / 0.02):.2f}')
    print(f'Dólar Australiano: {(valor / 3.18):.2f}')
    print(f'Dólar Canadense: {(valor / 3.64):.2f}')
    print(f'Franco Suíco: {(valor / 0.42):.2f}')
    print(f'Euro: {(valor / 5.36):.2f}')
    print(f'Libra esterlina: {(valor / 6.21):.2f}')


def contar_vogais(frase):
    frase = frase.upper()
    vogais = "AEIOU"
    cont_vogais = 0
    for letra in frase:
        if letra in vogais:
            cont_vogais += 1
    print(f'Contém {cont_vogais} vogais na frase')


def jogo_forca():
    import os
    import random

    lista_palavras = ['livro','lago','uva','praia','ceu']

    palavra_secreta = random.choice(lista_palavras)

    tamanho = len(palavra_secreta)
    letras_acertadas = ''

    condicao = True
    count = 0

    while count < 6:
        
        letra = input('Digite uma letra: ')
        count += 1

        if len(letra) > 1:
            print('Digite apenas uma letra!')
            continue

        
        if letra in palavra_secreta:
            letras_acertadas += letra

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('clear')
            print(f'Você acertou!\nA palavra secreta era {palavra_secreta}')
            exit

    if palavra_formada != palavra_secreta:
        print(f'Você perdeu!\nA palavra era: {palavra_secreta}')




# 1
print('\nQuestão 1\n')
num1 = float(input('Entre com o primeiro valor: '))
num2 = float(input('Entre com o segundo valor: '))
num3 = float(input('Entre com o terceiro valor: '))
soma(num1, num2, num3)

print('\n---------------\n')


# 2
print('\nQuestão 2\n')
num_reverso = int(input('Forneça um número para obter o inverso: '))
reverso(num_reverso)
print('\n---------------\n')

# 3
print('\nQuestão 3\n')
temperatura = float(input('Entre com o valor da temperatura: '))
menu(temperatura)
print('\n---------------\n')

# 4
print('\nQuestão 4\n')
valor = float(input('Entre com o valor em dinheiro que tem em carteira: '))
conversao_moeda(valor)
print('\n---------------\n')

# 5
print('\nQuestão 5\n')
frase = input('Entre com uma frase: ')
contar_vogais(frase)
print('\n---------------\n')


# 6
print('\nJOGO FORCA\n')
jogo_forca()

