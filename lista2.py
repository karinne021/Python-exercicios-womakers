
# 1
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print(f'O maior valor é: {num1}')
elif num2 > num1:
    print(f'O maior valor é: {num2}')
else:
    print('Os números são iguais!')

# 2
turno = input('Digite o turno em que você estuda: \nM - matutino\nV - vespertino\nN - noturno\n')

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')

# 3
nota = int(input('Digite um valor entre 0 e 10: '))
while (nota < 0) or (nota > 10):
    nota = int(input('Valor inválido\nDigite um número entre 0 e 10: '))


# 4
nota = float(input('Digite o valor da nota: '))

if nota >= 7:
    print('Aprovado!')
else: 
    print('Reprovado!')


# 5
lado1 = int(input('Digite o valor do primeiro lado do triangulo: '))
lado2 = int(input('Digite o valor do segundo lado do triangulo: '))
lado3 = int(input('Digite o valor do terceiro lado do triangulo: '))

if lado1 == lado2 and lado1 == lado3:
    print('Triângulo Equilátero')
elif lado1 == lado2 and lado1 != lado3:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')

# 6
login = input('Digite o login: ')
senha = input('Digite a senha: ')

if login == 'admin' and senha == 'admin123':
    print('Acesso permitido!')
else:
    print('Acesso inválido!')

# 7
idade = int(input('Digite sua idade: '))

if idade > 0 and idade < 15:
    print('Criança')
elif idade >= 15 and idade < 18:
    print('Adolescente')
elif idade >= 18 and idade < 60:
    print('Adulto')
else:
    print('Idoso')


# 8
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print(f'O maior valor é: {num1}')
elif num2 > num1 and num2 > num3:
    print(f'O maior valor é: {num2}')
elif num3 > num1 and num3 > num2:
    print(f'O maior valor é: {num3}')
else:
    print('Os números são iguais!')

# 9
par = 0
impar = 0
num = int(input('Digite um número: '))

while num != 0:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    
    print(f'{impar} número(s) ímpar(es)')
    print(f'{par} número(s) par(es)')
    num = int(input('Digite um número: '))


# 10

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 < num2 < num3:
    print(f'{num1}\n{num2}\n{num3}')
elif num1 < num3 < num2:
    print(f'{num1}\n{num3}\n{num2}')
elif num2 < num1 < num3:
    print(f'{num2}\n{num1}\n{num3}')
elif num2 < num3 < num1:
    print(f'{num2}\n{num3}\n{num1}')
elif num3 < num1 < num2:
    print(f'{num3}\n{num1}\n{num2}')
elif num3 < num2 < num1:
    print(f'{num3}\n{num2}\n{num1}')



# 11
salario = float(input('Digite o valor do salário: '))

if salario <= 1903.98:
    print(f'Salário: R${salario}\nIsento de imposto de renda')
elif salario > 1903.98 and salario <= 2826.65:
    print(f'Salário: R${(salario - (0.075*(salario))):.2f}\nImposto de renda 7,5%')
elif salario > 2826.65 and salario <= 3751.05:
    print(f'Salário: R${salario - (0.15*(salario)):.2f}\nImposto de renda 15%')
elif salario > 3751.05 and salario <= 4664.68:
    print(f'Salário: R${salario - (0.225*(salario)):.2f}\nImposto de renda 22,5%')
else:
    print(f'Salário: R${salario - (0.275*(salario)):.2f}\nImposto de renda 27,5%')
