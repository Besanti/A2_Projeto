import streamlit as st
import pandas as pd
import numpy as np

st.title('Jogadores Real Madrid')

st.write("Tabela")

dataframe = pd.DataFrame({
    'Nome': ['Vini', 'Benzema', 'Rodrygo', 'Valverde'],
    'Gols': [23, 20, 15, 12]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Vini', 'Benzema', 'Rodrygo'])

st.line_chart(chart_data)
