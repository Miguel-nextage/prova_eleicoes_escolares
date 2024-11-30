import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep

# Configuração inicial da página

st.set_page_config(page_title="Sistema de Votação com Gráfico", layout="centered")

# Títulos e descrição
st.title("🗳️ Sistema de Votação")
st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

# Variáveis de estado para armazenar votos
if "votos_candidato1" not in st.session_state:
    st.session_state.votos_candidato1 = 0

if "votos_candidato2" not in st.session_state:
    st.session_state.votos_candidato2 = 0

if "ja_votou" not in st.session_state:
    st.session_state.ja_votou = False

# Verifica se o usuário já votou

col1, col2 = st.columns(2)

with col1:
    if st.button("Discurso do candidato 1"):
        webbrowser.open("https://drive.google.com/file/d/1YJOv0VQ5r7zRlWuPXgO2Dnzn5vA9S4Yb/view")
with col2:
        if st.button("Discurso do candidato 2"):
            webbrowser.open("https://drive.google.com/file/d/1AZausUdYaAfLX70AU1VNTdWBbg1MxvQd/view")

if st.session_state.ja_votou:
    st.warning("Você já votou! Obrigado por participar.")
else:
    # Botões de votação
    col3, col4 = st.columns(2)

    with col3:
        if st.button("Votar no Candidato 1"):  
            st.session_state.votos_candidato1 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 1!")
 
    with col4:
        if st.button("Votar no Candidato 2"):
            st.session_state.votos_candidato2 += 1
            st.session_state.ja_votou = True
            st.success("Seu voto foi registrado para o Candidato 2!")
            
col5, col6 = st.columns(2)
with col5:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZKGt2jCtNO-DJdIg4em02pymsSpmODM9GFg&s", width=160)
with col6:
    st.image("https://media.tenor.com/UPiEUVO2Q04AAAAe/mulch-mulch-dog.png", width=160)

if st.button("Ver resultado"):
    st.success("Transferindo")
    sleep(0.5)
    st.switch_page("pages/resultado.py")
