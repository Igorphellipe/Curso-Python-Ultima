#Atividade Semana 3 Modulo 1
#|Crie uma função que ao receber um número inteiro retorna se um número impar ou par

def par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
        #print(f'O {numero} é par')
    else:
        #print(f'O {numero} é impar')
        return 'Impar'

numero = int(input('Digite um número: '))

print(par_impar(numero))
