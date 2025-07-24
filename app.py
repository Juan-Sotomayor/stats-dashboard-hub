import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stats Hub")
st.title("Intuição Estatística")
st.write("Site em desenvolvimento")

st.write("Explore conceitos de estatística por meio de visualizações interativas.")


#Gerando dados fic
# Cenário: dados diários para 4 semanas (28 dias)
np.random.seed(42)

date_range = pd.date_range(start="2025-01-01", periods=28, freq='D')

serie_a = np.random.randint(10,100, size=28)

df = pd.DataFrame({"Série A": serie_a}, index=date_range)

# Exibir Df
st.title("Tabela dos dados")
st.write("Abaixo, uma representação dos dados no formato de tabela")
st.dataframe(df)

#Gráfico de linha
st.title("Gráfico de linha")
st.write("Representação em linha do mês de Janeiro")
st.line_chart(df)

#Gráfico de linha comparando 

# Adicionar coluna com dia da semana
dias_semana = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
df["Dia da Semana"] = df.index.dayofweek  # 0=Seg, ..., 6=Dom
df["Dia da Semana"] = df["Dia da Semana"].map(dict(enumerate(dias_semana)))

# Numero da semana
df["Semana"] = ((df.index - df.index[0]).days // 7) + 1

# Pivot: index = Dia da Semana, columns = Semana
pivot = df.pivot(index="Dia da Semana", columns="Semana", values="Série A")
pivot.columns = [f"Semana {col}" for col in pivot.columns]  # renomear colunas

# Reordenar os dias da semana
ordem_dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom']
pivot = pivot.loc[ordem_dias]

# Exibir tabela e gráfico
st.write("Série A: comparação entre semanas por dia da semana")
st.dataframe(pivot)

st.line_chart(pivot)

# Aplicando gradiente nas colunas (semanas)
styled = pivot.style.background_gradient(axis=0, cmap='Greens')

st.write("Tabela com gradiente de cor por semana:")
st.dataframe(styled) 