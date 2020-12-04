# Faça um programa que leia 5 números e informe o maior número

lista = []

while len(lista) < 5:    
    lista.append(int(input(f'Digite 5 número: ')))
print('O maior número é: ', max(lista))
