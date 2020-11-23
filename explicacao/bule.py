2 > 3 # False
3 > 2 # True

type(True)
type(False)

nome_1 = 'Fausto'
idade_1 = 3
nome_2 = 'Maria'
idade_2 = 23
nome_3 = 'Fausto'
idade_3 = 45

nome_1 == nome_2 # False
nome_1 == nome_3 # True
nome_1 != nome_2 # True

nome_1 == nome_3 and idade_1 == idade_3 # False
nome_1 == nome_3 or idade_1 == idade_1 # True

not nome_1 == nome_3 # False
