#Revisão Modulo 1 - Curso ultima 
# 1 Atividade - operações basicas
print('-=-' * 15)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A media do aluno é {media}')
print('-=-' * 15)
# 2 atividade - programa para computar a média de um aluno
nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota2) / 2
if media >= 7:
    print(f'O aluno {nome} foi aprovado!')
elif media < 5:
    print(f'O aluno {nome} foi reprovado!')
else:
    print(f'O aluno {nome} está de recuperação!')
print('-=-' * 15)

# 3 Atividade - calculando a media de N alunos
aprovado = []
recuperacao = []
reprovado = []
for aluno in range(3):
    print(f'NOTA DO ALUNO {aluno}')
    nome = str(input('Digite o nome do aluno'))
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2) / 2
    print(f'O aluno {aluno} tirou {media:.2f}')
    #Verificação de notas
    if media >= 7:
        print('Aprovado')
        aprovado.append(nome)
    elif media < 5:
        print('Reprovado')
        reprovado.append(nome)
    else:
        print('Recuperação')
        recuperacao.append(nome)
print(f'Temos {aprovado} alunos aprovados, {recuperacao} de recuperação, {reprovado} reprovado')
print('-=-' * 15)
