import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CryptoInsight", layout="wide")
st.title("CryptoInsight Dashboard")

#conectar ao banco
conn = sqlite3.connect('dados_cripto.db')
df = pd.read_sql_query("SELECT * FROM precos", conn)
conn.close()

#sidebar
st.sidebar.header("Filtros")
moeda_selecionada = st.sidebar.selectbox("Selecione a moeda:", df['moeda'].unique())

#filtrar dados
dados_filtrados = df[df['moeda'] == moeda_selecionada]

#métricas
col1, col2, col3, col4 = st.columns(4)
col1.metric("Preço Atual", f"U$ {dados_filtrados['preco_usd'].iloc[-1]:.2f}")
col2.metric("Média", f"U$ {dados_filtrados['preco_usd'].mean():.2f}")
col3.metric("Volatilidade", f"±U$ {dados_filtrados['preco_usd'].std():.2f}")
col4.metric("Registros", len(dados_filtrados))

#grafico
fig = px.line(dados_filtrados, x='data_hora', y='preco_usd', 
              title=f"Evolução do Preço - {moeda_selecionada}")
st.plotly_chart(fig)

#table
st.subheader("Últimos Registros")
st.dataframe(dados_filtrados.tail(10))