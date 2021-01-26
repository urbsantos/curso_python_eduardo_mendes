def soma(numero_1, numero_2):
    return numero_1 + numero_2

def media(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)


def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relatório parcial

    Nome: {nome}
    CPF: {cpf}
    Telefone: {telefone}
    """

print(imprime_relatorio('Urbano Santos', 123456789, 999991234))
