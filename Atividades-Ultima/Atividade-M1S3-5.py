#Atividade Semana 3 modulo 1
#Faça um programa com uma função que necessite de um parâmetro. A função deve retornar "Positivo", se o seu numero for maior que zero, "Negativo" se o número dor menor que zero, e "Zero" se o número for igual a zero.

def posivito_negativo_zero(numero):
    if numero > 0:
        print('Positivo')
        return 'Positivo'
    elif numero < 0:
        print('Negativo')
        return 'Negativo'
    elif numero == 0:
        print('Zero')
        return 'Zero'
numero = int(input('Digite um valor: '))
posivito_negativo_zero(numero)