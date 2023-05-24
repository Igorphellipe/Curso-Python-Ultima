#ATIVIDADE DE FUNÇÃO QUE ROTORNA O VALOR DO JUROS
def decorator_imprimir(juros):
    def valor(capital, taxa, tempo):
        print(f'Capital: {capital}, Taxa: {taxa}, Tempo: {tempo}')
        juros(capital, taxa, tempo)
        print('fim')
    return valor
@decorator_imprimir
def juros_s(capital, taxa, tempo):
    return print(f'Resultado juros: {capital * (taxa / 100) * tempo:.2f}' )

capital = float(input('Digite o valor do emprestimo: '))
taxa = float(input('Digite o valor da taxa de juros: '))
tempo = int(input('Digite a quantidade de meses para pagamento: '))
juros_s(capital, taxa, tempo)