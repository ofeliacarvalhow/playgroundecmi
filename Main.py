# Arquivo: Main.py (adaptado)

import streamlit as st
import pandas as pd
from manipulador_d_dados import carregadados
from texto import limpar_texto, maiscomuns, procuranoti, comparanoti
from visualizacao import frequennoti
from estilo import estilo_chavoso
from collections import Counter
import os

# Aplicamos o estilo
estilo_chavoso()

# Cabeçalho
st.markdown("""
<div class="custom-header">
    <h1>Palavras mais frequentes nas notícias CNN</h1>
    <img src="https://github.com/ofeliacarvalhow/ADOISVERSAOFINALULTRA/blob/2baf622ac142ffbd75586de9fcd2e90f6ff50a72/iconefofo.png" width="70">
</div>
""", unsafe_allow_html=True)

# Stopwords
IGNORAR = {'to', 's', 'the', 'of', 'for', 'in', 'a', 'its', 'what','on', 'u', 'with', 'as', 'at', 't', 'after', 'over', 'is', 'about', 'was','not', 'new', 'he', 'she', 'him', 'his', 'hers', 'her', 'news', 'them', 'they', 'and', 'says', 'just', 'watch', 'from', 'who','will', 'this', 'out', 'by', 'you', 'it', 'be', 'that', 'are', 'how', 'why','de', 'em', 'que','para','sobre','novo','diz','veja','cnn','como','mais','ser','tem','nesta','até','entre','ter','das','quem','r','após','são','pode','à','se','2025','não','sim','por','na','do','no','da','dos','a','o','os','ele','ela','eles','elas','é','com','um','uma','e','ou','quer','ao'}
CSV = 'noticias_cnn.csv'

if not os.path.exists(CSV):
    st.error("Arquivo noticias_cnn.csv não encontrado!")
    st.stop()

# Carregamos o CSV adaptado
df_noticias = pd.read_csv(CSV)

# Renomeamos colunas para o padrão do código
if 'title' in df_noticias.columns:
    df_noticias.rename(columns={'title': 'Notícias'}, inplace=True)
if 'source' in df_noticias.columns:
    df_noticias.rename(columns={'source': 'Fonte'}, inplace=True)

# Garantimos que as colunas esperadas existem
if 'Notícias' not in df_noticias.columns or 'Fonte' not in df_noticias.columns:
    st.error("As colunas esperadas 'Notícias' e 'Fonte' não estão presentes no CSV.")
    st.stop()

# Menu
pagina_selecionada = st.radio("O que você quer ver?", ["Nada", "Palavras mais frequentes", "Pesquisar ou comparar palavras"])

if pagina_selecionada == "Palavras mais frequentes":
    modo_de_analise = st.radio("Modo de análise:", ["Nenhum", "Geral", "Por fonte"], key="modo_palavras")

    if modo_de_analise in ["Geral", "Por fonte"]:
        tipo_grafico = st.radio("Tipo de gráfico:", ["Nenhum", "Colunas", "Barras horizontais", "Pizza"])
        quantidade_palavras = st.slider("Quantidade de palavras:", 5, 30, 10)

        if tipo_grafico != "Nenhum":
            df_filtrado = df_noticias
            if modo_de_analise == "Por fonte":
                fontes_disponiveis = sorted(df_noticias['Fonte'].dropna().unique())
                fonte_escolhida = st.selectbox("Escolha uma fonte:", fontes_disponiveis)
                df_filtrado = df_noticias[df_noticias['Fonte'] == fonte_escolhida]

            todas_as_palavras = []
            for texto_noticia in df_filtrado["Notícias"].dropna():
                todas_as_palavras.extend(limpar_texto(texto_noticia, IGNORAR))

            if todas_as_palavras:
                palavras_mais_comuns = Counter(todas_as_palavras).most_common(quantidade_palavras)
                frequennoti(palavras_mais_comuns, tipo_grafico)
            else:
                st.write("Nenhuma notícia encontrada para análise.")

elif pagina_selecionada == "Pesquisar ou comparar palavras":
    modo_de_analise = st.radio("Modo de análise:", ["Nenhum", "Geral", "Por fonte"], key="modo2")

    if modo_de_analise in ["Geral", "Por fonte"]:
        df_filtrado = df_noticias
        if modo_de_analise == "Por fonte":
            fontes_disponiveis = sorted(df_noticias['Fonte'].dropna().unique())
            fonte_escolhida = st.selectbox("Escolha uma fonte:", fontes_disponiveis, key="fonte2")
            df_filtrado = df_noticias[df_noticias['Fonte'] == fonte_escolhida]

        opcao_busca = st.radio("Tipo de busca:", ["Nenhuma", "Pesquisar uma palavra", "Comparar duas palavras"])

        if opcao_busca == "Pesquisar uma palavra":
            palavra_pesquisada = st.text_input("Digite a palavra para pesquisar").strip().lower()
            if palavra_pesquisada:
                procuranoti(palavra_pesquisada, df_filtrado, IGNORAR)

        elif opcao_busca == "Comparar duas palavras":
            primeira_palavra = st.text_input("Palavra 1").strip().lower()
            segunda_palavra = st.text_input("Palavra 2").strip().lower()
            tipo_grafico_comparacao = st.radio("Tipo de gráfico para ver a comparação:", ["Nenhum", "Colunas", "Pizza"], key="grafico_comparacao")

            if primeira_palavra and segunda_palavra and tipo_grafico_comparacao != "Nenhum":
                comparanoti(primeira_palavra, segunda_palavra, df_filtrado, IGNORAR, tipo_grafico_comparacao)
