# IF = SE

# "Papai, você comprou pão?"
# se sim ou se não
# se comprou, ele vai agradecer
# se n comprou,ele vai chorar

pergunta = input('Papai, você comprou pão? ')
resposta = pergunta.lower()

if resposta == 'sim':
    print('Obrigado, papai!!')
elif resposta == 'não':
    print('Buáááá!!')
else:
    print('Resposta errada!! Escolha sim ou não!!!')
