#Aula de Funções ao vivo 
def minha_primeira_funcao(nome):
    print(f'Seja bem-vindo {nome}')

nome = 'Samuel'
minha_primeira_funcao(nome)

def soma(x, y):
    resultado = x + y
    print(f'{resultado}')
    return resultado

x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
soma(x, y)
res = soma(x, y)
print(f'{res}')

# Retorna de uma pessoa e adulto ou criança dada uma determinada idade.
def maior_de_idade(idade):
    if idade >= 18:
        return 'Adulto'
    else:
        return 'Adolecente/criança'

idade = int(input('Digite sua idade: '))

saida = maior_de_idade(idade)
print(f'{saida}')

#Função cadastro de usuário
def cadastro_usuario():
    nome = str(input('Digite seu nome: '))
    cpf = int(input('Digite seu CPF: '))
    idade = int(input('Digite sua idade: '))
    print(f'Nome: {nome} CPF: {cpf} Idade: {idade}')

def maior_de_idade(idade):
    if idade >= 18:
        return 'Adulto'
    else:
        return 'Adolecente/criança'
    
while True:
    opcao = int(input('O que você desja? 1- Cadastro de usuário, 2- Finalizar Programa '))

    if opcao == 1:
        nome, cpf, idade = cadastro_usuario()
        saida = maior_de_idade(idade)
        print(saida)
    elif opcao == 2:
        print('Programa finalizado')
        break

def soma(*valores):
    tot = 0
    for num in valores:
        tot = tot + num
        print(num)
soma(5, 4, 3, 6)
