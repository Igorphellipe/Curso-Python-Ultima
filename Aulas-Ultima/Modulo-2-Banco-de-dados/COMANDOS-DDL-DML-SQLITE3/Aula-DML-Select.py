#Aula de DML SELECT

#Importando Banco de Dados
import sqlite3

#Criando Conexão com o banco de dados
conexao = sqlite3.connect('banco.teste')

#Comando de iteração com o usuário
id = int(input('Digite o ID do funcionario para buscar dados: '))

#Criar uma lista para armazenar varieveis de iteração com o usuário
valor = [id]

#Variavél para armazenar comando SQL
sql = "SELECT * FROM funcionario WHERE id = ?"

#Criando cursor para executar comando SQL
cursor = conexao.cursor()

#Comando para executar SQL e Armazenar dados da BUSCA em uma variavél
resultados = cursor.execute(sql, valor)

#Comando para mostrar dados recuperados do banco ao usuário
for resultado in resultados:
    print(resultado)
print('FIM DO PROGRAMA! ')

#Comando para fechar a conexão com o banco
conexao.close()