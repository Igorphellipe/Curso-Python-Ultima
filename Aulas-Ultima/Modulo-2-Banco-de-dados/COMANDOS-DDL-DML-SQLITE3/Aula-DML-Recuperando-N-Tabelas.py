#Aula de Banco, Recuperando dados de tabelas destintas
#Importando o banco de dados
import sqlite3

#Criando conexão com o banco
conexao = sqlite3.connect('Banco.rec')

#Variavel para armazenar comandos SQL
sql = 'CREATE TABLE IF NOT EXISTS categoria (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
      'nome VARCHAR (100));'

#Criando curso para executar comando SQL
cursor = conexao.cursor()

#Comando para executar SQL
cursor.execute(sql)

#Comando para salvar alterações ao Banco
conexao.commit()
print('BANCO CATEGORIA CRIADO COM SUCESSO!')

#SQL para criação da tabela produto

#Variavél criada para armazenar comando SQL
sql = 'CREATE TABLE IF NOT EXISTS produto (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,' \
      'nome VARCHAR (100),' \
      'categoria_id INTEGER NOT NULL,' \
      'CONSTRAINT produto_fk FOREIGN KEY (categoria_id) REFERENCES categoria(id));'

#Comando para executar SQL
cursor.execute(sql)

#Comando para salvar alterações no Banco
conexao.commit()
print('TABELA CRIADA COM SUCESSO!')


#laço para colocar dados na tabela categorias
for i in range(3):
      #Iteração com o usuário
      nome = str(input('Digite o nome da categoria: '))
      #Lista para armazenar variavél de iteração com o usuario
      valor = [nome]

      sql = 'INSERT INTO categoria (nome) VALUES (?);'

      #Comando para executar sql
      cursor.execute(sql, valor)

      #comando para salvar alteração no banco
      conexao.commit()
      print('DADOS SALVOS COM SUCESSO!')

for i in range(4):
      #Iteração com o usuario
      nome = str(input('Digite o nome do produto: '))
      id_cat = int(input('Digite o ID da categoria do produto: '))

      #Lista para armazenar valores de iteração com o usuário
      valores = [nome, id_cat]

      #Variavél para armazenar comandos SQL
      sql = 'INSERT INTO produto (nome, categoria_id) VALUES (?, ?);'

      #Comando para executar SQL
      cursor.execute(sql, valores)

      #Comando para salvar alterações no banco
      conexao.commit()
      print('DADOS SALVOS COM SUCESSO!')

#Usando comado Select para vizualizar dados das Tabelas Categoria e Produto
sql = 'SELECT * FROM categoria'

#Comando para executar SQL e armazenar os dados buscados na variavél Resultado
resultado = cursor.execute(sql)

#Laço For para mostrar dados recuperados do banco
for res in resultado:
      print(res)
print('-=-' * 15)
sql = 'SELECT * FROM produto'

#Comando para executar SQL e armazenar dados buscados na variavél resultado
resultado = cursor.execute(sql)

#laço For para mostrar dados recuperados do banco
for res in resultado:
      print(res)
print('-=-' * 15)

#Usando Select e Combinando Tabelas
#Variavél para armazenar comandos SQL
sql = 'SELECT produto.id, produto.nome, categoria.nome as categoria ' \
      'FROM produto as produto, categoria as categoria WHERE produto.categoria_id = categoria.id'

#executando Comando Sql e armazenando busca de dados a variavel Resultado
resultado = cursor.execute(sql)

#laço for para mostrar dados
for res in resultado:
      print(res)
print('-=-' * 15)

#Comando Select com LIKE buscar todas categorias que começam com C
#Variavél para armazernar comando SQL
sql = 'SELECT id, nome FROM categoria WHERE nome LIKE "c%" '

#Comando para executar SQl e Armazenar buscas do banco na Variavél Resultado
resultado = cursor.execute(sql)

#Laço for para mostrar resultado da busca
for res in resultado:
      print(res)
print('-=-' * 15)

# Comando Select com LIKE buscar todos produtos que contenham a letra e no seu nome
# Variavél para armazernar comando SQL
sql = 'SELECT id, nome, categoria_id FROM produto WHERE nome LIKE "%e%" '

# Comando para executar SQl e Armazenar buscas do banco na Variavél Resultado
resultado = cursor.execute(sql)

# Laço for para mostrar resultado da busca
for res in resultado:
      print(res)
