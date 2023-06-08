import pytest
pecas = []


def  gerar_código ():
    tamanho_lista  =  len ( pecas )
    if  tamanho_lista  >  0 :
        ultima_peca  =  pecas [ tamanho_lista  -  1 ]
        ultimo_codigo  =  ultima_peca [ 'codigo' ]
        return  ultimo_codigo  +  1

    return 1


def  cadastrar_peca ():
    codigo = int(input('Codigo peça')) #gerar_codigo ()
    #print ( f' \n Código da peça: { codigo :03d } ' )
    nome = str(input ( 'Por favor entre com o nome da peça: ' ))
    fabricante = str(input ( 'Por favor entre com o fabricante da peça: ' ))
    valor = float(input ( 'Por favor entre com o valor da peça (R$): ' ))
    peca = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor }
    pecas.append(peca)
    print ( 'Peça Adicionada! \n ' )


def  imprimir_peca ( peca ):
    print ( f'Código: { peca [ "codigo" ]}')
    print ( f'Fabricante: { peca [ "fabricante" ]}')
    print ( f'Valor: { peca [ "valor" ]}R$')


def  consultar_pecas ():
    finaliza_consulta  =  False
    while not finaliza_consulta :
        print ( 'Você selecionou a opção para consultar peças' )
        print ( 'Escolha a opção desejada:' )
        print ( '1 - Consultar todas as pecas' )
        print ( '2 - Consultar peças por código' )
        print ( '3 - Consultar peças por fabricante' )
        print ( '4 - Retornar' )
        opção_consulta  =  int ( input ( 'Opção: ' ))
        print ()
        if  opcao_consulta  ==  1 :
            for peca in pecas:
                print ( peca )
                print ( '-'  *  15 )
        elif  opcao_consulta  ==  2 :
            codigo  =  int ( input ( 'Digite o código da peça: ' ))
            for peca in pecas:
                if  peca [ 'codigo' ] ==  codigo :
                    print ( peca )
                    print ( '-'  *  15 )
                    break
        elif  opcao_consulta  ==  3 :
            fabricante  =  input ( 'Digite o fabricante da peça: ' )
            for peca in pecas:
                if  peca [ 'fabricante' ] ==  fabricante :
                    print ( peca )
                    print ( '-'  *  15 )
        elif  opcao_consulta  ==  4 :
            finaliza_consulta  =  Verdadeiro
            print ()
        else:
            print ( 'Opção inválida. Tente novamente' )


def  removedor_peca ():
    print ( 'Você selecionou a opção para retirar uma peça' )
    codigo  =  int ( input ( 'Código da peça a ser removido: ' ))
    peca_removedor = {}
    for peca in pecas:
        if  peca [ 'codigo' ] ==  codigo :
            peca_removedor  =  peca
            break

    pecas.remove( peca_removedor )
    print ( 'Peça removida com sucesso' )


if __name__  ==  '__main__' :
    opcao  =  0
    while  opcao  !=  4 :
        print ( 'Escolha a opção desejada' )
        print ( '1 - Cadastrar Peças' )
        print ( '2 - Consultar Peças' )
        print ( '3 - Removedor de Peças' )
        print ( '4 - Sair' )
        opção  =  int ( input ( 'Opção desejada: ' ))

        if opcao  ==  1 :
            cadastrar_peca ()
        elif  opcao  ==  2 :
            consultar_pecas ()
        elif  opcao  ==  3 :
            removedor_peca ()
        elif  opcao  >  4  or  opcao  <  1 :
            print('Opção inválida')

    print ( 'Obrigado por usar nossos aplicativos' )
