"""
Faça um programa que peça uma nota, entre zero e dez. Mostra uma mensagem caso o 
valor seja inválido e continue pedindo até que o usuário informe um valor válido
"""
nota = float(input('Digite uma nota entre zero e dez: '))

while nota < 0 or nota > 10: 
    nota = float(input('Você digitou uma nota incorreta. Digite uma nota entre zero e dez: '))
else:
    print('Nota válida!')
