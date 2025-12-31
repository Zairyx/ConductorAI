import streamlit as st
import requests
import json
from maestroia.graphs.marketing_graph import build_marketing_graph

st.title("MaestroIA - Orquestração de Agentes de Marketing")

# Simulação de login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.subheader("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if email and password:
            st.session_state.logged_in = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Credenciais inválidas")
else:
    st.success(f"Logado como {st.session_state.email}")

    graph = build_marketing_graph()

    # Abas para organizar
    tab1, tab2, tab3 = st.tabs(["Campanha", "Configurações", "Resultados"])

    with tab1:
        st.header("Criar Campanha")
        objetivo = st.text_input("Objetivo da Campanha", placeholder="Ex: Aumentar vendas em 30%")
        publico = st.text_input("Público-Alvo", placeholder="Ex: Mulheres 25-40 anos interessadas em bem-estar")
        canais = st.multiselect("Canais", ["Instagram", "Facebook", "Google Ads", "Twitter/X", "LinkedIn", "TikTok", "YouTube", "Pinterest", "Snapchat"])
        orcamento = st.number_input("Orçamento (R$)", min_value=0.0, value=1000.0)

        if st.button("Executar Campanha", type="primary"):
            if not objetivo or not publico or not canais:
                st.error("Preencha todos os campos obrigatórios!")
            else:
                # Barra de progresso
                progress_bar = st.progress(0)
                status_text = st.empty()

                state = {
                    "objetivo": objetivo,
                    "publico_alvo": publico,
                    "canais": canais,
                    "orcamento": orcamento
                }

                # Simular progresso por agente
                agentes = ["pesquisador", "estrategista", "criador_conteudo", "publicador", "otimizador", "maestro"]
                for i, agente in enumerate(agentes):
                    status_text.text(f"Executando {agente}...")
                    progress_bar.progress((i + 1) / len(agentes))
                    # Pequeno delay para visualização
                    import time
                    time.sleep(0.5)

                # Executar campanha
                result = graph.invoke(state)
                st.session_state.last_result = result
                st.session_state.campaign_executed = True

                status_text.text("Campanha concluída!")
                progress_bar.progress(1.0)

                st.success("Campanha executada com sucesso!")

    with tab2:
        st.header("Configurações de Redes Sociais")
        st.info("Configure suas chaves de API para integrações reais. Deixe vazio para usar simulações.")

        with st.expander("Meta (Instagram/Facebook)"):
            st.text_input("Access Token", type="password", key="meta_token")
            st.text_input("App ID", key="meta_app_id")

        with st.expander("Twitter/X"):
            st.text_input("API Key", type="password", key="twitter_api_key")
            st.text_input("API Secret", type="password", key="twitter_api_secret")
            st.text_input("Access Token", type="password", key="twitter_access_token")
            st.text_input("Access Token Secret", type="password", key="twitter_access_secret")

        with st.expander("LinkedIn"):
            st.text_input("Access Token", type="password", key="linkedin_token")

        with st.expander("TikTok"):
            st.text_input("Access Token", type="password", key="tiktok_token")

        with st.expander("YouTube"):
            st.text_input("API Key", type="password", key="youtube_key")

        with st.expander("Pinterest"):
            st.text_input("Access Token", type="password", key="pinterest_token")

        with st.expander("Snapchat"):
            st.text_input("Access Token", type="password", key="snapchat_token")

        if st.button("Salvar Configurações"):
            st.success("Configurações salvas! (Nota: Ainda não persistidas - implementar futuramente)")

    with tab3:
        if "campaign_executed" in st.session_state and st.session_state.campaign_executed:
            result = st.session_state.last_result

            st.header("Resultados da Campanha")

            # Mostrar resumo
            if "pesquisa" in result:
                st.subheader("📊 Pesquisa de Mercado")
                st.write(result["pesquisa"])

            if "conteudos" in result:
                st.subheader("📝 Conteúdos Gerados")
                for i, conteudo in enumerate(result["conteudos"], 1):
                    st.write(f"**Conteúdo {i}:** {conteudo[:200]}...")

            if "publicacoes" in result:
                st.subheader("🚀 Publicações")
                st.json(result["publicacoes"])

            if "imagens" in result:
                st.subheader("🖼️ Imagens Geradas")
                for img_url in result["imagens"]:
                    if img_url.startswith("http"):
                        st.image(img_url, caption="Imagem gerada")
                    else:
                        st.write(img_url)

            # Botões de ação
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("✅ Aprovar e Publicar", type="primary"):
                    st.success("Publicação aprovada! (Integração real pendente)")

            with col2:
                if st.button("🔄 Ajustar Campanha"):
                    st.info("Recarregue a página e ajuste os parâmetros.")

            with col3:
                # Download
                result_json = json.dumps(result, indent=2, ensure_ascii=False)
                st.download_button(
                    label="📥 Baixar Resultados",
                    data=result_json,
                    file_name="campanha_maestroia.json",
                    mime="application/json"
                )
        else:
            st.info("Execute uma campanha primeiro para ver os resultados.")