"""
Faça um programa que itera uma string e toda vez que uma vogal aparecer na sua tela, 
print o seu nome entre as letras

"""

palavra = 'abracadabra'
vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        print('Urbano')
    else:
        print(letra)
