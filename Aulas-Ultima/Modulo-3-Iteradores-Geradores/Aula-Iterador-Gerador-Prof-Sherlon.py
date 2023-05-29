#Aula de Iterador - Prof Sherlon

#PRIMEIRA FORMA
#indices        0      1       2
minha_lista = ['Um', 'Dois', 'Três']

for variavel in minha_lista:
    print(variavel)
print('-=-' * 10)
#SEGUNDA FORMA
iter_list = iter([['Um','Dois'],['Três','Quatro']])
print(next(iter_list))#Pega o primero "Lote" de dados: 1 e 2
print(next(iter_list))#Pega o Segundo "lote" de dados: 3 e 4
print('-=-' * 15)

#TERCEIRA FORMA
def contador(n):
    #Indices
    minha_lista = ['Um', 'Dois', 'Três']
    for i in range(0, n):
        yield minha_lista[i]

#Percorrendo iteração com Next
iter_list = contador(3)
print(next(iter_list))#Executa o primeiro
print(next(iter_list))#Executa o segundo
print(next(iter_list))#Executa o terceiro
