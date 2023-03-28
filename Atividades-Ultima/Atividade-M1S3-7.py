#Atividade Semana 3 Modulo 1
#Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. A letra desejada e a frase a ser verificada serão passadas por parâmetro para função, que retornará a quantidade da letra na frase.

def conta_letras(letra_buscada, frase):
    contagem = 0
    contagem = (frase.count(letra))
    return contagem

letra = str(input('Digite uma letra: '))
frase = str(input('Digite uma frase: '))
saída = conta_letras(letra, frase)
print(saída)