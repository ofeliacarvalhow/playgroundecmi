# manipulador_d_dados.py (versão simplificada)

import csv
import os

def carregadados(nome_arquivo):
    dados = []
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            leitor_csv = csv.reader(f)
            next(leitor_csv, None)  # pula cabeçalho
            for linha in leitor_csv:
                if linha and linha[0]:
                    dados.append(linha[0])
    except Exception as e:
        print(f"Erro ao carregar dados do arquivo '{nome_arquivo}': {e}")
    return dados


