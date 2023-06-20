

import requests
from bs4 import beautifulsoup4
import streamlit as st

st.title("Localizador de Jogadores")

title = st.text_input('Digite o nome de um jogador do Real Madrid: ', ':')
st.write('Informações sobre o Jogador', title)




extras = {
    "cr7": {"diga": "O Maior Artilheiro da história do Real Madrid fez 450 gols pelo clube Siiiiiiiiuu"}
}

sinonimos = {
    "Vinícius_Júnior": ["vinicius jr", "vinícius", "vinicius", "vinícius júnior", "vinícius junior", "vinicius júnior", "vinicius junior", "vini jr", "vini", "vini malvadeza", "vinícius josé paixão de oliveira júnior", "melhor jogador do mundo", "malvadeza", "ela é uma boa menina" ],
    "Rodrygo_Goes": ["rodrygo", "rayo", "rodrygo goes"],
    "Karim_Benzema": ["karim", "benzema", "karim benzema"],
    "Marco_Asensio": ["asensio", "marco asensio"],
    "Federico_Valverde": ["valverde", "fede valverde", "federico valverde", "fede"],
    "Luka_Modrić": ["modric", "luka modric", "luka modrić"],
    "Éder_Militão": ["militão", "militao", "éder militão", "eder militão", "éder militao", "eder militao"],
    "Dani_Carvajal": ["carvajal", "dani carvajal", "daniel carvajal"],
    "Nacho_(futebolista)": ["nacho", "nacho fernandez", "nacho fernández"],
    "David_Alaba": ["alaba", "david alaba"],
    "Toni_Kroos": ["kroos", "toni kroos"],
    "Eduardo_Camavinga": ["camavinga", "eduardo camavinga"],
    "Thibaut_Courtois": ["courtois", "thibaut courtois"],
    "Antonio_Rüdiger": ["rudiger", "antonio rudiger"],
    "Jesús_Vallejo": ["vallejo", "jesús vallejo", "jesus vallejo"],
    "Ferland_Mendy": ["mendy", "ferland mendy"],
    "Lucas_Vázquez": ["lucas vázquez", "lucas vazquez", "vázquez", "vazquez"],
    "Aurélien_Tchouaméni": ["tchouaméni", "tchouameni"],
    "Dani_Ceballos": ["dani ceballos", "ceballos"],
    "Eden_Hazard": ["hazard", "eden hazard"],
    "Mariano_Díaz_Mejía": ["mariano díaz", "mariano diaz", "mariano"],
    "Andriy_Lunin": ["lunin"],
}

desempenho = {}

for key, value in sinonimos.items():
    for sinonimo in value:
        desempenho[sinonimo] = desempenho.get(key, {})
        desempenho[sinonimo].update({"gols": 20, "assists": 15})

desempenho["Karim_Benzema"] = {"gols": 31, "assists": 6}
desempenho["Rodrygo_Goes"] = {"gols": 19, "assists": 11}
desempenho["Vinícius_Júnior"] = {"gols": 23, "assists": 21}
desempenho["Marco_Asensio"] = {"gols": 12, "assists": 8}
desempenho["Federico_Valverde"] = {"gols": 12, "assists": 7}
desempenho["Luka_Modrić"] = {"gols": 6, "assists": 6}
desempenho["Éder_Militão"] = {"gols": 7, "assists": 1}
desempenho["Dani_Carvajal"] = {"gols": 0, "assists": 5}
desempenho["Nacho_(futebolista)"] = {"gols": 1, "assists": 1}
desempenho["David_Alaba"] = {"gols": 2, "assists": 3}
desempenho["Toni_Kroos"] = {"gols": 2, "assists": 6}
desempenho["Eduardo_Camavinga"] = {"gols": 0, "assists": 2}
desempenho["Thibaut_Courtois"] = {"gols": 0, "assists": 0}
desempenho["Antonio_Rüdiger"] = {"gols": 2, "assists": 0}
desempenho["Jesús_Vallejo"] = {"gols": 0, "assists": 0}
desempenho["Ferland_Mendy"] = {"gols": 0, "assists": 1}
desempenho["Lucas_Vázquez"] = {"gols": 4, "assists": 3}
desempenho["Aurélien_Tchouaméni"] = {"gols": 0, "assists": 4}
desempenho["Dani_Ceballos"] = {"gols": 1, "assists": 9}
desempenho["Eden_Hazard"] = {"gols": 1, "assists": 2}
desempenho["Mariano_Díaz_Mejía"] = {"gols": 0, "assists": 0}
desempenho["Andriy_Lunin"] = {"gols": 0, "assists": 0}

jogadorao = st.text_input("Digite o nome do jogador Madridista: ")
jogador = jogadorao.lower()


if jogador in desempenho:
    corrected_jogador = None
    for key, value in sinonimos.items():
        if jogador in value:
            corrected_jogador = key
            break

    if corrected_jogador:
        st.write(f"O {jogadorao} tem {desempenho[corrected_jogador]['gols']} gols e {desempenho[corrected_jogador]['assists']} assistências nessa temporada, até o momento em que esse programa foi feito")

        url = 'https://pt.wikipedia.org/wiki/' + corrected_jogador.replace(" ", "_")
        site = requests.get(url)
        soup = BeautifulSoup(site.content, "lxml")
        tabela = soup.find("table", {'class': "infobox"})
        linhas = tabela.find_all(["th", "tr"])

        for index, row in enumerate(linhas):
            if index >= 26:
                break
            cells = row.find_all("td")
            for cell in cells:
                value = cell.get_text(strip=True)
                st.write("The value in this cell is %s" % value)
    else:
        st.write("Não foi possível encontrar sinônimos para o jogador informado.")
