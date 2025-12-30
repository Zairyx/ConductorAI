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
