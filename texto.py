import re
import string
from collections import Counter
import streamlit as st
import pandas as pd

def limpar_tokenizar(texto, ignorarer):
#Limpamos nossos dados, deixando eles cheirosos e filtrados.
    palavra_limpa = re.findall(r'\b\w+\b', texto.lower())
    return [p for p in palavra_limpa if p not in ignorarer]

def limpar_texto(texto, ignorarer):
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    palavra_separ = texto.split()
    return [p for p in palavra_separ if p not in ignorarer and len(p) > 2]

def maiscomuns(df_noticias, ignorarer, numero_palavras=10):
  #Buscamos as palavras mais frequentes!

    todas_as_palavras = []
    for texto_noticia in df_noticias["Notícias"].dropna():
        todas_as_palavras.extend(limpar_texto(texto_noticia, ignorarer))
    contagem_palavras = Counter(todas_as_palavras)
    return contagem_palavras.most_common(numero_palavras)

def procuranoti(palavra, df_filtrado, ignorarer):
    textos = df_filtrado["Notícias"].dropna()
    total_ocorrencias = sum([1 for noticia in textos if palavra in limpar_texto(noticia, ignorarer)])
    st.write(f"A palavra **{palavra}** apareceu em **{total_ocorrencias}** notícia(s).")

    #Exibimos os títulos que contêm a palavra do input
    noticias_filtradas = [noticia for noticia in textos if palavra in limpar_texto(noticia, ignorarer)]
    if noticias_filtradas:
        st.markdown("**Títulos contendo a palavra:**")
        for item_noticia in noticias_filtradas:
            st.markdown(f"- {item_noticia}")

def comparanoti(palavra1, palavra2, df_filtrado, ignorarer, tipo_grafico):
   #comparamos a frequencia de duas noticias em especifico
    textos = df_filtrado["Notícias"].dropna()
    contagem1 = sum([1 for noticia in textos if palavra1 in limpar_texto(noticia, ignorarer)])
    contagem2 = sum([1 for noticia in textos if palavra2 in limpar_texto(noticia, ignorarer)])

    st.write(f"{palavra1}: {contagem1} ocorrência(s)")
    st.write(f"{palavra2}: {contagem2} ocorrência(s)")

    #visualizaçoes
    from visualizacao import comparaplotnoti
    comparaplotnoti(palavra1, palavra2, contagem1, contagem2, tipo_grafico)

    noticias_palavra1 = [noticia for noticia in textos if palavra1 in limpar_texto(noticia, ignorarer)]
    noticias_palavra2 = [noticia for noticia in textos if palavra2 in limpar_texto(noticia, ignorarer)]

    if noticias_palavra1:
        st.markdown(f"**Títulos com {palavra1}:**")
        for item_noticia in noticias_palavra1:
            st.markdown(f"- {item_noticia}")

    if noticias_palavra2:
        st.markdown(f"**Títulos com {palavra2}:**")
        for item_noticia in noticias_palavra2:
            st.markdown(f"- {item_noticia}")
