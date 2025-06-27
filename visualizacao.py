
import matplotlib.pyplot as plt
import streamlit as st

def frequennoti(dados, tipo_grafico):
  #Vamos criar graficos com base nos nossos dados
    if not dados:
        st.write("Não há dados para gerar o gráfico.")
        return

    palavras, frequencias = zip(*dados)
    figura, eixo = plt.subplots(figsize=(max(10, len(palavras) * 0.8), 6)) #Ajustamos o tamanho da figura

    if tipo_grafico == "Colunas":
        eixo.bar(palavras, frequencias, color='skyblue')
        eixo.set_ylabel("Frequência")
        eixo.set_title("Frequência de Palavras (Colunas)")
        eixo.set_xticklabels(palavras, rotation=45, ha='right')
    elif tipo_grafico == "Barras horizontais":
        eixo.barh(palavras, frequencias, color='salmon')
        eixo.invert_yaxis()
        eixo.set_xlabel("Frequência")
        eixo.set_title("Frequência de Palavras (Barras Horizontais)")
    elif tipo_grafico == "Pizza":
        figura, eixo = plt.subplots() 
        eixo.pie(frequencias, labels=palavras, autopct='%1.1f%%', startangle=90)
        eixo.axis('equal') 
        eixo.set_title("Frequência de Palavras (Pizza)")

    st.pyplot(figura)

def comparaplotnoti(palavra1, palavra2, contagem1, contagem2, tipo_grafico):
    #Geramos graficos comparativos das palavras pesquisadas
    rotulos = [palavra1, palavra2]
    contagens = [contagem1, contagem2]

    figura, eixo = plt.subplots()

    if tipo_grafico == "Colunas":
        eixo.bar(rotulos, contagens, color=["mediumorchid", "gold"])
        eixo.set_ylabel("Frequência")
        eixo.set_title(f"Comparação de Frequência: '{palavra1}' vs '{palavra2}' (Colunas)")
    elif tipo_grafico == "Pizza":
        #Caso ambas sejam 0 
        if contagem1 == 0 and contagem2 == 0:
            st.write("Ambas as palavras têm 0 ocorrências, não é possível gerar gráfico de pizza.")
            plt.close(figura) 
            return
        eixo.pie(contagens, labels=rotulos, autopct='%1.1f%%', startangle=90, colors=["mediumorchid", "gold"])
        eixo.axis('equal') 
        eixo.set_title(f"Comparação de Frequência: '{palavra1}' vs '{palavra2}' (Pizza)")

    st.pyplot(figura)

