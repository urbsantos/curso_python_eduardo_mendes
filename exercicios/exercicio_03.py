# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# de um litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas
# e o preço total.

tamanho_metros_quadrados = float(input('Tamanho em metros quadrados: '))

quantidade_latas_de_tinta = 1 + ((tamanho_metros_quadrados / 3) // 18)
valor_total_tinta = quantidade_latas_de_tinta * 80

print(f'A quantidade de latas de tinta necessárias é: {quantidade_latas_de_tinta:.2f}')
print(f'O preço total gasto em tinta será: {valor_total_tinta:.2f}')
