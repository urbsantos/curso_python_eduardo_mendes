"""
Faça um programa que: Dada uma lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e um número inteiro,
imprima a tabuada desse número.
"""

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resposta = int(input('Qual é o número? '))

for numero in lista_de_numeros:
    print(f'{numero} x {resposta} = {resposta * numero}')
