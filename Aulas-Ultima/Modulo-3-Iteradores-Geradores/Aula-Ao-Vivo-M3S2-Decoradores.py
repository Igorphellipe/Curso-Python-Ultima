#Aula de Gerador
#Aula ao vivo
def sou_objeto():
    return 'Sim eu sou'
obj = sou_objeto()
print (obj)

def aquilo():
    return 'imprima aquilo'
def isso(tambem):
    msg = f'imprima isso, mas tambem {tambem}'
    print(msg)

isso(aquilo())

def calculadora(a, b):
    def soma (a, b):
        return a + b
    def subtracao(a, b):
        return a - b
    def multiplicacao(a, b):
        return a * b
    def divisao (a, b):
        return a / b
    msg = f'soma:\t{soma(a, b)}\nsubtração:\t{subtracao(a, b)}' \
          f'\nmultiplicação:\t{multiplicacao(a, b)}\ndivisão:\t{divisao(a, b):.1f}'
    print(msg)
calculadora(5, 6)

def fibonacci_rec(atual):
    if (atual == 1):
        return 0
    elif (atual == 2):
        return 1
    else:
        a = fibonacci_rec(atual - 1)
        b = fibonacci_rec(atual - 2)
        return (a + b)
for i in range(10):
    print(fibonacci_rec(i + 1))

def primeiro_decorador(func):
    def primeira_func():
        print('Execução antes da função')
        func()
        print('Execução após a função')
    return primeira_func

@primeiro_decorador
def funcao_utilizadora():
    print('Preciso usar o decorador')
funcao_utilizadora()

def calculadora_dec(func):
    a = int(input('Digite o valor de A:'))
    b = int(input('Digite o valor de B:'))
    resultado = func (a, b)
    msg = f'Resultado: {resultado}\n'
    print(msg)

@calculadora_dec
def soma(b, a):
    return a + b

@calculadora_dec
def subtracao(a, b):
    return a - b

@calculadora_dec
def multiplicacao(a, b):
    return a * b

@calculadora_dec
def divisao(a, b):
    return a / b

def log_soma(func):
    def mensagem(*args):
        msg = f'a soma de {args[0]} com {args[1]} da '
        print(msg, end='')
        resposta = func(*args)
        print(resposta)
    return mensagem

@log_soma
def soma (a, b):
    return a + b
soma(4, 5)
