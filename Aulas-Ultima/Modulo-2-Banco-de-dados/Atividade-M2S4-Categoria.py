import sqlite3

conexao = sqlite3.connect('banco.sqlite3')

#FUNÇÃO PARA O USUÁRIO CADASTRAR UMA NOVA CARTEGORIA
def casdastro_categoria():
    # solicita dados ao usuário
    id = int(input('Digite o ID da categoria: '))
    nome = str(input('Digite o nome da categoria: '))

    # lista para armazenar dados solicitados pelo usuário
    valor = [id, nome]

    # variavél SQL para armazenar comando sql
    sql = 'INSERT INTO categorias (id, nome) VALUES (?, ?)'

    # cria o cursor para executar comandos sql
    cursor = conexao.cursor()

    # comando de execução de SQL
    cursor.execute(sql, valor)

    # comando para salvar alterações no banco
    conexao.commit()

    # camando para encerrar conexão com banco
    conexao.close()

#FUNÇÃO ATUALIZAR DADOS DA TABELA CATEGORIA
def atualizar_categoria():

    #solicita dados ao usuário
    id = int(input('Digite o ID da categoria que deseja atualizar: '))
    nome = str(input('Digite um novo nome para a categoria: '))

    #lista para armazenar dados solicitados pelo usuário
    valor = [nome, id]

    #variavél SQL para armazenar comando sql
    sql = 'UPDATE categorias SET nome = ? WHERE id = ?'

    #cria o cursor para executar comandos sql
    cursor = conexao.cursor()

    #comando de execução de SQL
    cursor.execute(sql, valor)

    #comando para salvar alterações no banco
    conexao.commit()

    #camando para encerrar conexão com banco
    conexao.close()


#FUNÇÃO PARA DELETAR DADOS DA TABELA CATEGORIA
def deletar_categoria():
    id = int(input('Digite o Id da categoria que deseja excluir: '))

    # lista para armazenar dados solicitados pelo usuário
    valor = [id]

    # variavél SQL para armazenar comando sql
    sql = 'DELETE FROM categorias WHERE id = ?'

    # cria o cursor para executar comandos sql
    cursor = conexao.cursor()

    # comando de execução de SQL
    cursor.execute(sql, valor)

    # comando para salvar alterações no banco
    conexao.commit()

    # camando para encerrar conexão com banco
    conexao.close()

#FUNÇÃO PARA LISTAR TODAS AS CATEGORIAS
def listar_categorias():
    resp = int(input('Digite 1) listar categorias 2) Sair: '))

    #Condição para listar categorias
    if resp == 1:
        #Variavél
        sql = 'SELECT * FROM categorias'

        #Cria cursor para comando Sql
        cursor = conexao.cursor()

        #Comando para executar SQL
        cursor.execute(sql)

        resultado = cursor
        for cat in resultado:
            print(cat)

        #Comando para encerra conexão com banco
        conexao.close()
    elif resp == 2:
        print('ENCERRANDO BUSCA !')