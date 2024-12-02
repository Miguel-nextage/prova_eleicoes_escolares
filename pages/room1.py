import streamlit as st
import matplotlib.pyplot as plt
import random
from io import BytesIO
import time
import webbrowser
from time import sleep
from PIL import Image
 

#cores

st.markdown("""
        <style>
            /*Estilo para o título */
            h1 {
                color: #FFFCCC;
                font-size: 30px;
                font-weight: bold;
            }

        .stButton>button {
            width: 260px;
            background-color: green;
            color: white;     
            padding: 15px 30px;
            font-size: 16px;
            border-radius: 30px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto;

        }

        .stButton>button:hover {
            background-color: darkred;  /* Cor do botão ao passar o mouse */
        }
        .bt1 >button {
            background-color: #777666;  /* Cor do botão 1 */
            color: white;  /* Cor do texto */
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .bt1 > button:hover {
            background-color: #777666;  /* Cor ao passar o mouse para o botão 1 */
        }
            
            .candidato > button {
            background-color: #777555;  /* cor para o botao de resultado */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
            font-size: 18px;
            border-radios: 15;
        }

        .button_candidato2 > button:hover {
            background-color: #0000FF;  /* Cor ao passar o mouse para o botão do Candidato 2 */
        }
            
        </style>
            
            
    """, unsafe_allow_html=True)

# Configuração inicial da págin


# Títulos e descrição
st.title("🗳️ Sistema de Votação")

st.write("Vote com cuidado! Veja com atenção o discurso de cada um, e então vote. Você só pode votar uma vez!")

st.write("")
st.write("")
st.write("")


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
        webbrowser.open("https://drive.google.com/file/d/11IVI3_s0NYogvjrYesEWxzz2KC7oO9Wv/view")
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
            



if st.button("Resultado", key="candidato", help="Ver resultado das eleições", use_container_width=True):
    st.success("Redirecionando...")
    sleep(0.5)
    st.switch_page("pages/resultado.py")
