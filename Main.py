import streamlit as st
import pandas as pd
from manipulador_d_dados import peganoticia, salvanoti, carregadados
from texto import limpar_texto, limpar_tokenizar, maiscomuns, procuranoti, comparanoti
from visualizacao import frequennoti, comparaplotnoti
from estilo import estilo_chavoso
import os
import matplotlib.pyplot as plt
from collections import Counter

#Aplicamos nosso estilo iconico
estilo_chavoso()

#Cabeçalho 
st.markdown("""
<div class="custom-header">
    <h1>Palavras mais frequentes nas notícias CNN</h1>
    <img src="https://github.com/ofeliacarvalhow/ADOISVERSAOFINALULTRA/blob/2baf622ac142ffbd75586de9fcd2e90f6ff50a72/iconefofo.png" width="70">
</div>
""", unsafe_allow_html=True)

#Stopwords
IGNORAR = {'de', 'em', 'que','para','sobre','novo','diz','veja','cnn','como','mais','ser','tem','nesta','até','entre','ter','das','quem','r','após','são','pode','à','se','2025','não','sim','por','na','do','no','da','dos','a','o','os','ele','ela','eles','elas','é','com','um','uma','e','ou','quer','ao'}
CSV = 'noticias_cnn.csv'

#Pegar noticias novas
noticias_novas = peganoticia()
salvanoti(noticias_novas, CSV)

#Carrega nossos dados 
lista_noticias = carregadados(CSV)

#Criamos nosso dataframe
df_noticias = pd.read_csv(CSV)
if 'Data' not in df_noticias.columns:
    df_noticias['Data'] = pd.Timestamp.now()
else:
    df_noticias['Data'] = pd.to_datetime(df_noticias['Data'], errors='coerce')
df_noticias = df_noticias.dropna(subset=['Data'])

#Seleção de caixas para o usuário decidir o que quer da vida
pagina_selecionada = st.radio("O que você quer ver?", ["Nada", "Palavras mais frequentes", "Pesquisar ou comparar palavras"])

#Palavras mais frequentes
if pagina_selecionada == "Palavras mais frequentes":
    modo_de_analise = st.radio("Modo de análise:", ["Nenhum", "Geral", "Por dia"], key="modo_palavras")

    if modo_de_analise in ["Geral", "Por dia"]:
        tipo_grafico = st.radio("Tipo de gráfico:", ["Nenhum", "Colunas", "Barras horizontais", "Pizza"])
        quantidade_palavras = st.slider("Quantidade de palavras:", 5, 30, 10)

        if tipo_grafico != "Nenhum":
            df_filtrado = df_noticias
            if modo_analise == "Por dia":
                datas_disponiveis = sorted(df_noticias['Data'].dt.date.unique())
                data_escolhida = st.selectbox("Escolha uma data disponível:", datas_disponiveis)
                df_filtrado = df_noticias[df_noticias['Data'].dt.date == data_escolhida]

            #Filtramos o dataframe e achamos as palavras mais comuns
            todas_as_palavras = []
            for texto_noticia in df_filtrado["Notícias"].dropna():
                todas_as_palavras.extend(limpar_texto(texto_noticia, IGNORAR))

            if todas_as_palavras:
                palavras_mais_comuns = Counter(todas_as_palavras).most_common(quantidade_palavras)
                if palavras_mais_comuns:
                    frequennoti(palavras_mais_comuns, tipo_grafico)
                else:
                    st.write("Não há palavras pra exibir.")
            else:
                st.write("Nenhuma notícia foi encontrada para fazer essa análise.")

#Pesquisar ou comparar palavras
elif pagina_selecionada == "Pesquisar ou comparar palavras":
    modo_de_analise = st.radio("Modo de análise:", ["Nenhum", "Geral", "Por dia"], key="modo2")

    if modo_de_analise in ["Geral", "Por dia"]:
        df_filtrado = df_noticias
        if modo_de_analise == "Por dia":
            datas_disponiveis = sorted(df_noticias['Data'].dt.date.unique())
            data_escolhida = st.selectbox("Escolha uma data disponível:", datas_disponiveis, key="data2")
            df_filtrado = df_noticias[df_noticias['Data'].dt.date == data_escolhida]

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


