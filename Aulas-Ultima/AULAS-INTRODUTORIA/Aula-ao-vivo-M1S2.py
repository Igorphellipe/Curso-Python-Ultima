#Introdução
#Input - solicita uma entrada de dados do usuario atraves do teclado
#nome = input('Digite seu nome: ')
#Print - imprime valores atribuidos a variáveis 
#print('Olá:', nome)

#Variáveis (tipos)

nome = 'Igor' #<class 'str'>
print(nome, type(nome))

num_r = 3.14159 #<class 'flaot'>
print(num_r, type(num_r))

num_i = 5 #<class 'interger'>
print(num_i, type(num_i))

#Operadores Aritméticos (+ - / * ** %)
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
print(x, y, 'Resultado:', x ** y)
x = 5
y = 2
print(x + y)
print(x - y)
print(x * y)
print(x / 2)
print(x ** y)
print(x % y)

#Mostrando valores contindo em uma variavel - Usando Pi, .format ou f
pi = 3.14159
print('O valor de PI é ', pi)
print('O valor de PI é {}'.format(pi))
print(f'O valor de PI {pi:.3f}')

# Operadores de comparação (> < >= <= == != )
x = 5
y = 2
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)

senha = 'minha_senha'
tentativa = 'jogao'
print(senha == tentativa)

#Operadores logicos (AND OR NOT)
# AND -> "E": Retorna True se todas as entradas são True.
print(False and False)
print(False and True)
print(True and False)
print(True and True)

#OR -> "OU": Retorna True se pelo MENOS UMA das entradas é True.
print(False or False)
print(False or True)
print(True or False)
print(True or True)

#NOT -> "NÂO": Inverte a entrada.
print(not False)
print(not True)

#Estruturas Condicionais (If Else Elif)
chovendo = True
gasolina = False
dinheiro = True
if chovendo:
    print('Ficar em casa!')
    if dinheiro:
        print('Pedir uma Pizza!')
    else:
        print('Preparar miojo!')
else:
    if gasolina:
        print('Vou á praia!')
    else:
        print('Abastecer o carro!')

idade = 66
if idade > 0 and idade < 13:
    print('Criança')
elif idade >= 13 and idade < 18:
    print('Adolescente')
elif idade >= 18 and idade < 65:
    print('Adulto')
elif idade >= 65:
    print('Idoso')
else: 
    print('Idade inválida!')

#Estruturas de Repetição (FOR WHILE)
inicio = 0
while inicio < 3:
    print('Entrou no WHILE', inicio)
    inicio = inicio + 1


#Indice 01234567...
nome = 'André Ferreira'

indice = 0
while indice < 5:
    print(nome[indice])
    indice = indice + 1

inicio = 0
fim = 3
incremento = 1
while inicio < fim:
    print(inicio)
    inicio = inicio + incremento

for indice in range(0, 3, 1): #(inicio, fim, incremento)
    print(indice)