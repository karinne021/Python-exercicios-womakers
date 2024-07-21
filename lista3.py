
# 1
print('Questão 1\n')
lista = []
print('Responda com "S" para Sim, e "N" para Não')
lista.append(input('Telefonou para a vítima? '))
lista.append(input('Esteve no local do crime? '))
lista.append(input('Mora perto da vítima? '))
lista.append(input('Devia para a vítima? '))
lista.append(input('Já trabalhou com a vítima? '))



cont_sim = 0

for i in lista:
    if i == 'S':
        cont_sim += 1


if cont_sim == 2:
    print('\nSuspeita')
elif cont_sim >= 3 and cont_sim < 5:
    print('\nCúmplice')
elif cont_sim == 5:
    print('\nAssasino!')
else:
    print('\nInocente')

print('\n------------\n')



# 2
print('Questão 2\n')
media = []
nota = 0
contador_2 = 1
contador = 1

while contador < 6:
    while contador_2 < 5:
        nota += float(input(f'Digite a nota {contador_2} do aluno {contador}: ')) 
        contador_2 += 1
    media.append(nota/4)
    nota = 0
    contador_2 = 1
    contador += 1

aprovado = 0
for i in media:
    if i >= 7:
       aprovado += 1

print(f'\n{aprovado} alunos aprovados!') 

print('\n------------\n')

# 3
print('Questão 3\n')
compras = {}
compras['Blusa'] = 35.00
compras['Vestido'] = 80.00
compras['Sapato'] = 154.00
print('\nCARRINHO DE COMPRAS')
print(f'O valor é de R${sum(compras.values())}')

print('\n------------\n')

# 4
print('Questão 4\n')
agenda = {'Ana':'9999999', 'Karinne':'97362753', 'Maria':'11111111'}

print(agenda.keys())
nome = input('Qual contato gostario de procurar? ')

if nome in agenda:
    print('O telefone é: ', agenda.get(nome))

print('\n------------\n')

# 5
print('Questão 5\n')
tupla1 = ('1', '2', '3')
tupla2 = ('4', '5', '6')

nova_tupla = tupla1 + tupla2

print(nova_tupla)
print('\n------------\n')

# 6
print('Questão 6\n')
nome = input('Digite o seu nome: ')

nome_invertido = nome[::-1]

print(nome_invertido.upper())

print('\n------------\n')