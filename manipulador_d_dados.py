import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
from datetime import datetime

#Aonde tudo começou :o

#esse é o modulo aonde pegamos a noticia, criamos nossa tabela, garantimos que ela é atualizada e que sempre verificamos sua existencia, foi a parte mias simples do código.

def peganoticia():
    url_cnn = 'https://www.cnnbrasil.com.br/'
    try:
        resposta = requests.get(url_cnn, headers={'User-Agent': 'Mozilla/5.0'})
        resposta.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar notícias: {e}")
        return []

    sopa = BeautifulSoup(resposta.content, 'html.parser')

    lista_noticias = []
    for elemento in sopa.find_all(['a', 'h2', 'h3']):
        texto = elemento.get_text(strip=True)
        if texto and len(texto) > 30 and texto not in lista_noticias:
            lista_noticias.append(texto)
    return lista_noticias

def salvanoti(novas_noticias, nome_arquivo='noticias_cnn.csv'):
    df_existente = pd.DataFrame()
    noticias_existentes = set()

    if os.path.exists(nome_arquivo):
        df_existente = pd.read_csv(nome_arquivo)
        if 'Notícias' in df_existente.columns:
            noticias_existentes = set(df_existente['Notícias'].tolist())
        if 'Data' in df_existente.columns:
            df_existente['Data'] = pd.to_datetime(df_existente['Data'], errors='coerce')
            df_existente = df_existente.dropna(subset=['Data']) 
        else:
            df_existente['Data'] = pd.NaT 

    noticias_unicas = [noticia for noticia in novas_noticias if noticia not in noticias_existentes]

    if noticias_unicas:
      
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
        df_novas = pd.DataFrame({'Notícias': noticias_unicas, 'Data': data_atual})
        df_novas['Data'] = pd.to_datetime(df_novas['Data']) 

        df_final = pd.concat([df_existente, df_novas], ignore_index=True)
  
        df_final.to_csv(nome_arquivo, index=False, encoding='utf-8-sig', date_format='%Y-%m-%d %H:%M:%S')
        print(f"Adicionadas {len(noticias_unicas)} novas notícias ao arquivo '{nome_arquivo}'.")
    else:
        print("Nenhuma notícia nova para adicionar.")

def carregadados(nome_arquivo):
  
    dados = []
    if not os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            leitor_csv = csv.reader(f)
            next(leitor_csv, None)  
            for linha in leitor_csv:
                if linha and linha[0]: 
                    dados.append(linha[0])
    except Exception as e:
        print(f"Erro ao carregar dados do arquivo '{nome_arquivo}': {e}")
    return dados

