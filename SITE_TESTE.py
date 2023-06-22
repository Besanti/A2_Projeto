import streamlit as st
import pandas as pd

# Carregar o arquivo CSV
url = 'https://raw.githubusercontent.com/besanti/A2_Projeto/informaçõesjogadores.csv'
df = pd.read_csv(url)

# Título do aplicativo
st.title("Localizador de Jogadores")

# Entrada do nome do jogador
player_name = st.text_input('Digite o nome de um jogador do Real Madrid:')

# Localizar as informações do jogador
player_info = df[df['Nome'] == player_name]

# Exibir as informações do jogador
if not player_info.empty:
    st.write('Informações sobre o Jogador:', player_name)
    st.write(player_info)
else:
    st.write('Jogador não encontrado.')
