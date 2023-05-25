#Aula Banco de dados
#importando e criando conexão com SQLite3
#Importando Banco de dados
import sqlite3

#Criando conexão com o banco
conexao = sqlite3.connect('banco.teste')

#variavel criada para armazenar comandos SQL
sql = 'CREATE TABLE funcionario (id INT PRIMARY KEY NOT NULL,' \
      'nome VARCHAR (100),' \
      'endereco VARCHAR (100));'

#Criando um curso para executar comando SQL
cursor = conexao.cursor()

#Comando para executar SQL
cursor.execute(sql)

#Comando para salvar alterações no banco
conexao.commit()

#Comando para fechar conexão com banco
conexao.close()
