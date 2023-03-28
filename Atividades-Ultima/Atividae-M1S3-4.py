#Atividade Semana 3 Modulo 1
#Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário com entrada, permitindo soma qualquer contidade de dados de entrada.

#Atividade concluída Utilizando funçao e laço While
def soma_num(numero):
    soma = 0
    while numero != -1:
        soma = soma + numero
        numero = int(input('Digite um valor ou [-1] para finalizar: '))
    print(soma)
numero = int(input('Digite um valor ou [-1] para finalizar: '))
soma_num(numero)