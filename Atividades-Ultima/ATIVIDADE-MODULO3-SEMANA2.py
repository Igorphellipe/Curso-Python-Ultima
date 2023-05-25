#ATIVIDADE DE FUNÇÃO QUE ROTORNA O VALOR DO JUROS
def decorator_imprimir(juros):
    def valor(*args):
        print(f'Capital: {args[0]}, Taxa: {args[1]}, Tempo: {args[2]}')
        juros(*args)
        print('fim')
        return (juros_s)
    return valor
@decorator_imprimir
def juros_s(capital, taxa, tempo):
    return print(f'Resultado juros: {capital * (taxa / 100) * tempo:.2f}' )

juros_s(1300, 4, 6)
