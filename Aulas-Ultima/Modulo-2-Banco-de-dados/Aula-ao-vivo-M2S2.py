'''Atividade 1

Crie um programa em Python que gera tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:

As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não);
As restrições/relacionamentos devem fazer sentido'''

#importa o banco de dados para utilizar
import sqlite3

#Cria o banco de dados
conexao = sqlite3.connect('atividade-M2S2.db')

#Criar um cursor para executar comandos SQL (DDL/DML)
cursor = conexao.cursor()

#Comando CURSOR.EXECUTE utilizado para passar comandos SQL e seus paramentros para criar uma tabala
cursor.execute('CREATE TABLE IF NOT EXISTS categoria (id_tarefas INT PRIMARY KEY, portugues VARCHAR (100), ingles VARCHAR (100),matematica VARCHAR(100), data DATE NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS tarefas (id_tarefas INT PRIMARY KEY,id_materia INT, nome VARCHAR (100) NOT NULL, data DATE NOT NULL, status INT CHECK (status IN  (0 , 1)), FOREIGN KEY (id_materia) REFERENCES categoria(id_materia));')



#Comando CONEXAO.COMMIT salva as alterações na tabela
conexao.commit()

#Comando CONEXAO.CLOSE encerra a conexão com o banco de dados
conexao.close()