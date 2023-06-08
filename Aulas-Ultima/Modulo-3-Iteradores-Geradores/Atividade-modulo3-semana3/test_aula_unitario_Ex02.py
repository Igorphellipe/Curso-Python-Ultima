#Aula de teste Unitario !
import pytest
'''
cardapio = """
   *******Cardápio*******
   ----------------------------------------------
   | Código | Descrição | Valor |
   | 100 | Cachorro Quente | 9,00 |
   | 101 | Cachorro Quente Duplo | 11,00 |
   | 102 | X-Ovo | 12,00 |
   | 103 | X-Salada | 12,00 |
   | 104 | X-Bacon | 14,00 |
   | 105 | X-Tudo | 17,00 |
   | 200 | Refrigerante Lata | 5,00 |
   | 201 | Chá Gelado | 4,00 |
   ----------------------------------------------
   """
print(cardapio)
codigos = []

#codigo = int(input('Digite o codigo do produto: '))

while True:
    if codigo in [101, 101, 102, 103, 104, 105, 200, 201]:
        codigos.append(codigo)
    else:
        print('Opção Invalidada:')

    print('Deseja pedir mais algo ?')
    print('Opçao = 1: Sim')
    print('Opção = 2: Sair')

    opcao = int(input())

    if opcao == 2:
        break

    #codigo = int(input('Digite o codigo do produto: '))
    '''
def venda_lanche(codigos):
    total = 0.0
    cardapio = {
     100: ("Cachorro Quente",  9.00),
     101: ("Cachorro Quente Duplo",  11.00),
     102: ("X-Ovo", 12.00),
     103: ("X-Salada", 12.00),
     104: ("X-Bacon", 14.00 ),
     105: ("X-Tudo", 17.00),
     200: ("Refrigerante Lata", 5.00),
     201: ("Chá Gelado", 4.00)
        }
    for codigo in codigos:
        if codigo in cardapio:
            produto, valor = cardapio[codigo]
            print(f'Você pediu um {produto} no valor de {valor:.2f}')
            total += valor
        else:
            print('Opção inválida!')
    return total
