

import requests

import streamlit as st

st.title("Localizador de Jogadores")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
