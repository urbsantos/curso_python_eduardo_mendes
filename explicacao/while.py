reposta = input('Bora dá um rolê? [s/n] ')

n = 0

while reposta != 's':
    reposta = input(f'Bora{"a" * n} [s/n]?? ')
    n += 1
    if 'chato' in reposta or 'chata' in reposta:
        print('Foi mal!!')
        break
else:
    print(f'Então, bora{"a" * n}!')
