# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preco_1 = float(input('Preço 1: '))
preco_2 = float(input('Preço 2: '))
preco_3 = float(input('Preço 3: '))

if preco_1 < preco_2 and preco_1 < preco_3:
    print('Compre o 1')
elif preco_2 < preco_1 and preco_2 < preco_3:
    print('Compre o 2')
else:
    print('Compre o 3')
