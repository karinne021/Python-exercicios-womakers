
# 1
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))


print(f'A soma é: {numero1+numero2}')
print(f'A subtração é: {numero1-numero2}')
print(f'A multiplicação é: {numero1*numero2}')
print(f'A divisão é: {numero1/numero2}')

# 2
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
print(f'Sua idade é: {2024-ano_nascimento} anos')

# 3
km = float(input('Digite a quantidade de quilômetros: '))
print(f'Metros: {km*1000}, Centímetros: {km*100000}, Milímetros: {km*1000000}')

# 4
litros = float(input('Digite a quantidade de litros de combustível: '))
distancia = float(input('Digite a distância percorrida: '))

print(f'O consumo médio é de {(distancia/litros):.2f}km/l')

# 5
distancia_viagem = float(input('Digite a distancia da viagem: '))
print(f'De avião a viagem levará {(distancia_viagem/600):.2f} horas\nDe carro a viagem levará {(distancia_viagem/100):.2f} horas\nDe ônibus a viagem levará {(distancia_viagem/80):.2f} horas')

# 6
peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura em metros: '))

print(f'O Índice de Massa Corporal (IMC) é {(peso/(altura*altura)):.2f}')

# 7
ganho_horas = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês: '))

print(f'O seu salário do mês é de: R${(ganho_horas*horas_trabalhadas):.2f}')

# 8
horas_exercicio = float(input('Digite a quantidade de horas de exercício físico praticados na semana: '))
print(f'A quantidade de calorias queimadas foi de {(horas_exercicio*60)*5}')

# 9
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
cidade = input('Digite qual a sua cidade: ')
area = input('Digite qual o seu curso: ')

print(f'Olá {nome}! Sua idade é {idade}, você é da cidade de {cidade} e estuda {area}')