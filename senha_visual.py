import streamlit as st
import time
import os

st.set_page_config(page_title="Painel de Chamada", layout="centered")
st.title("Painel de Chamada")
st.image('Meli.jpg')

placeholder = st.empty()

def ler_senhas():
    if not os.path.exists("senhas.txt"):
        return []
    with open("senhas.txt", "r") as f:
        linhas = f.readlines()
    return [linha.strip() for linha in linhas if linha.strip()]

# Loop para atualizar dinamicamente (a cada segundo)
while True:
    senhas = ler_senhas()
    senha_atual = senhas[-1] if senhas else "---"
    ultimas_20 = senhas[-20:][::-1]  # últimas 20, ordem mais recente no topo

    with placeholder.container():
        st.subheader("🔔 Senha Atual:")
        st.markdown(f"<h1 style='color: blue; font-size: 72px;'>{senha_atual}</h1>", unsafe_allow_html=True)
        st.subheader("📋 Últimas 20 Senhas Chamadas:")
        for senha in ultimas_20:
            st.write(f"🔹 Senha {senha}")

    time.sleep(1)