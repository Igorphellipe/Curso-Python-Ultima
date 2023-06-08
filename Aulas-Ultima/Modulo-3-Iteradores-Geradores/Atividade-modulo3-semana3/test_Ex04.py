from test_aula_unitario_Ex04 import *
from unittest import mock
import pytest
import sys
from io import StringIO
def test_remover_peca(monkeypatch):
    # Adiciona uma peça para ser removida
    pecas.append({'codigo': 1, 'nome': 'Roda4', 'fabricante': 'Cofap', 'valor': 10.5})
    #pecas.append({'codigo': 2, 'nome': 'Roda43', 'fabricante': 'Cofap2', 'valor': 10.4})

    #Substitui input temporariamente
    monkeypatch.setattr('builtins.input', lambda _: 1)

    # Chama a função que queremos testar
    removedor_peca()

    # Verifica se a peça foi adicionada corretamente
    assert len(pecas) == 0

import sys
from io import StringIO
def test_imprimir_peca():
    #Cria um objeto StringIo para capturar a saída impressa
    output = StringIO()
    sys.stdout = output

    #define uma peça fictícia para imprimir
    peca = {'codigo': 1, 'fabricante': 'fabricante 1', 'valor': 10.0}

    #chama a função que queremos testar
    imprimir_peca(peca)

    #obtém a saída impressa
    printed_output = output.getvalue()

    #restaura a saída padrão
    sys.stdout = sys.__stdout__

    #verifica se a saída impressa está correta
    assert printed_output == "Código: 1\nFabricante: fabricante 1\nValor: 10.0R$\n"

#Função personalizada para simular entrada de dados do usuário
def simulate_input(inputs_list):
    return lambda *args: inputs_list.pop(0)

def test_cadastro_peca(monkeypatch):
    #Simula a entrada do usuário com valores pré-definidos
    inputs = [123, 'Nome da Peça', 'Fabricante de Peça', 10.5]
    monkeypatch.setattr('builtins.input', simulate_input(inputs))

    #chama a função que vamos testar
    cadastrar_peca()

    assert len(pecas) == 1
    assert pecas[0]["codigo"] == 123
    assert pecas[0]["nome"] == 'Nome da Peça'
    assert pecas[0]["fabricante"] == 'Fabricante de Peça'
    assert pecas[0]["valor"] == 10.5


