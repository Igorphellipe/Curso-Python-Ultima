print('-=-' * 10)
print('CALCULANDO TOTAL DE MOEDAS NO CAIXA')
print('-=-' * 10)
#Calculo total de moedas em caixa utilizando While True
total = valor = 0
quantidade = moedas = 0
while True:
    moedas = float(input('Qual valor da moeda: R$'))
    quantidade = int(input('Digite a quantidade: '))
    print('-=-' * 10)
    valor = moedas * quantidade
    total = total + valor
    #Condicional de parada:
    resp = str(input('Deseja continuar [S/N]')).strip().upper()[0]
    print('-=-' * 10)
    if resp in 'Nn':
        break
print(f'O valor total de moedas em caixa é R${total}')

#Calculando total de moedas em caixa somando as variaveis
print('-=-' * 10)
print('CALCULANDO MOEDAS EM CAIXA')
print('-=-' * 10)

#Colocando valores nas variaveis
total_5_centavos = 35 * 0.05
total_10_centavos = 50 * 0.10
total_25_centavos = 30 * 0.25
total_50_centavos = 15 * 0.50
total_1_real = 19 * 1.0
#Somando todos os valores e atribuindo a uma varial de soma total (total_caixa)
total_caixa = total_5_centavos + total_10_centavos + total_25_centavos + total_50_centavos + total_1_real

#Mostrando a soma de cada moeda 
print(f'Seu caixa tem R${total_5_centavos} de moedas de R$0.05')
print(f'Seu caixa tem R${total_10_centavos} de moedas de R$0.10')
print(f'Seu caixa tem R${total_25_centavos} de moedas de R$0.25')
print(f'Seu caixa tem R${total_50_centavos} de moedas de R$0.50')
print(f'Seu caixa tem R${total_1_real} de moedas de R$1.00')

#Mostrando o resultado final da soma de todas as moedas.
print(f'Somando todos os valores temos um total de R${total_caixa} em moedas no caixa')
print('-=-' * 10)