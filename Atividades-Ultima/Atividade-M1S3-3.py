#Atividade Semana 3 Modulo 1
# Crie um programa com uma função que necessite de três parâmetros e então retorne sua soma.

def soma_3_numeros(a, b, c):
    return a + b + c

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
print(soma_3_numeros(a, b, c))