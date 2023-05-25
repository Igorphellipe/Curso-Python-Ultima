#Aula de Banco de dados DML delete
#Importando banco de dados
import sqlite3

#criando conexão com o banco
conexao = sqlite3.connect('banco.teste')

#Criando variavél de interação com o usuário
id = int(input('Digite o ID do funcionário que deseja excluir: '))

#Lista para armazenar variavél de interação com o usuário
valor = [id]

#Criando variavél para armazenar comando SQL
sql = 'DELETE FROM funcionario WHERE id = ?'

#Criando cursor para executar SQL
cursor = conexao.cursor()

#Executando comando SQL
cursor.execute(sql, valor)

#Comando para salvar alterações no banco
conexao.commit()
print('DADOS APAGADOS COM SUCESSO!')

#Comando para fechar conexão com o banco
conexao.close()