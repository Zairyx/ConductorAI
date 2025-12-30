<<<<<<< HEAD
import streamlit as st

st.set_page_config(
    page_title="MaestroIA Marketing",
    layout="wide"
)

st.sidebar.title("🎼 MaestroIA")

page = st.sidebar.selectbox(
    "Navegação",
    ["Dashboard", "Nova Campanha", "Agentes", "Relatórios", "Configurações"]
)

st.title("MaestroIA Marketing")

if page == "Dashboard":
    st.metric("Campanhas Ativas", 3)
    st.metric("ROI Médio", "3.2x")

elif page == "Nova Campanha":
    st.subheader("Criar Nova Campanha")
=======
import streamlit as st
from core.auth import login_user, register_user
from main import run_maestro

st.set_page_config(page_title="MaestroIA", layout="centered")

st.title("🎼 MaestroIA Marketing")

menu = st.sidebar.selectbox("Menu", ["Login", "Cadastro"])

if menu == "Cadastro":
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")

    if st.button("Criar conta"):
        if register_user(email, password):
            st.success("Conta criada com sucesso!")
        else:
            st.error("Usuário já existe.")

if menu == "Login":
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        token = login_user(email, password)
        if token:
            st.session_state["auth"] = True
            st.success("Login realizado!")
        else:
            st.error("Credenciais inválidas.")

if st.session_state.get("auth"):
    st.divider()
    st.subheader("🚀 Executar MaestroIA")
    if st.button("Iniciar Campanha"):
        with st.spinner("Orquestrando agentes..."):
            result = run_maestro()
            st.write(result)
>>>>>>> 53d8f3e (Primeiro commit do MaestroIA)
