import streamlit as st
import csv

# Função para procurar o jogador no arquivo CSV
def procurar_jogador(nome_jogador, informacoesjogadores):
    with open(informacoesjogadores, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for jogador in leitor_csv:
            if jogador['Nome Completo'].lower() == nome_jogador.lower():
                return jogador
    return None

# Título do aplicativo
st.title("Localizador de Jogadores")

# Entrada do nome do jogador
nome_jogador = st.text_input('Digite o nome de um jogador:')

# Chamar a função para procurar o jogador
jogador_encontrado = procurar_jogador(nome_jogador, 'nome_do_arquivo.csv')

# Exibir as informações do jogador, se encontrado
if jogador_encontrado:
    st.write("Informações do jogador:")
    for chave, valor in jogador_encontrado.items():
        st.write(f"{chave}: {valor}")
else:
    st.write("Jogador não encontrado no arquivo CSV.")

