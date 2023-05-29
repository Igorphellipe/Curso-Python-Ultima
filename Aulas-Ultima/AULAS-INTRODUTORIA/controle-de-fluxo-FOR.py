#Nomes sem lista
nome = 'Bruno'.lower()
print(nome)
print('-=-' * 10)

#lista de Nomes usando o Laço FOR
nomes = ['Ana','Bruno','JOSE','MARIA', 'zeca']
print(nomes)
for n in nomes:
    print(n.lower())
print('-=-' * 10)

# Lista utilizando números
lista = list(range(1,10))
print(lista)
print('-=-' * 10)

#Lista de números utilzando FOR
for numeros in range(1,11):
    print(numeros)
print('-=-' * 10)

#Percorrendo listas Simultaneamente com Laço FOR e função Zip
nomes = ['bruno', 'jose', 'João', 'Fernanda']
idades = [40, 55, 44, 60]
lista_de_tuplas = zip(nomes, idades)
for nome, idade in lista_de_tuplas:
    print(f'{nome} tem {idade} anos')
print('-=-' * 10)

#Percorrendo lista idades com laço FOR e fazendo uma seleção
idade = 0
cont = 0
for idade in idades:
    if idade > 50:
        cont = cont + 1
print(f'{cont} pessoa(s) tem mais que 50 anos')  
print ('-=-' * 10)

#Percorrendo uma lista de idades com laço For e indicando sua colocação
for indice, idade in enumerate(idades):
    if idade > 50:
        print(f'Indice:{indice} contém idade maior que 50!')

#Percorrendo lista de alunos
print('-=-' * 10)
alunos = ['Elaine', 'Giúlia', 'Pedro', 'Thiago', 'Wanessa']
alunos_presentes = 0
for aluno in alunos:
    print(f'{aluno} presente')
    alunos_presentes = alunos_presentes + 1
print(f'Quantidade de alunos {alunos_presentes}')

#Ultilizando laço FOR com RANGE
print('-=-' * 10)
for i in range(10):
    print(i)

#Laço FOR com interações de parada e pular 
print('-=-' * 10)
for numero in range(100):
    if numero % 2 != 0:
        continue
    print(f'O número {numero} é PAR!')
    if numero == 10:
        print('Ops... já verifiquei muitos numeros pares!')
        break

#Criando lista de coordenadas com Laço FOR
print('-=-' * 10)
coordenadas = [(1, 1), (2, 1), (3,4)]
for x, y in coordenadas:
    print(f'X: {x}| Y: {y}')
