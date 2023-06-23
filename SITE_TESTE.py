import streamlit as st
import csv

# Dicionário de jogadores e seus sinônimos
jogadores = {
    "Vinicius José Paixão de Oliveira Júnior": ["vinicius jr", "vinícius", "vinicius", "vinícius júnior", "vinícius junior", "vinicius júnior", "vinicius junior", "vini jr", "vini", "vini malvadeza", "vinícius josé de oliveira júnior", "melhor jogador do mundo", "malvadeza", "ela é uma boa menina"],
    "Rodrygo Silva de Goes": ["rodrygo", "rayo", "rodrygo goes"],
    "Karim Mostafa Benzema": ["karim", "benzema", "karim benzema"]
}

# Função para procurar o jogador no arquivo CSV
def procurar_jogador(nome_jogador, informacoesjogadores):
    with open(informacoesjogadores, 'r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for jogador in leitor_csv:
            for sinonimo in jogadores[jogador['Nome Completo']]:
                if sinonimo.lower() == nome_jogador.lower():
                    return jogador
    return None

# Título do aplicativo
st.title("Localizador de Jogadores")

# Entrada do nome do jogador
nome_jogador = st.text_input('Digite o nome de um jogador:')

# Chamar a função para procurar o jogador
jogador_encontrado = procurar_jogador(nome_jogador, 'informacoesjogadores.csv')

# Exibir as informações do jogador, se encontrado
if jogador_encontrado:
    st.write("Informações do jogador:")
    for chave, valor in jogador_encontrado.items():
        st.write(f"{chave}: {valor}")
else:
    st.write("Jogador não encontrado no arquivo CSV.")
