import streamlit as st
import csv

# Dicionário de jogadores e seus sinônimos
jogadores = {
    "Vinicius José Paixão de Oliveira Júnior": ["vinicius jr", "vinícius", "vinicius", "vinícius júnior", "vinícius junior", "vinicius júnior", "vinicius junior", "vini jr", "vini", "vini malvadeza", "vinícius josé de oliveira júnior", "melhor jogador do mundo", "malvadeza", "ela é uma boa menina"],
    "Rodrygo Silva de Goes": ["rodrygo", "rayo", "rodrygo goes"],
    "Karim Mostafa Benzema": ["karim", "benzema", "karim benzema"],
    "Marco Asensio Willemsen": ["asensio", "marco asensio"],
    "Federico Santiago Valverde Dipetta": ["valverde", "fede valverde", "federico valverde", "fede"],
    "Luka Modrić": ["modric", "luka modric", "luka modrić"],
    "Éder Gabriel Militão": ["militão", "militao", "éder militão", "eder militão", "éder militao", "eder militao"],
    "Daniel Carvajal Ramos": ["carvajal", "dani carvajal", "daniel carvajal"],
    "José Ignacio Fernández Iglesias": ["nacho", "nacho fernandez", "nacho fernández"],
    "David Olatukunbo Alaba": ["alaba", "david alaba"],
    "Toni Kroos": ["kroos", "toni kroos"],
    "Eduardo Celmi Camavinga": ["camavinga", "eduardo camavinga"],
    "Thibaut Nicolas Marc Courtois": ["courtois", "thibaut courtois"],
    "Antonio Rüdiger": ["rudiger", "antonio rudiger"],
    "Jesús Vallejo Lázaro": ["vallejo", "jesús vallejo", "jesus vallejo"],
    "Ferland Sinna Mendy": ["mendy", "ferland mendy"],
    "Lucas Vázquez Iglesias": ["lucas vázquez", "lucas vazquez", "vázquez", "vazquez"],
    "Aurélien Djani Tchouaméni": ["tchouaméni", "tchouameni"],
    "Eden Michael Hazard": ["hazard", "eden hazard"],
    "Mariano Díaz Mejía": ["mariano díaz", "mariano diaz", "mariano"],
    "Andriy Oleksiyovych Lunin": ["lunin", "andriy lunin"],
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
st.title("Almanaque Real Madrid")

# URL direto para a imagem no GitHub
url_imagem = 'https://upload.wikimedia.org/wikipedia/pt/9/98/Real_Madrid.png'

# Exibir a imagem
st.image(url_imagem, caption='Escudo do Real', use_column_width=False)

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
