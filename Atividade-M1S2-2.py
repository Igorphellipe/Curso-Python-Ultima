print('-=-' * 10)
print('CALCULANDO VALOR FREELANCE PYTHON')
print('-=-' * 10)

#Valores iniciados nas variaveis
valor_inicial = 1000
valor_hora = 20.45
horas = 80
porcentagem = 0.15
total_serviço = (valor_inicial + horas * valor_hora) * porcentagem + (valor_inicial + (horas * valor_hora))

#Descrição dos valores em cada variavel
print(f'Valor inicial do serviço R${valor_inicial}!')
print(f'Valor serviço por hora R${valor_hora}')
print(f'Total de horas {horas}')
print('Porcentagem cobrada no total do serviço: 15% de taxa')
print(f'Total dos servios prestados R${total_serviço:.2f}')
print('-=-' * 22)

#CALCULANDO VALOR DE FREELANCE, SOLICITANDO ENTRADA DE VALORES PELO TECLADO!
print('CALCULANDO SERVIÇO DE FREELANCE PYTHON')
valor_inicial = float(input('Digite o valor inicial do serviço: R$'))
valor_hora = float(input('Digite o valor cobrado por hora: R$'))
horas = int(input('Digite as horas trabalhadas: '))
porcentagem = 0.15
total_serviço = (valor_inicial + horas * valor_hora) * porcentagem + (valor_inicial + horas * valor_hora)
print(f'O valor total do serviços prestados é: R${total_serviço:.2f}')