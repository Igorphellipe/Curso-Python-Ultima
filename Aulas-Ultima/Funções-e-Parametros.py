#Aula de Funções e Parâmetros Basiscos em Python
#Existem dois tipos basicos de função
#1º Funções defindas pelo Usuário - São indentificadas pelo usário para executar uma tarefa específica.
#2º Funções embutidas -funções pré-definidas em python

#Função definda pelo usuário, solicitando entrada de dados pelo teclado
#Função para atribuir nomes a um texto de boas vindas com entrada de dado pelo teclado.
print('-=-' * 15)
print('Usando função para mostrar uma mensagem atraves de entrada pelo telcado')
def apresentação (nome, idade):
    print(f'Olá {nome}, você tem {idade} anos' )
nome = str(input('Digte seu nome: '))
idade = int(input('Digite sua idade: '))

apresentação(nome, idade)

#Função para somar dois valores
print('-=-' * 15)
print('Usando função para soma de dois valores digitados pelo teclado')
def soma(num1, num2):
    return num1 + num2
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

total = soma(num1, num2)
print(total)


#Função calculo expoente:
print('-=-' * 15)
print('Usando função para mostrar um valor elevado ao expoente digitado pelo usuario ')
def potencia(x, expoente=2):
    return x ** expoente
x = int(input('Digite um valor: '))
expoente = int(input('Digite um numero de potencia: '))

resultado = potencia(x, expoente)
print(resultado)

#Função para calculo de juros simples
print('-=-' * 15)
print('Calculando Juros de emprestimos com Função')
def juros_simples(capital, taxa, tempo):
    return capital * (taxa / 100) * tempo
capital = float(input('Digite o valor do emprestimo: '))
taxa = float(input('Digite o valor da taxa de juros: '))
tempo = int(input('Digite o tempo para pagamento: '))
juros = juros_simples(capital, taxa, tempo)
total = capital + juros
print(f'O valor a ser emprestado é R${capital:.2f}')
print(f'Sua taxa de juros e de {taxa}%')
print(f'O valor total do emprestimo fica em R${total}')

#Função que aceita inumeros argumentos
print('-=-' * 15)
print('Criando função que aceita inumeros argumentos do tipo string')
def mistura_palavras(*args):
    return '_'.join(args)

letras = mistura_palavras('a','b')
print(letras)
letras = mistura_palavras('jose','foi', 'a', 'praia')
print(letras)
letras = mistura_palavras('q','w','e','r','t')
print(letras)
#Testando funçoes junto com variaveis e utilizando menu para mostrar o funcionamenta das funçoes criadas
def dados(nome, telefone, cpf):
    print('CADASTRO DE CLIENTE')
    print(f'NOME: {nome}')
    print(f'TEL: {telefone}')
    print(f'CPF: {cpf}')

def lista(*args):
    print('Lorem Ipsum é simplesmente um texto fictício da indústria tipográfica e de impressão. Lorem Ipsum tem sido o texto fictício padrão da indústria desde os anos 1500, '
          '\nquando um impressor desconhecido pegou uma galera de tipos e os embaralhou para fazer um livro de espécimes de tipos. Ele sobreviveu não apenas a cinco séculos, '
          '\nmas também ao salto para a composição eletrônica, permanecendo essencialmente inalterado. '
          '\nFoi popularizado na década de 1960 com o lançamento de folhas Letraset contendo passagens de Lorem Ipsum e, mais recentemente, '
          '\ncom software de editoração eletrônica como Aldus PageMaker, incluindo versões de Lorem Ipsum.')
    return

print('Cadastrando novos cliente:')
nome = str(input('Digite seu nome: '))
telefone = int(input('Digite seu telefone: '))
cpf = int(input('Digite seu CPF: '))

print('SELECIONE UMA DAS OPÇÕES:')
while True:
    resp = int(input('CADASTRO [1] '
                     'CONTRATO [2]'
                     ' SAIR [3]'))
    if resp == 1:
        cadastro = dados(nome, telefone, cpf)
        print(cadastro)
    if resp == 2:
        contrato = lista()
        print(contrato)
    elif resp == 3:
        break
print('teste')