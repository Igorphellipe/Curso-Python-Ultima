# While condicional executa ate que a condicional seja falsa
print('INICIO')
soma = 0
while soma < 100:
    soma = soma + 11
    print(f'Soma = {soma}')
print('FIM')

#Testando laços While
print('-=-' * 10)
valor = 1
while valor <= 5:
    print(f'O valor é: {valor}')
    valor = valor + 1
print('FIM')

#Testando instruções de Continue e Break
print('-=-' * 10)
numero = 0
while numero <= 1000:
    if numero % 2 != 0:
        numero = numero + 1
        
    print(f'O número {numero} é PAR!')

    if numero == 10:
        print('Ops... já verifiquei muitos números pares!')
        break

    numero = numero + 1
print('FIM')