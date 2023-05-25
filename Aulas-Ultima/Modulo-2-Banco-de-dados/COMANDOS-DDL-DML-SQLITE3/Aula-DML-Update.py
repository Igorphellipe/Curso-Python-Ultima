#Aula de DML Atualizando Dados com comando Update

#Importando banco de dados
import sqlite3

#Criando conexão com o banco de Dados
conexao = sqlite3.connect('banco.teste')

#Criando iteração com o usuário para atualizar dados
id = int(input('Digite o ID do funcionario para atualização: '))
nome = str(input('Digite um novo Nome para o Funcionário: '))

#Lista para armazenar variavéis de interação com o usuário
valor = [nome, id]

#Variavel para armazenar comandos SQL
sql = "UPDATE funcionario SET nome = ? WHERE id = ?"

#Criando cursor para executar comandos SQL
cursor = conexao.cursor()

#Comando para execução dos comandos SQL
cursor.execute(sql, valor)

#Comando para salvar alterações no banco
conexao.commit()
print('ATUALIZAÇÃO FEITA COM SUCESSO!')

#Comando para fechar conexão
conexao.close()