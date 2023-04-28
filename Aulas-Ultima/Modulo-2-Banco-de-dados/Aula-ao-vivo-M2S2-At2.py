'''Atividade 2

Crie um programa em Python que gere tabelas para uma aplicação de eventos. Elas devem compreender as seguintes funcionalidades:
Eventos devem ter título, data e local, além da referência ao organizador;
O organizador deve ter nome, email e cpf;
As restrições/relacionamentos devem fazer sentido.'''

#importa o banco de dados para utilizar
import sqlite3

#Cria o banco de dados
conexao = sqlite3.connect('atividade-M2S2-At2.db')

#Criar um cursor para executar comandos SQL (DDL/DML)
cursor = conexao.cursor()

#Comando CURSOR.EXECUTE utilizado para passar comandos SQL e seus paramentros para criar uma tabala
cursor.execute('CREATE TABLE IF NOT EXISTS organizador (id_organizador INT PRIMARY KEY, nome VARCHAR (100) NOT NULL, cpf VARCHAR (100) NOT NULL,email VARCHAR(100) NOT NULL);')

cursor.execute('CREATE TABLE IF NOT EXISTS eventos (id_enventos INT PRIMARY KEY,id_organizador INT, titulo VARCHAR (100) NOT NULL, data DATE NOT NULL,local VARCHAR (100), FOREIGN KEY (id_organizador) REFERENCES categoria(id_organizador));')



#Comando CONEXAO.COMMIT salva as alterações na tabela
conexao.commit()

#Comando CONEXAO.CLOSE encerra a conexão com o banco de dados
conexao.close()