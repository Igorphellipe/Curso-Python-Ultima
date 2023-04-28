'''Crie uma table cliente com sqlite3'''

# Biblioteca responsavel por interagir com o banco de dados
import sqlite3

# Conectar (ou criar) o banco de dados
conexao = sqlite3.connect('biblioteca.db')

# Criar um objeto cursor para executar comandos SQL
cursor = conexao.cursor()

# Criar a tabela de categorias
cursor.execute('''
CREATE TABLE IF NOT EXISTS livro (
    id INT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    data_de_publicacao DATE,
    preco DECIMAL(10, 2)
    
);
''')

#salvar alterações
conexao.commit()
conexao.close()