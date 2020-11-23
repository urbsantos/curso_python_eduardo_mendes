# Faça um programa que peça 2 números e um número float. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo
# A soma do triplo do primeiro com o terceiro
# O terceiro elevado ao cubo

numero_1 = int(input('Digite o primeiro número, número inteiro: '))
numero_2 = int(input('Digite o segundo número, número inteiro: '))
numero_3 = float(input('Digite o terceiro número, número float: '))

resutaldo_1 = (numero_1 * 2) * (numero_2 / 2)

resultado_2 = (numero_1 * 3) + numero_3

resultado_3 = numero_3 ** 3

print(f'Resultado 1: {resutaldo_1}')
print(f'Resultado 2: {resultado_2}')
print(f'Resultado 3: {resultado_3:.2f}')
