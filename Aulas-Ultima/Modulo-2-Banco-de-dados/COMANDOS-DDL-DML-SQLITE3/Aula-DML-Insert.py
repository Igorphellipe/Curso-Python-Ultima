#Aula de Manipulação de dados
#INSERT (inserir dados)
#SELECT (realizar consultas)
#UPDATE (atualizar dados)
#DELETE (remover dados)

#Trabalhando com Comando INSERT
#Importando Banco
import sqlite3

#Criando conexão com o banco
conexao = sqlite3.connect('banco.teste')

#Solicitando Dados ao Usuário
id = int(input('Digite o ID do funcionario: '))
nome = str(input('Digite o Nome do funcionário: '))
endereco = str(input('Digite o endereço: '))

#Criando uma lista para armazenar variaveis
valores = [id, nome, endereco]

#Variavél para armazenar comandos SQL
sql = "INSERT INTO funcionario (id, nome, endereco) VALUES (?, ?, ?);"

#Criando cursor para executar comando SQL
cursor = conexao.cursor()

#Comando para executar SQL
cursor.execute(sql, valores)

#Salvando alterações no banco
conexao.commit()
print('DADOS INSERIDOS COM SUCESSO! ')

#Fechando conexão com o banco
conexao.close()