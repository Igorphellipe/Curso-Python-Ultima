#ATIVIDADE DE CRIAÇÃO DE TAFERAS
#importar o banco de dados
import sqlite3

#criar conexão com o banco de dados
conexao = sqlite3.connect('banco.sqlite3')

#FUNÇÃO PARA CADASTRAR UMA TAREFA
def cadastro_tarefa():
    #entrada de dados do usuário
    id = int(input('Digite um ID para a tarefa: '))
    nome = str(input('Digite o Nome da Tarefa: '))
    data = input('Digite a data de entrega da Tarefa: (AAAA-MM-DD): ')
    id_categoria = int(input('Digite o ID da categoria da Tarefa: '))
    #situacao = int(input('Digite 1 para tarefa concluída é 0 para pendente: '))

    #lista para armazenar dados passados pelo usuário
    valores = [id,nome,data,id_categoria]

    #Variavél SQL para armazenar comandos SQl
    sql = 'INSERT INTO tarefas (id, nome, data_entrega, situacao, categorias_id) VALUES (?, ?, ?, 0, ?)'

    #cria um cursor para executar os comandos SQL
    cursor = conexao.cursor()

    #comando de execução de SQL
    cursor.execute(sql, valores)

    #Comando para salvar alterações no banco
    conexao.commit()

    #Comando para fechar conexão com banco
    conexao.close()

conexao = sqlite3.connect('banco.sqlite3')
#FUNÇÃO PARA ATUALIZAR DADOS DE UMA TAREFA
def atualizar_tarefa():
    #entrada de dados do usuário
    id = int(input('Digite o ID da tarefa que deseja atualizar: '))
    nome = str(input('Digite um novo nome para tarefa: '))
    data = input('Digite uma nova data para a tarefa: ')
    id_categoria = int(input('Digite o ID da nova categoria da tarefa: '))

    #lista para armazenar novos dados pasados pelo usuário
    valores = [nome, data, id_categoria, id]

    #vairavél para armazenar comando SQL
    sql = 'UPDATE tarefas SET nome = ?, data_entrega = ?, situacao = 0, categorias_id = ? WHERE id = ? '

    #Cria um cursor para executar comando SQL
    cursor = conexao.cursor()

    #Executa comando SQL
    cursor.execute(sql, valores)

    #Comando para salvar alterações no banco
    conexao.commit()

    #Comando para fechar conexão com o banco
    conexao.close()

#FUNÇÃO PARA EXCLUSÃO DE TAREFAS
def del_tarefas():
    #Solicita o usuário ID da atividade para exlusão
    id = int(input('Digite o ID da tarefa que deseja excluir: '))

    #lista para armazenar dados passados pelo usuário
    valor = [id]

    #Variavél criada para armazenar dados SQL
    sql = 'DELETE FROM tarefas WHERE id = ?'

    #Cria um cursor para executar comando SQL
    cursor = conexao.cursor()

    #Comando de execução do SQL
    cursor.execute(sql, valor)

    #Comando para salvar alterações no banco
    conexao.commit()

    #Comando para encerrar conexão com o banco
    conexao.close()

#FUNÇÃO PARA LISTAR TODOS OS AFAZERES DE UM DIA ESPECIFÍCO
def listar_tarefas():
    #Solicita data ao usário para fazer verificação de tarefas
    data = input('Digite uma data para verificar tarefas (AAAA-MM-DD): ')

    #lista para armazenar dados passados pelo usuário
    valor = [data]

    sql = 'SELECT * FROM tarefas WHERE data_entrega = ?'

    #Cria cursor para executar comando SQL
    cursor = conexao.cursor()

    #Comando para executar SQL
    cursor.execute(sql, valor)

    resultado = cursor
    for tarefa in resultado:
        print(tarefa)

    #Comando para encerrar conexão com o banco
    conexao.close()

#FUNÇÃO PARA VERIFICAR CONCLUSÃO DE TAREFA
def conclusao_tarefa():
    #Solicita ID e Nome da tarefa para atualizar situação
    print('ATUALIZAR CONCLUSÃO DE TAREFAS')
    id = int(input('Digite o Id da tarefa: '))
    nome = str(input('Digite o Nome da tarefa: '))
    situacao = int(input('DIGITE (1) para tarefa concluida (0) para não concluida: '))

    #lista para armazenar dados passados pelo usuário
    valores = [situacao, id, nome]

    #Variavél para armazenar comandos SQL
    sql = 'UPDATE tarefas SET situacao = ? WHERE id = ? AND nome = ?'

    #Cria um cursor para executar comando SQL
    cursor = conexao.cursor()

    #Comando para executar SQL
    cursor.execute(sql, valores)

    #Comando para salvar alterações no banco
    conexao.commit()

    #Comando para encerrar conexão com o banco
    conexao.close()

conclusao_tarefa()