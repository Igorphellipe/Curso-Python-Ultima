#Atividade Semana 3 Modulo 1
#Crie uma função que receba duas palavras e retorne "True" casoo a primeira palavra seja um prefixo da segunda, e 'False' caso contrário.

#Resolução Pelo aluno 
def verfica_prefixo(palavra1, palavra2):
    if palavra1 in palavra2:
        return 'True'
    else:
        return 'False'
palavra1 = str(input('Digite uma palavra: ')).strip()
palavra2 = str(input('Digite outra palavra: ')).strip()

resultado = verfica_prefixo(palavra1, palavra2)
print(resultado)




#Resolução do professor
def prefixo(palavra1, palavra2):
    tamanho = len(palavra1)
    for indice in range(tamanho):
        if palavra1[indice] != palavra2[indice]:
            return False
        return True
palavra1 = str(input('digite: '))
palavra2 = str(input('digite: '))
resultado = prefixo(palavra1, palavra2)
print(resultado)