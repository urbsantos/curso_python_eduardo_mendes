"""
Dada uma lista de entradas de usuário de números inteiros, construa um
dicionário com a lista padrão, a lista dos valores elevados ao quadrado
e a lista dos valores elevados ao cubo.
"""

def eleva_numero(lista_valores, numero_elevado):
    lista_resposta = []
    for numero in lista_valores:
        lista_resposta.append(numero ** numero_elevado)
    
    return lista_resposta


lista_valores = []

for digitar_valor in range(10):
    lista_valores.append(int(input('Fala um número aí: ')))


dicionario = {
    'lista padrão': lista_valores,
    'lista quadrada': eleva_numero(lista_valores, 2),
    'lista cúbica': eleva_numero(lista_valores, 3)
}

print(dicionario)
