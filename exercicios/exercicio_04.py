# Faça um programa que peça 2 números e um número float. Calcule e mostre:

# O produto do dobro do primeiro com metade do segundo
# A soma do triplo do primeiro com o terceiro
# O terceiro elevado ao cubo

numero_1 = int(input('Digite o primeiro número, número inteiro: '))
numero_2 = int(input('Digite o segundo número, número inteiro: '))
numero_3 = float(input('Digite o terceiro número, número float: '))

produto_dobro_primeiro_metade_segundo = (numero_1 * 2) * (numero_2 / 2)

soma_triplo_primeiro_terceiro = (numero_1 * 3) + numero_3

terceiro_elevado_cubo = numero_3 ** 3

print(f'Resultado 1: {produto_dobro_primeiro_metade_segundo}')
print(f'Resultado 2: {soma_triplo_primeiro_terceiro}')
print(f'Resultado 3: {terceiro_elevado_cubo:.2f}')
