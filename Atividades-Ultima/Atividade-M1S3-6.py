#Atividade Semana 3 Modulo 1
#Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.

def gorjeta(valor, porcentagem):
    return valor * (porcentagem / 100)
valor = float(input('Digite o valor da conta: R$'))
porcentagem = int(input('Digite a porcentagem do graçom: '))
resultado = gorjeta(valor, porcentagem)
print(f'{resultado:.2f}')