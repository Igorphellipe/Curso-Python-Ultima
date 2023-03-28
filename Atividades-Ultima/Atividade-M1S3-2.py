#Atividade Semana 3 Modulo 1
#Crie uma função que recebe um numéro inteiro por parâmetro e então imprime na tela do número recebido até o zero.
#Contando de Número ate zero utilizando funções - Laço For
print('-=-' * 15)
print('Contegem utilizando função e laço For')
def mostra_ate_zero(numero):
    for numero in range(numero,-1,-1):
        print(numero)

numero = int(input('Digite um valor: '))
mostra_ate_zero(numero)

#Contando de Número ate zero utilizando funções - Laço While
print('-=-' *15)
print('Contagem utilizando função e laço while')
def mostra_ate_zero(numero):
    while numero >= 0:
        print(numero)
        numero = numero - 1
numero = int(input('Digite um número: '))
mostra_ate_zero(numero)