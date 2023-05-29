print('-=-' * 10)
print('\033[1;4mOPERADORES BOOLEANOS\033[m')
print('-=-' * 10)
 
#Verifando valor maior que 60 e impar:
numero = 63

if numero > 60 and numero % 2 == 1:
    print(f'O {numero} e maior que 60 é Impar!')

#Operador AND e suas combinações:
print('-=-' * 10)
print('Operador AND e suas combinações')

combinações = [(True, True), (True, False), (False, True), (False, False)]

for x, y in combinações:
    print(f'{x} and {y} -> {x == y}')

#Operador OR e suas combinações:
print('-=-' * 10)
print('Operador Or e suas combinações')
combinações = [(True, True), (True, False), (False, True), (False, False)]

for x, y in combinações:
    print(f'{x} OR {y} -> {x or y}')

#Operador NOT e suas combinações:
print('-=-' * 10)
print('Operador NOT e suas combinações')

combinações = [True, False]

for x in combinações:
    print(f'NOT {x} -> {not x}')

#Combinando expressões booleanas:
print('-=-' * 10)
print('Combinando operações booleanas')
pode_parcelar = True
valor = 1500
limite = 1400

print(f'Valor do produto: R${valor}')
print(f'Limite do cartão: R${limite}')

if (pode_parcelar or valor < 2000) and limite >= valor:
    print('Vou comprar')
else:
    print('Puts, ainda não posso comprar')